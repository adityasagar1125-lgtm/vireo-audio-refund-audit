# VIREO AUDIO — SUBMISSION FORM
**Candidate Task Submission: Support Data Pack (Set C)**  
**Target:** Arjun Mehta, Finance Controller, Vireo Audio  
**System:** Python 3.10+ / Scikit-Learn / OpenPyXL / Streamlit  

---

### 1. Business Goal (A Number)
> **"Reduce the simultaneous refund-and-replacement ('double payout') rate from 12.3% to below 2.0% of refund tickets within two quarters (by Q4 FY27), recovering ₹12.31 Lakh annually (~₹3.08 Lakh per quarter) in combined physical inventory, freight, and cash leakage."**

* **Breakdown of Leakage (Last 4 Full Quarters: 2025 Q3 – 2026 Q2):**
  * Total refund tickets: 1,869
  * Simultaneous refund + replacement violations: **230 tickets (12.3%)**
  * Hardware replacement & freight cost incurred (Unit Cost + ₹340 logistics): **₹4,18,980** (~₹1,04,745 / quarter)
  * Cash refunds disbursed on the same tickets: **₹8,11,680** (~₹2,02,920 / quarter)
  * **Total Financial Leak: ₹12,30,660** (~₹3,07,665 / quarter)
* **Implementation Mechanism:** Deploy an API-level database constraint in the Helpdesk UI that programmatically blocks processing a cash refund if an active RMA/replacement tracking number exists for the same `order_id`, requiring Tier 2 Team Lead authorization for policy exceptions.

---

### 2. How to Run
Starts cleanly on any machine with Python 3.10+:

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the financial reconciliation & AI classification pipeline
python refunds.py --data . --out out

# 3. Run the mathematical audit & statistical cross-validation suite
python validate.py --data .

# 4. (Optional) Launch the interactive executive dashboard
python -m streamlit run app.py
```

* **Execution Speed:** Complete data cleaning, NLP training, audit generation, and Excel compilation finishes in under **8 seconds**.
* **Zero External API Keys:** Self-contained, offline reproducible pipeline requiring no cloud credits or internet connection.
* **Outputs Generated in `out/`:**
  * `refund_summary.xlsx`: Executive Board-ready workbook with live formulas, freeze panes, reconciliation tab, reason code tabs, agent tab, and leak audit tab.
  * `refund_clean.csv`: Clean audited dataset with normalized IST timestamps and corrected currency units.
  * `double_payouts_audit.csv`: Detailed audit of all 283 violation tickets with customer notes.
  * `headline.md`: Key metrics and findings for executive memos.
  * `review_sample.csv`: 40-row stratified random sample for human-in-the-loop scoring.

---

### 3. How I Know It Works
1. **Deterministic Accounting Reconciliations (Exact Rupee Proof):**
   * **100% of legacy Freshdesk refunds** are exact multiples of 100 paise (native helpdesk is 5.5%).
   * **125 duplicate refund pairs** present across both systems show an exact **100.00x ratio** (`legacy_paise / helpdesk_inr == 100.0`).
   * **Mathematical Equality Invariant:** Every summary cut (`By Reason As-Coded`, `By Reason AI Re-Read`, `By Agent`, and `Data`) reconciles to **₹67,09,932.00** down to 0 paise via automated assertions.
2. **Statistical Machine Learning Validation:**
   * Evaluated via **5-Fold Stratified Cross-Validation** on 1,349 ground-truth labeled tickets (non-GW-OTHER).
   * Achieves **91.3% overall cross-validated accuracy** (Macro F1: 0.833, Weighted F1: 0.909).
   * High-confidence predictions ($\ge 0.60$ threshold) achieve **95.7% accuracy** across **89.3% sample coverage**.
3. **Cross-Tabulation Sensitivity:**
   * Cross-verified the `replacement_issued == 'Y'` flag against agent closing notes NLP regex (`BOTH_PAT` and `NEG_PAT`), proving that while 137 are caught by system flags alone, an additional 93 tickets (40% more) are revealed through notes text analysis.

---

### 4. How Often It Is Wrong
1. **AI Reason Code Re-Classification:**
   * **Overall Error Rate:** ~8.7% across all classes on cross-validation; drops to **4.3%** on confident predictions ($\ge 0.60$).
   * **Weakest Discrimination:** `DOA-REPL` (Dead on Arrival) vs `WTY-BUYBACK` (Warranty Buyback). F1-score drops to 0.662 for DOA and 0.381 for Warranty Buyback because both ticket types describe identical physical failure symptoms (*e.g., "left bud dead", "battery drains in 10 mins"*).
   * **Selection Bias Caveat:** Frontline agents who defaulted to `GW-OTHER` may differ systematically from agents who selected specific codes. To mitigate false certainty, all predictions with confidence $<0.60$ or exceeding the ₹500 goodwill cap are quarantined into a human `REVIEW` queue.
2. **Double-Payout Leak Identification:**
   * Conservative lower bound (agent flag only): **137 tickets** (₹6.5 Lakh loss).
   * Comprehensive upper bound (agent flag + notes NLP): **230 tickets** (₹12.3 Lakh loss).
   * The 93 notes-only tickets require operational team lead confirmation to ensure the noted replacement was actually shipped rather than merely discussed.

---

### 5. Decisions I Made
1. **Deduplication Priority:** Kept the `helpdesk` record over `legacy_fd` for the 638 duplicate migrated tickets because the modern helpdesk stores native rupees and accurate team routing metadata.
2. **Paise-to-Rupee Transformation:** Divided all legacy Freshdesk refund amounts by 100 based on empirical proof that 100% of legacy amounts are multiples of 100 and migrated pairs differ by 100.00x.
3. **Timezone Offset (+5h 30m):** Shifted migrated ticket resolution timestamps from UTC to IST before assigning calendar months, ensuring month-end tickets align with Vireo's fiscal reporting.
4. **Open/Pending Refund Treatment:** Retained 115 unresolved refund tickets totaling ₹3,17,314 and dated them by ticket creation timestamp, highlighting them explicitly for Treasury confirmation.
5. **Separation of Accounting Books vs AI Estimates:** Never overwrite the legal as-coded ledger in financial tables. We provide the as-coded summary as the primary accounting sheet and present the AI re-classification as a separate analytical audit.
6. **Agent Attribution:** Assigned refunds to the resolving `agent_id` rather than assigned team, while explicitly noting in the memo that Returns Desk and Billing handle the highest volumes by structural role rather than poor performance.

---

### 6. Left Out and Why (Scope Management)
1. **External LLM API Integrations:** Discarded cloud LLM dependencies (OpenAI/Claude API) in favor of an offline, zero-cost, reproducible TF-IDF + Logistic Regression pipeline that runs in 8 seconds on any machine.
2. **Agent Disciplinary League Tables:** Discarded ranking agents by refund dollars. Tier 2 and Returns Desk agents naturally process refunds as their core job description; penalizing them creates toxic incentives.
3. **Manufacturing Lot Code Defect Mining:** Discarded deep correlation of `lot_code` against refund rate. Ticket volume across lot codes was too sparse to provide statistically rigorous defect attribution.
4. **General Ledger Audit:** Freshdesk-era bank statements and general ledger entries were not provided in the pack, so legacy reconciliation relies strictly on export data.

---

### 7. AI Tools Used / Cost / Discarded
* **AI Coding Assistants Used:** Google Antigravity / Claude 3.5 Sonnet for exploratory data analysis, hypothesis testing, and pipeline construction.
* **Financial Cost Incurred:** ₹0 (utilized built-in development tooling and local execution).
* **Discarded AI Artifacts:**
  * Discarded an initial naive regex for double payouts that lacked negation filtering (falsely caught *"customer declined replacement"*).
  * Discarded a multi-layer neural network classifier that offered no performance advantage over calibrated logistic regression while introducing unnecessary computational overhead and opacity.

---

### 8. Total Hours Spent
* **Total Time Invested:** **4 hours 15 minutes** (within the strict 5.0-hour cap).
  * Data exploration & legacy anomaly forensics: 1 hr 15 min
  * Pipeline engineering & deterministic reconciliation: 1 hr 00 min
  * ML classifier training, calibration & validation: 45 min
  * Executive dashboard & Excel workbook generation: 45 min
  * Executive memo, recording script & documentation: 30 min
