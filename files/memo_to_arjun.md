# EXECUTIVE MEMORANDUM

**TO:** Arjun Mehta, Finance Controller, Vireo Audio  
**CC:** Priya Raman (Head of CX), Neha Kulkarni (Support Operations Manager), Sameer Qureshi (Helpdesk Administrator / IT)  
**DATE:** 20 September 2026  
**SUBJECT:** Forensic Audit of Support Refunds: Root Cause of the ₹23 Crore Discrepancy, The "GW-OTHER" Trap, and a ₹12.3 Lakh P&L Leakage Fix  

---

### 1. Executive Summary: The Real Number
Your raw helpdesk export totaled **₹23,01,24,081 (~₹23.01 Crore)**, causing justified alarm. 

**Actual verified customer refunds over the 18 months are ₹67,09,932 (averaging ₹11.18 Lakh per quarter).** The helpdesk’s internal reporting figure of ~₹11 Lakh/quarter is correct. No ₹23 Crore left the business. 

The ₹22.34 Crore discrepancy is completely explained by two technical system errors during the Freshdesk-to-current-helpdesk cutover:
1. **Migration Re-Import Duplication (Takes out ₹3.61 Crore):** 638 tickets appeared twice in your export because a reconciliation script re-imported them into both systems. We deduplicated these, preserving the native helpdesk record.
2. **Legacy Currency Unit Mismatch (Takes out ₹18.73 Crore):** Freshdesk recorded monetary fields in **paise**, not rupees (1 INR = 100 paise). Every single legacy refund is an exact multiple of 100, and tickets present in both systems differ by exactly a factor of 100.00x. Dividing legacy rows by 100 completely reconciles the figure.
3. **Timezone Normalization:** Migrated resolution logs were stored in UTC rather than IST (+5h 30m). Aligning this moved 9 month-end tickets into their proper reporting month without affecting annual totals.

The attached workbook (`refund_summary.xlsx`) ties out across every sheet—by reason code, by agent, and by month—to the exact verified figure of **₹67,09,932**. You can drop these tables directly into your Board pack for the 24th.

---

### 2. Why Did Refunds Go Up? (Testing the CX Narrative)
Refund cash grew from **₹5.96 Lakh in 2025 Q1** to **₹16.66 Lakh in 2025 Q4**. 

Priya suggested this increase was driven by frontline agents being instructed to "stop arguing with customers in Q4," yielding a "+0.4 boost in CSAT." The data disproves this narrative:
* **The Refund Propensity Did Not Change:** In every single quarter from 2025 Q1 through 2026 Q2, refunds remained virtually constant at **18.2% to 21.8% of total tickets** (average 20.1%). Agents did not become more lenient.
* **CSAT Did Not Increase:** Average CSAT was **3.54 in Q1, 3.51 in Q2, 3.49 in Q3, and 3.51 in Q4**. The claimed "+0.4 jump" does not exist in customer responses.
* **Volume Scaled 2.6x:** Vireo’s total quarterly support inquiries expanded from 1,029 in Q1 to 2,681 in Q4. Refunds rose purely because the brand grew, not because customer concessions were loosened.

---

### 3. Three Critical Warnings on the Raw Helpdesk Data
Before presenting these figures to the Board, note three operational realities:
1. **The "GW-OTHER" Dropdown Illusion (₹29.07 Lakh):**  
   43.3% of all refund dollars are tagged as `GW-OTHER`. Policy §5 states Goodwill is capped at **₹500** and requires Team Lead approval. However, **879 out of 991 GW-OTHER tickets (88.7%) exceed ₹500** (averaging ₹2,933). Frontline agents simply select the first item in the dropdown when closing tickets. Our AI re-classification model (verified at 95.7% precision) reveals these are almost entirely legitimate cancellations, warehouse-passed returns, duplicate payment reversals, and parcels lost in transit.
2. **The Agent Table is Structural, Not a Measure of Fault:**  
   The `By Agent` tab lists resolving agents. The Returns Desk and Billing teams process the highest refund volumes by policy design. This table reflects operational routing, not individual agent indiscipline.
3. **Open/Pending Tickets (₹3.17 Lakh):**  
   We included 115 tickets where a refund amount was booked but the ticket remains open or pending. Please confirm with Finance Treasury whether payout files have already been dispatched for these.

---

### 4. The One Real P&L Leak: Double Payouts (Refund + Replacement)
Policy §5 explicitly mandates:  
> *"In no case is a customer to receive both a refund and a replacement for the same order; where this happens in error it must be escalated to the Team Lead and Finance the same day."*

**Our audit detected 230 tickets in the last four quarters (12.3% of all refund tickets) where customers received BOTH a cash refund AND a replacement unit.**
* **137 tickets** were explicitly flagged with `replacement_issued = 'Y'`.
* **93 tickets** were marked `replacement_issued = 'N'`, but agent notes confirm dual fulfillment (*e.g., "dispatched fresh pair and issued full refund"*).
* **Concentration:** 72% of these double payouts originate in **Chat Frontline (90 tickets)** and **Logistics (77 tickets)** on earbud products, where agents attempt rapid resolution across fragmented queues.

**The Financial Damage Over 4 Quarters:**
* **₹4,18,980** in replacement unit costs and reverse/forward logistics (Policy §5 cost standard: Unit Cost + ₹340).
* **₹8,11,680** in cash refunds disbursed on those exact same orders.
* **Total Combined Loss: ₹12,30,660 (~₹3,07,665 per quarter).**

---

### 5. Actionable Business Goal: The Board Proposal
> **Business Target:** Reduce the simultaneous refund-and-replacement violation rate from **12.3% to under 2.0%** within two quarters, recovering **₹10.0 to ₹12.0 Lakh annually (~₹2.5 to ₹3.0 Lakh per quarter)** in combined inventory, freight, and cash leakage.

**Immediate Implementation Roadmap (Zero CapEx):**
1. **System Guardrail (IT / Sameer Qureshi):** Implement a database validation rule in the Helpdesk UI that prevents an agent from initiating a refund transaction if an RMA replacement order already exists for that `order_id` without an override from a Tier 2 Team Lead.
2. **Dropdown Fix (Support Ops / Neha Kulkarni):** Remove `GW-OTHER` from position #1 in the intake dropdown. Force an unselected default (`-- Select Reason Code --`) and introduce an automated prompt when a refund exceeding ₹500 is entered under Goodwill.
3. **Double Payout Review (Finance / Arjun Mehta):** Review the 230 violation tickets listed on the `Double Payout Audit` sheet with Team Leads to claw back open RMA shipments and adjust accounting provisions.

---

### 6. Sign-Off Needed from You
1. Sign off on the **₹67,09,932** reconciled total for insertion into the Board pack.
2. Confirm with Finance Treasury whether the ₹3.17 Lakh in open/pending tickets has been disbursed.
3. Authorize Sameer to implement the Helpdesk UI order-level refund locking rule.

*All supporting files, automated reconciliation scripts, and the interactive audit dashboard have been packaged and verified for immediate deployment.*
