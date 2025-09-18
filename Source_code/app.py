import gradio as gr
from huggingface_hub import InferenceClient
from excel_checker import analyze_excel
from data import questions, scenario_prompts
import random, re, io, tempfile, os, base64, requests
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# === System message for LLM ===
system_message = """
You are ExcelBot, an AI interviewer for Excel.
Responsibilities:
1. Evaluate answers flexibly — accept synonyms or close variations.
2. Always respond in this format:
   - ✅ Correct! (short explanation)
   - ❌ Incorrect. The correct answer is: <answer> (short explanation)
3. Keep responses short and professional.
4. Do NOT ask the next question — Python backend controls that.
"""

# === Interview Bot Logic ===
def interview_bot(
    message,
    history,
    difficulty,
    score_state,
    index_state,
    asked_state,
    quiz_report,
    quiz_done,
    candidate_name,
    hf_token: gr.OAuthToken
):
    client = InferenceClient(token=hf_token.token, model="openai/gpt-oss-20b")

    if difficulty is None:
        level = message.strip().lower()
        if level in ["beginner", "intermediate", "advanced"]:
            difficulty = level.capitalize()
            asked_state = random.sample(questions[difficulty], 5)
            index_state = 1
            history.append({
                "role": "assistant",
                "content": f"Great choice {candidate_name}! You selected {difficulty} level.\n\n**Question 1:** {asked_state[0]['question']}"
            })
            return "", history, difficulty, score_state, index_state, asked_state, quiz_report, quiz_done
        else:
            history.append({
                "role": "assistant",
                "content": f"Please type to select proficiency, {candidate_name}: beginner / intermediate / advanced."
            })
            return "", history, difficulty, score_state, index_state, asked_state, quiz_report, quiz_done

    current_q = asked_state[index_state - 1]
    eval_prompt = f"""
Question: {current_q['question']}
Correct answer: {current_q['answer']}
Accepted alternatives: {', '.join(current_q['alternatives'])}
User's answer: {message}

Judge correctness flexibly.
"""

    try:
        completion = client.chat_completion(
            [{"role": "system", "content": system_message},
             {"role": "user", "content": eval_prompt}],
            max_tokens=200,
            temperature=0.3,
        )
        feedback = completion.get("choices", [{}])[0].get("message", {}).get("content")
    except Exception as e:
        feedback = f"⚠️ Error: {str(e)}"

    if not feedback:
        feedback = "⚠️ No response received from model."

    if "✅" in feedback:
        score_state += 1

    history.append({"role": "assistant", "content": feedback})

    if index_state >= 5:
        result = "✅ PASS! Congratulations, you did well." if score_state >= 3 else "❌ FAIL. Please practice more and try again."
        summary = f"🎉 Quiz complete! Final Score: {score_state}/5\n{result}"
        history.append({"role": "assistant", "content": summary})

        quiz_report = summary
        quiz_done = True
        return "", history, None, 0, 0, [], quiz_report, quiz_done

    next_q = asked_state[index_state]["question"]
    history.append({"role": "assistant", "content": f"**Question {index_state+1}:** {next_q}"})
    index_state += 1

    return "", history, difficulty, score_state, index_state, asked_state, quiz_report, quiz_done


# === Combine Reports ===
def combine_reports(quiz_report, checker_report, candidate_name, candidate_email):
    if not quiz_report or not checker_report:
        return "⚠️ Please complete both the quiz and Excel checker first."

    final = f"""
📑 Final Candidate Report
===========================

👤 Candidate Info
---------------------------
Name: {candidate_name}
Email: {candidate_email}

🎓 Quiz Results
---------------------------
{quiz_report}

📊 Excel File Evaluation
---------------------------
{checker_report}

🏆 Overall Verdict
---------------------------
"""
    if "✅ PASS" in quiz_report.upper() and "✅ PASS" in checker_report.upper():
        final += "✅ Candidate passed both theory and practical."
    else:
        final += "❌ Candidate did not meet the required proficiency level."

    return final


# === Generate PDF ===
def generate_pdf(report_text, candidate_name):
    styles = getSampleStyleSheet()
    story = []
    for line in report_text.split("\n"):
        story.append(Paragraph(line, styles["Normal"]))
        story.append(Spacer(1, 10))

    tmpdir = tempfile.mkdtemp()
    filename = os.path.join(tmpdir, f"{candidate_name.replace(' ', '_')}_Excel_Report.pdf")
    doc = SimpleDocTemplate(filename)
    doc.build(story)
    return filename


# === Send Email via Resend ===
def send_email_resend(to_email, cc_email, subject, body, pdf_path):
    RESEND_API_KEY = os.getenv("RESEND_API_KEY")
    if not RESEND_API_KEY:
        return "❌ Missing RESEND_API_KEY environment variable"

    url = "https://api.resend.com/emails"
    headers = {
        "Authorization": f"Bearer {RESEND_API_KEY}",
        "Content-Type": "application/json"
    }

    with open(pdf_path, "rb") as f:
        pdf_data = base64.b64encode(f.read()).decode("utf-8")

    data = {
        "from": "ExcelBot <onboarding@resend.dev>",    # keep as is or change to verified domain later
        "to": [to_email],
        "cc": [cc_email] if cc_email else [],
        "subject": subject,
        "html": f"<p>{body}</p>",
        "attachments": [
            {
                "filename": os.path.basename(pdf_path),
                "content": pdf_data,
                "type": "application/pdf"
            }
        ]
    }

    resp = requests.post(url, headers=headers, json=data)
    return resp.text


# === Gradio App ===
with gr.Blocks() as demo:
    with gr.Sidebar():
        gr.LoginButton()

    gr.Markdown("## 📊 Excel Interview Assistant\nYour personal AI interviewer and Excel checker.")

    # === Candidate Info ===
    with gr.Tab("👤 Candidate Info") as info_tab:
        name_box = gr.Textbox(label="Your Name", placeholder="Enter your full name")
        email_box = gr.Textbox(label="Your Email", placeholder="Enter your email address")
        save_btn = gr.Button("Save Info")
        info_status = gr.Textbox(label="Status", interactive=False)

        candidate_name = gr.State("")
        candidate_email = gr.State("")

    with gr.Tabs() as tabs:
        # === Tab 1: Interview Bot (start hidden) ===
        with gr.Tab("💬 Excel Interview Bot", visible=False) as quiz_tab:
            chatbot = gr.Chatbot(type="messages", value=[
                {"role": "assistant", "content": "👋 Hi! Please fill in your info first under 'Candidate Info' tab, then start the quiz by choosing a level: beginner / intermediate / advanced."}
            ])
            msg = gr.Textbox(label="Your Answer")

            difficulty = gr.State(None)
            score = gr.State(0)
            index = gr.State(0)
            asked = gr.State([])
            quiz_report = gr.State("")
            quiz_done = gr.State(False)
            checker_report = gr.State("")
            final_report = gr.State("")

            msg.submit(
                fn=interview_bot,
                inputs=[msg, chatbot, difficulty, score, index, asked, quiz_report, quiz_done, candidate_name],
                outputs=[msg, chatbot, difficulty, score, index, asked, quiz_report, quiz_done],
            )

        # === Tab 2: Excel Checker ===
        with gr.Tab("Excel Checker", visible=False) as checker_tab:
            gr.Markdown("### 📊 Upload your Excel file based on the given scenario")

            level = gr.Dropdown(["Beginner", "Intermediate", "Advanced"], label="Select Proficiency Level")
            scenario_box = gr.Textbox(label="Scenario", lines=8, interactive=False)
            candidate_file = gr.File(label="Upload Excel File", file_types=[".xlsx"], type="filepath")
            output_box = gr.Textbox(label="Analysis Report", lines=20)

            def show_scenario(level):
                return scenario_prompts[level]

            level.change(fn=show_scenario, inputs=level, outputs=scenario_box)

            def run_checker(f, lvl):
                res = analyze_excel(f, lvl)
                return res, res

            analyze_button = gr.Button("Analyze Excel")
            analyze_button.click(
                fn=run_checker,
                inputs=[candidate_file, level],
                outputs=[output_box, checker_report],
            )

        # Unlock checker when quiz done
        quiz_done.change(fn=lambda q: gr.update(visible=True) if q else gr.update(), inputs=quiz_done, outputs=checker_tab)

        # === Tab 3: Final Report ===
        with gr.Tab("📑 Final Report", visible=False) as report_tab:
            final_box = gr.Textbox(label="Final Candidate Report", lines=25)
            download_btn = gr.File(label="Download Report PDF")

        def unlock_and_generate_report(quiz_report, checker_report, candidate_name, candidate_email):
            if not quiz_report or not checker_report:
                return gr.update(visible=False), "", None, ""

            report = combine_reports(quiz_report, checker_report, candidate_name, candidate_email)
            pdf_path = generate_pdf(report, candidate_name)

            owner_email = os.getenv("OWNER_EMAIL")
            if owner_email:
                try:
                    email_body = (
                        f"Candidate: {candidate_name}\n"
                        f"Candidate email: {candidate_email}\n\n"
                        f"Quiz Result:\n{quiz_report}\n\n"
                        f"Excel Checker Result:\n{checker_report}\n\n"
                        "Full report attached."
                    )
                    _ = send_email_resend(owner_email, None, f"{candidate_name} - Result", email_body, pdf_path)
                except Exception:
                    pass

            return gr.update(visible=True), report, pdf_path, ""

        checker_report.change(
            fn=unlock_and_generate_report,
            inputs=[quiz_report, checker_report, candidate_name, candidate_email],
            outputs=[report_tab, final_box, download_btn],
        )

    # === Unlock quiz after info ===
    def save_info(name, email):
        if not name or not email:
            return "❌ Please enter both name and email.", name, email, gr.update(visible=False), gr.update(visible=True)
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return "❌ Invalid email format. Please enter a valid email.", name, email, gr.update(visible=False), gr.update(visible=True)
        return f"✅ Info saved! Welcome {name}. You can now start the quiz.", name, email, gr.update(visible=True), gr.update(visible=False)

    save_btn.click(
        fn=save_info,
        inputs=[name_box, email_box],
        outputs=[info_status, candidate_name, candidate_email, quiz_tab, info_tab],
    )


if __name__ == "__main__":
    demo.launch()
