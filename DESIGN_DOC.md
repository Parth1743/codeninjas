
# 📑 Design Document – Excel Interview Assistant

## 1. Problem Statement

Hiring managers need a consistent, automated way to evaluate Excel proficiency of candidates.
Traditional interviews are:

* Time-consuming
* Subjective
* Hard to scale

This solution automates Excel assessments via an **AI Interview Assistant** that simulates a real interviewer, evaluates Q\&A responses, validates uploaded Excel assignments, and generates professional reports.

---

## 2. Solution Overview

The **Excel Interview Assistant** provides:

* **Login & Verification** → Secure Hugging Face login, candidate details validation.
* **Structured Interview** → Multi-turn Q\&A (Beginner, Intermediate, Advanced).
* **AI Evaluation** → LLM-powered semantic correctness checking.
* **Practical Assessment** → Excel scenario tasks validated via automated checker.
* **Reporting** → Auto-generated PDF report, silent email delivery to owner.

Deployment is done via **Hugging Face Spaces**, making it accessible to both recruiters and candidates without setup.

---

## 3. System Architecture

### Components

1. **Frontend (Gradio UI)**

   * Sidebar: Hugging Face Login.
   * Tab 1: Candidate Info (Name, Email validation).
   * Tab 2: Interview Bot (Q\&A with chatbot UI).
   * Tab 3: Excel Checker (scenario-based file uploads).
   * Tab 4: Final Report (PDF download + email to owner).

2. **Backend Logic**

   * **Interview Manager** → Tracks difficulty, score, and current progress.
   * **LLM Evaluator** → Uses Hugging Face `InferenceClient` (`openai/gpt-oss-20b`) for intelligent, flexible scoring.
   * **Excel Checker** → Python + OpenPyXL-based rule verification.
   * **Report Generator** → Builds structured PDF via ReportLab.
   * **Email Notifier** → Sends results silently to recruiter using Resend API.

3. **Data**

   * Question bank: curated Q\&A pool with acceptable alternatives.
   * Scenario prompts: beginner, intermediate, advanced Excel tasks.

---

## 4. Candidate Flow (Step-by-Step)

1. **Login with Hugging Face**

   * Ensures authenticated, verified candidate sessions.

2. **Fill Candidate Info**

   * Enter **Name** and **Email**.
   * Email format validated.
   * Once saved → Candidate Info tab is locked to prevent tampering.
   * Interview Bot tab is unlocked.

3. **Interview Stage**

   * Candidate selects difficulty (Beginner/Intermediate/Advanced).
   * 5 random questions asked in sequence.
   * Answers are evaluated via LLM with semantic flexibility.
   * Bot provides ✅ / ❌ with short explanations.
   * Final summary → Score (/5) + Pass/Fail.
   * If quiz completed → Excel Checker tab unlocked.

4. **Excel Checker Stage**

   * Candidate receives scenario prompt.
   * Uploads `.xlsx` file solution.
   * Automated rule-based checker validates formulas, pivots, formatting, etc.
   * Generates detailed pass/fail report.
   * Once analysis complete → Final Report tab unlocked.

5. **Final Report Stage**

   * Consolidates candidate info, quiz performance, and Excel evaluation.
   * Verdict → ✅ Pass if both theory & practical are cleared, ❌ Fail otherwise.
   * Candidate can download a PDF.
   * Recruiter receives report silently via Resend email.

---

## 5. Interview Flow

1. Candidate Info collected.
2. Quiz session begins → 5 multi-turn Q\&A.
3. Each answer:

   * Evaluated with context-aware LLM.
   * Scoring updated.
4. At end of quiz → result shown.
5. Unlocks Excel Checker → file-based validation.
6. Final Report → pass/fail verdict, PDF generated, recruiter notified.

---

## 6. Excel Checker Flow

* **Beginner**: Check for SUM, AVERAGE, conditional formatting.
* **Intermediate**: Check for VLOOKUP/XLOOKUP, totals, validation, pivot tables.
* **Advanced**: Nested IF, pivots, charts, macros.
* Each feature detected → contributes to score.
* Pass threshold: **≥70% features met**.

---

## 7. Technical Stack

* **Frontend/UI** → Gradio (Blocks, Tabs, States).
* **Authentication** → Hugging Face OAuth login.
* **LLM Evaluation** → Hugging Face `InferenceClient` (`openai/gpt-oss-20b`).
* **Excel Analysis** → Python, OpenPyXL.
* **Report Generation** → ReportLab (PDF).
* **Email Delivery** → Resend API (to recruiter only).
* **Deployment** → Hugging Face Spaces.

---

## 8. Strengths & Justification

* **Structured, progressive flow** → no skipping ahead.
* **Human-like evaluation** → AI adapts to synonyms, natural responses.
* **Rule-based Excel validation** → ensures objectivity.
* **Professional reports** → PDF + recruiter email for audit trail.
* **Secure** → Requires Hugging Face login, validated candidate info.

---

## 9. Future Improvements

* Dual email delivery (candidate + recruiter).
* Database integration (SQLite/Postgres) for persistent results.
* Advanced NLP fine-tuning for improved evaluation accuracy.
* Richer Excel validation (charts, pivot drill-down, macros detection).
* Gamification (timed rounds, leaderboards).

---

## 10. Example Transcript

**Bot:** 👋 Hi! Please log in with Hugging Face and enter your details to start.
**Candidate:** Logged in + Info saved.
**Bot:** Great, PARTH! You selected Beginner level.

**Q1:** What is the difference between A1 and \$A\$1?
**Candidate:** relative vs absolute reference
**Bot:** ✅ Correct! A1 moves when copied, \$A\$1 stays fixed.

... (5 questions) ...

**Bot:** 🎉 Quiz complete! Final Score: 4/5 → ✅ PASS
**Bot:** Excel Checker unlocked. Please upload your assignment file.

---
