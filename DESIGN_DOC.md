
# 📑 Design Document – Excel Interview Assistant  

## 1. Problem Statement  
Hiring managers need a consistent, automated way to evaluate Excel proficiency of candidates.  
Traditional Q&A interviews are time-consuming and subjective. This bot simulates an Excel interviewer, asks structured questions, evaluates answers with flexibility, and validates uploaded Excel assignments automatically.  

---

## 2. Solution Overview  
The solution is an **AI-powered Excel Interview Assistant** that:  
- Conducts interactive interviews with candidates (Q&A style).  
- Adapts difficulty level (Beginner, Intermediate, Advanced).  
- Evaluates answers flexibly using an **LLM** for semantic understanding.  
- Provides immediate feedback and final **Pass/Fail**.  
- Includes **scenario-based Excel assignments** where candidates upload a file.  
- Automatically checks formulas, formatting, pivots, validation rules, and more.  

Deployment is done via **Hugging Face Spaces** for easy access by evaluators and candidates.  

---

## 3. System Architecture  

### Components:
1. **Frontend (Gradio UI)**  
   - Chatbot tab for structured Q&A.  
   - Excel Checker tab for file uploads.  
   - Clean, tab-based interface with onboarding message.  

2. **Backend Logic**  
   - **Interview Manager**: Handles state (difficulty, score, current question).  
   - **LLM Evaluator**: Hugging Face `InferenceClient` with `gpt-oss-20b` for answer evaluation.  
   - **Excel Checker**: Python + OpenPyXL rules to verify candidate submissions.  

3. **Data**  
   - Curated question bank (45+ Q&As) with acceptable alternatives.  
   - Scenario-based problem sets (1 beginner, 1 intermediate, 1 advanced).  

---

## 4. Interview Flow  

1. Bot introduces itself and asks user to choose proficiency: beginner / intermediate / advanced.  
2. Picks 5 random questions from that level.  
3. After each answer:  
   - Uses LLM + rule-based matching for correctness.  
   - Responds with ✅ or ❌ + short explanation.  
   - Keeps internal score.  
4. At end:  
   - Displays final score + **Pass/Fail (≥3/5 = Pass)**.  
   - Optionally assigns an Excel scenario task.  

---

## 5. Excel Checker Flow  

1. Candidate uploads `.xlsx` file.  
2. Rules checked (based on proficiency):  
   - **Beginner**: SUM, AVERAGE, conditional formatting.  
   - **Intermediate**: VLOOKUP/XLOOKUP, Total Sales formulas, data validation, pivot tables.  
   - **Advanced**: Nested IF, pivot tables, charts, macros.  
3. Generates detailed report: which checks passed/failed.  
4. Outputs score and Pass/Fail (≥70% = Pass).  

---

## 6. Technical Stack  
- **Frontend/UI**: Gradio (Blocks, Tabs, ChatInterface).  
- **LLM**: Hugging Face `openai/gpt-oss-20b`.  
- **Excel Analysis**: Python, OpenPyXL.  
- **Deployment**: Hugging Face Spaces (Docker-free, public).  

---

## 7. Strengths & Justification  
- **Hugging Face**: Free, shareable, requires no infra setup.  
- **Gradio**: Simple to build UI, easy candidate interaction.  
- **LLM + Rules**: Combines semantic flexibility (LLM) with deterministic checks (rules).  
- **Extendable**: Can add new scenarios, new questions, or fine-tune model later.  

---

## 8. Future Improvements  
- Add email reporting (send results to candidate + recruiter).  
- Store candidate results in a database (SQLite/Postgres).  
- Fine-tune LLM on actual interview transcripts for better accuracy.  
- Improve Excel Checker to detect charts, pivots, macros more robustly.  
- Gamify with timer/leaderboards.  

---

## 9. Example Transcript  

**Bot:** 👋 Hi! I am your AI Excel interviewer. Please choose: beginner / intermediate / advanced.  
**Candidate:** beginner  
**Bot:** Great! Let’s start.  

**Q1:** What is the difference between A1 and $A$1?  
**Candidate:** relative vs absolute reference  
**Bot:** ✅ Correct! Good job.  

... (5 questions) ...  

**Bot:** 🎉 Quiz complete! Final Score: 4/5 → ✅ PASS  
