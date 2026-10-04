# 🎧 Vireo Audio — Financial Support Audit & AI Forensic Engine

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Streamlit App](https://img.shields.io/badge/Streamlit-Dashboard-red.svg)](https://streamlit.io/)
[![Scikit-Learn](https://img.shields.io/badge/ML-Scikit--Learn-orange.svg)](https://scikit-learn.org/)

An executive-grade forensic accounting, machine learning, and support operations audit suite for **Vireo Audio**. Reconciles complex multi-system helpdesk exports, exposes hidden P&L leakage, audits frontline dropdown misclassifications, and provides an interactive executive dashboard.

---

## 📌 Executive Summary

Arjun Mehta (Finance Controller) observed that raw helpdesk exports totaled **₹23,01,24,081 (~₹23.01 Crore)**, suggesting catastrophic refund leakage. 

Our forensic pipeline proved that **actual verified customer refunds over 18 months totaled ₹67,09,932 (~₹11.18 Lakh / quarter)**, perfectly confirming the helpdesk IT report (~₹11 Lakh/quarter). The ₹22.34 Crore discrepancy was caused by two technical artifacts:
1. **Freshdesk Migration Duplication:** 638 tickets were imported twice during system cutover, inflating the raw file by **₹3.61 Crore**.
2. **Paise-to-Rupee Currency Mismatch:** Legacy Freshdesk stored currency in **paise** (1 INR = 100 paise), inflating legacy rows by exactly **100x** (**₹18.73 Crore**).

### 🎯 Key Findings & Quantified Business Goal
* **The "GW-OTHER" Trap:** **43.3%** of all refund dollars (₹29.07 Lakh) were assigned to `GW-OTHER` because it is the **first item in the agent dropdown**. Policy §5 caps goodwill at ₹500, yet **88.7%** of these tickets exceeded ₹500. Our calibrated NLP model re-classified them into true operational categories (cancellations, failed delivery, QC-cleared returns).
* **The Real Cash Leak (Double Payouts):** Policy §5 strictly prohibits issuing both a refund and a replacement unit on the same order. Over the last 4 quarters, **230 tickets (12.3% of refunds)** received both, causing **₹12,30,660 in combined physical inventory, freight, and cash loss (~₹3.08 Lakh / quarter)**.
* **The CSAT Myth Debunked:** Average customer CSAT was virtually unchanged across all six quarters (**3.49 in Q3 vs 3.51 in Q4**). Refunds rose proportionally from ₹5.95 Lakh to ₹16.65 Lakh because **total inquiry volume surged 2.6x** (1,029 to 2,681 tickets), not because frontline agents became more lenient.
* **The Board Goal:** **Cut double-payout violations from 12.3% to below 2.0% within two quarters, recovering ₹10.0 to ₹12.0 Lakh annually (~₹2.5 to ₹3.0 Lakh / quarter).**

---

## ⚡ Quickstart (Clean Machine, < 10 Seconds)

Requires **Python 3.10+**. Self-contained, zero cloud API keys, 100% offline reproducible.

```bash
# 1. Clone the repository
git clone https://github.com/vireo-audio/support-audit.git
cd support-audit

# 2. Install dependencies
pip install -r requirements.txt

# 3. Execute the automated forensic reconciliation & AI pipeline
python refunds.py --data . --out out

# 4. Run the mathematical audit & statistical validation suite
python validate.py --data .

# 5. Launch the interactive executive dashboard
python -m streamlit run app.py
```

---

## 📊 Pipeline Architecture & Deliverables

```
vireo-support-audit/
├── refunds.py                 # Core forensic accounting & NLP classification engine
├── validate.py                # Mathematical validation & 5-fold CV statistical suite
├── app.py                     # Streamlit executive audit dashboard
├── memo_to_arjun.md           # 1-page executive memorandum for Arjun Mehta
├── submission-form.md         # Completed vendor evaluation submission form
├── video_script.md            # 3-minute timed screen recording guide & script
├── requirements.txt           # Minimal Python dependencies
└── out/                       # Generated audit artifacts
    ├── refund_summary.xlsx    # Executive multi-tab Board-ready Excel workbook
    ├── refund_clean.csv       # Clean audited ticket dataset
    ├── double_payouts_audit.csv # Audit log of all 283 double-dip violation tickets
    ├── headline.md            # Summary numbers for executive reporting
    └── review_sample.csv      # Stratified 40-ticket sample for human-in-the-loop review
```

---

## 🖥️ Interactive Executive Dashboard (`app.py`)

Launch the web cockpit via `streamlit run app.py` to explore:
* **Reconciliation Waterfall:** Step-by-step interactive journey from ₹23.01 Crore to ₹67.10 Lakh.
* **Volume & CSAT Reality:** Interactive charts debunking the "+0.4 CSAT" claim against ticket volume growth.
* **Dropdown Masking Radar:** Side-by-side distribution of frontline reason codes vs AI-audited operational causes.
* **Double-Payout Policy Violations:** Breakdown of the 230 leak tickets by assigned team, agent, and product family.
* **Live AI Classifier Sandbox:** Interactive test station to input custom customer messages and view real-time predictions and probability distributions.

---

## 🔬 Validation & Model Performance

Run `python validate.py --data .` to verify:

### 1. Deterministic Financial Invariants
* **100%** of legacy Freshdesk refunds are exact multiples of 100 paise.
* **125 duplicate refund pairs** present across both systems show an exact **100.00x** ratio.
* Every summary table (`By Reason As-Coded`, `By Reason AI Re-Read`, `By Agent`, and `Clean Data`) reconciles to **₹67,09,932.00** down to 0 paise via automated assertions.

### 2. Machine Learning Generalization (5-Fold Stratified CV)
* Evaluated on 1,349 ground-truth labeled tickets (non-GW-OTHER):
  * **Overall Accuracy:** **91.3%** (Macro F1: 0.833, Weighted F1: 0.909)
  * **High-Confidence Accuracy ($\ge 0.60$):** **95.7%** across **89.3%** sample coverage.
  * Near-perfect 99–100% precision on `CANCEL`, `DUP-PAYMENT`, and `PRICE-ADJ`.
  * Low-confidence predictions ($<0.60$) and goodwill exceeding the ₹500 cap are safely routed to a human `REVIEW` queue.

---

## 📋 Board Action Plan (Zero CapEx Levers)

1. **P0 System Guardrail (Helpdesk UI):** Programmatically block refund processing if an active RMA/replacement tracking number exists for the same order without Tier 2 Team Lead sign-off.
2. **P1 Intake Dropdown Fix:** Remove `GW-OTHER` from position #1 in the dropdown; force `-- Select Reason Code --` default and trigger an automated warning for Goodwill refunds > ₹500.
3. **P2 Open Ticket Review:** Confirm with Finance Treasury whether the ₹3.17 Lakh in 115 open/pending tickets has been disbursed.

---

## 📄 License
This project is licensed under the MIT License.
