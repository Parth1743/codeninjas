

# 📑 Excel Interview Assistant – Documentation

## 1. Core Requirements Fulfilled

### 1.1 Structured Interview Flow ✅

* The agent introduces itself and guides the candidate.
* Flow is sequential:

  1. Candidate Info Collection (Name + Email validation)
  2. Quiz (multi-turn Q\&A session with 5 randomized questions based on difficulty)
  3. Excel Checker (scenario-based hands-on task with automated validation)
  4. Final Report (auto-generated + downloadable as PDF, emailed silently to owner).
* Tabs (Gradio UI) are **progressively unlocked** to enforce structured flow.

---

### 1.2 Intelligent Answer Evaluation ✅

* Uses **Hugging Face InferenceClient** with `openai/gpt-oss-20b`.
* Prompts are **flexible evaluation prompts** → allows synonyms and variations (not strict matching).
* Returns:

  * ✅ Correct (short explanation)
  * ❌ Incorrect (with correct answer)

---

### 1.3 Agentic Behavior & State Management ✅

* Agent maintains state across turns:

  * Current question index
  * Candidate’s score
  * Quiz completion status
* Unlocks next stage **only after completing the previous stage**.
* Feels like a **human interviewer**: greets with candidate’s name, gives contextual instructions, and provides feedback.

---

### 1.4 Constructive Feedback Report ✅

* At quiz end → candidate gets a **score and pass/fail verdict**.
* Excel checker → provides a **detailed report of detected features** (formulas, formatting, etc.).
* Final Report →

  * Candidate info (Name, Email)
  * Quiz performance summary
  * Excel task evaluation
  * Overall verdict
* Auto-generated PDF report (downloadable).
* Report is also **emailed silently to the owner** (audit trail).

---

## 2. Expected Deliverables

### 2.1 Design Document & Approach Strategy

✅ Attached separately (`DESIGN_DOC.md`) explaining architecture, flows, and reasoning.

---

### 2.2 Working Proof-of-Concept (PoC)

#### Source Code

* Full runnable code available in repo (`app.py`, `excel_checker.py`, `data.py`).

#### Deployed Link

* Hugging Face Space: \[🔗 Add Your Space Link Here]

#### Sample Transcripts

**Example 1 – Beginner Level Quiz**

```
🤖: Hi PARTH! Welcome to the Excel interview. Let's start.  
🤖: Question 1: What is the difference between A1 and $A$1?  
👤: A1 moves when copied, $A$1 stays fixed.  
🤖: ✅ Correct! A1 is relative, $A$1 is absolute.  
...  
🎉 Quiz complete! Final Score: 5/5  
✅ PASS! Congratulations, you did well.  
```

**Example 2 – Excel Checker Output**

```
📊 Checking Excel file for Beginner scenario...  
✔️ SUM formulas found in column E  
✔️ AVERAGE formulas found in column F  
✔️ Conditional formatting detected  

📊 Final Score: 3/3 (100%) → ✅ PASS
```

**Example 3 – Final Report**

```
📑 Final Candidate Report  

👤 Candidate Info  
Name: John Doe  
Email: john@example.com  

🎓 Quiz Results  
Score: 4/5 → ✅ PASS  

📊 Excel File Evaluation  
Final Score: 2/3 → ❌ FAIL  

🏆 Overall Verdict  
❌ Candidate did not meet the required proficiency level.
```

---

## 3. Technical Stack

* **Framework:** Gradio + Hugging Face Spaces
* **LLM Evaluation:** Hugging Face Inference API (`openai/gpt-oss-20b`)
* **Excel Checking:** `openpyxl`, `pandas`
* **Report Generation:** ReportLab (PDF)
* **Email Notifications:** Resend API (owner only)

---

## 4. Key Differentiators

* Progressive flow with tab unlocking → structured process.
* Flexible AI-powered evaluation (not rule-based only).
* Auto-generated **PDF Final Report**.
* Silent email notifications to owner (for audit).
* Personalization: bot greets candidate by name.

---
