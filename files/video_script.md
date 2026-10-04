# 3-MINUTE SCREEN RECORDING SCRIPT & WALKTHROUGH GUIDE
**Target Duration:** Exactly 2 minutes 50 seconds (under the 3:00 cap)  
**Format:** Live screen capture (Terminal + Excel + Streamlit App). No slide decks.  
**Tone:** Concise, analytical, confident.

---

## Part 1: Chronological Walkthrough & Speaking Script

### [0:00 – 0:25] The Mystery: ₹23 Crore vs ₹11 Lakh
* **On Screen:** Open `email-thread.txt`. Highlight Arjun Mehta’s email: *"sums to well over a crore a quarter... export is a mess"* and Sameer’s reply: *"around Rs 11 lakh a quarter."*
* **Say:**  
  *"Arjun Mehta was alarmed because his raw support export showed over ₹23 Crore in refunds—well over a crore a quarter. Meanwhile, Helpdesk IT claimed it was around ₹11 Lakh a quarter. One of them was misreading the data. Our job was to find the truth, reconcile every single rupee, and uncover where money is actually leaking."*

---

### [0:25 – 0:55] Terminal Run & Deterministic Reconciliation
* **On Screen:** Open terminal and run:
  ```bash
  python refunds.py --data . --out out
  ```
  Switch to `refund_summary.xlsx` -> `Reconciliation` tab.
* **Say:**  
  *"Running `refunds.py` reconciles the export in under 8 seconds. The raw export showed ₹23.01 Crore. We discovered two critical technical artifacts:*  
  *First, 638 tickets were duplicated during the Freshdesk migration cutover. Removing them eliminated ₹3.61 Crore.*  
  *Second, Freshdesk stored monetary values in paise, not rupees. Every legacy refund was an exact multiple of 100, and duplicate pairs in both systems differed by exactly 100x. Dividing by 100 removed ₹18.73 Crore.*  
  *The true audited total is exactly ₹67,09,932—or ₹11.2 Lakh a quarter, confirming the helpdesk's number."*

---

### [0:55 – 1:35] AI Prompts & What Changed Between Versions
* **On Screen:** Show code editor / prompt notes showing iterative development.
* **Say:**  
  *"We used AI assistance across three targeted prompts:*  
  *1. Prompt 1 asked to detect currency anomalies across source systems, which identified the 100x paise artifact.*  
  *2. Prompt 2 asked to audit `GW-OTHER`, which revealed that 88.7% of tickets tagged as goodwill exceeded the ₹500 policy cap, proving agents were using it as a dropdown default.*  
  *3. Prompt 3 generated our dual-detection NLP pattern for double payouts.*  
  
  *What changed between versions?*  
  *- In v1, we took reason codes at face value.*  
  *- In v2, we noticed the ₹500 goodwill cap breach and built a text classifier to re-read notes.*  
  *- In v3, our double-dip detector initially flagged 'replacement declined' as a violation; we introduced a strict negation filter to eliminate false positives.*  
  *- In v4, we added an automated assertion suite and an interactive executive dashboard."*

---

### [1:35 – 2:15] The Real Leak & The Business Goal
* **On Screen:** Switch to the Streamlit app (`streamlit run app.py`) -> `Double-Payout Leak Radar` tab.
* **Say:**  
  *"Here is the real financial leak: Policy §5 strictly forbids giving a customer both a refund and a replacement unit on the same order. Over the last four quarters, 230 tickets—12.3% of all refunds—issued both. 137 were flagged by agents, and another 93 were disclosed in agent closing notes.*  
  *This resulted in ₹4.19 Lakh in hardware and freight replacement costs plus ₹8.12 Lakh in unentitled cash refunds, totaling a ₹12.3 Lakh loss.*  
  *Our business goal for Arjun's board pack is concrete: Cut double payouts from 12.3% to under 2.0% within two quarters by implementing an API-level order check in the helpdesk UI, recovering ₹4.5 Lakh per quarter."*

---

### [2:15 – 2:40] What We Threw Away (And Why)
* **On Screen:** Switch to terminal and run `python validate.py --data .`. Show cross-validation output.
* **Say:**  
  *"To stay disciplined under the 5-hour scope, we intentionally threw away:*  
  *1. Agent league tables: Returns Desk and Billing structurally process the most refunds, so ranking agents by refund volume creates unfair bias.*  
  *2. LLM API calls: Our offline TF-IDF + Logistic Regression model delivers 91.3% cross-validated accuracy (and 95.7% at confidence ≥0.60) completely free with zero latency.*  
  *3. Lot code manufacturing defect analysis: The statistical signal in orders.csv was too sparse to prove batch defects."*

---

### [2:40 – 3:00] Validation & What I Trust Least
* **On Screen:** Highlight the confusion matrix in `validate.py` output.
* **Say:**  
  *"Every financial sheet ties out to the exact rupee. Our AI model reaches 95.7% accuracy on high-confidence classifications.*  
  *What number do I trust least? The split between Dead-on-Arrival (DOA-REPL) and Warranty Buyback (WTY-BUYBACK). Both share identical acoustic hardware defect vocabulary in agent notes, giving the model lower distinctiveness between those two classes. We quarantined low-confidence tickets into a 40-row human review sample for operational audit."*

---

## Part 2: Quick Reference for Recording

| Timestamp | Screen Target | Core Message |
| :--- | :--- | :--- |
| **0:00 - 0:25** | `email-thread.txt` | Arjun's ₹23 Cr vs Sameer's ₹11 Lakh discrepancy. |
| **0:25 - 0:55** | Terminal + Excel `Reconciliation` | 638 duplicates (-₹3.61 Cr) + paise correction (-₹18.73 Cr) = ₹67.10 Lakh clean. |
| **0:55 - 1:35** | Code / Prompt Log | 3 Prompts; Evolution from v1 (raw) to v4 (calibrated NLP + assertions). |
| **1:35 - 2:15** | Streamlit `Leak Radar` | 230 double-dip tickets (12.3%); ₹12.3 Lakh loss; Target: cut to <2.0%. |
| **2:15 - 2:40** | Terminal `validate.py` | Discarded agent blame ranking, external LLM costs, and lot defect mining. |
| **2:40 - 3:00** | Terminal Confusion Matrix | 95.7% accuracy; least trusted number is DOA vs Warranty Buyback separation. |
