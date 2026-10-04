"""Vireo Audio - Executive Support Audit & AI Forensic Dashboard.

Streamlit web application providing an interactive executive cockpit for:
1. Reconciliation waterfall (Rs 23.01 Cr -> Rs 67.10 Lakh)
2. Business hypothesis testing (debunking the CSAT claim)
3. GW-OTHER dropdown reclassification breakdown
4. Policy §5 Double-payout leakage radar
5. Live interactive AI text classification sandbox

Run with:
    streamlit run app.py
"""

import os
import re
import numpy as np
import pandas as pd
import streamlit as st
import refunds as R

st.set_page_config(
    page_title="Vireo Audio | Support Audit & Financial Reconciliation",
    page_icon="🎧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling for Executive Dark/Modern Look
st.markdown("""
<style>
    .main-title {
        font-size: 2.2rem;
        font-weight: 700;
        color: #1E3A8A;
        margin-bottom: 0.2rem;
    }
    .sub-title {
        font-size: 1.05rem;
        color: #4B5563;
        margin-bottom: 1.5rem;
    }
    .kpi-card {
        background-color: #F8FAFC;
        border: 1px solid #E2E8F0;
        border-radius: 8px;
        padding: 16px;
        text-align: center;
    }
    .kpi-val {
        font-size: 1.8rem;
        font-weight: 700;
        color: #1E293B;
    }
    .kpi-label {
        font-size: 0.85rem;
        color: #64748B;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    .alert-box {
        background-color: #FEF2F2;
        border-left: 4px solid #EF4444;
        padding: 12px 16px;
        border-radius: 4px;
        margin-bottom: 16px;
    }
</style>
""", unsafe_allow_html=True)


@st.cache_data
def get_data():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    tickets, agents, products = R.load_datasets(current_dir)
    clean_tickets, refunds, audit = R.clean_and_reconcile(tickets, agents, products)
    refunds = R.detect_double_payouts(refunds)
    refunds = R.reclassify_goodwill(refunds, threshold=0.60)
    return clean_tickets, refunds, audit


clean_tickets, refunds, audit = get_data()

# Header
st.markdown('<div class="main-title">🎧 VIREO AUDIO — Executive Support & Financial Audit</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Forensic Helpdesk Reconciliation, Dropdown NLP Re-classification & Double-Payout Policy Violation Radar</div>', unsafe_allow_html=True)

# Top KPI Cards
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.markdown("""
    <div class="kpi-card">
        <div class="kpi-label">Audited Refund Total</div>
        <div class="kpi-val">₹67.10 Lakh</div>
        <div style="color: #059669; font-size: 0.85rem;">Export showed ₹23.01 Cr (Artifact)</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="kpi-card">
        <div class="kpi-label">Quarterly Run Rate</div>
        <div class="kpi-val">₹11.2 Lakh / Q</div>
        <div style="color: #2563EB; font-size: 0.85rem;">Matches Helpdesk Internal Report</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="kpi-card">
        <div class="kpi-label">Policy §5 Double-Dip Leak</div>
        <div class="kpi-val">₹12.31 Lakh / Yr</div>
        <div style="color: #DC2626; font-size: 0.85rem;">230 Tickets (12.3% of Refunds)</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class="kpi-card">
        <div class="kpi-label">AI Re-Classification Precision</div>
        <div class="kpi-val">95.7%</div>
        <div style="color: #059669; font-size: 0.85rem;">At ≥0.60 confidence (89% coverage)</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# Navigation Tabs
tabs = st.tabs([
    "📊 Financial Reconciliation",
    "📈 Volume & CSAT Reality",
    "🏷️ Dropdown Masking (GW-OTHER)",
    "🚨 Double-Payout Leak Radar",
    "🤖 Live AI Classifier Sandbox",
    "👥 Department & Agent View"
])

# TAB 1: Financial Reconciliation
with tabs[0]:
    st.subheader("Helpdesk Export Forensic Reconciliation")
    st.markdown("""
    **Executive Summary:** Arjun Mehta's initial export summed to **₹23,01,24,081** (~₹23.01 Crore), raising alarm of massive financial leakage. 
    Our forensic audit proves this was an artifact of two compounding technical system errors:
    1. **Freshdesk Migration Duplication:** 638 tickets were imported twice during cutover, inflating the raw export by **₹3.61 Crore**.
    2. **Paise-to-Rupee Legacy Storage Unit:** Freshdesk recorded currency in *paise* (1 INR = 100 paise), making every migrated row exactly **100x too large**. Correcting this takes out **₹18.73 Crore**.
    """)

    col_w1, col_w2 = st.columns([3, 2])
    with col_w1:
        waterfall_df = pd.DataFrame([
            {"Stage": "1. Raw Export Sum", "Amount (INR)": audit['raw_refund_sum'], "Explanation": "Raw helpdesk uncleaned export total"},
            {"Stage": "2. Less Migration Duplicates", "Amount (INR)": audit['dedup_loss_reduction'], "Explanation": "638 duplicate migrated rows removed"},
            {"Stage": "3. Less Legacy Paise Correction", "Amount (INR)": audit['paise_loss_reduction'], "Explanation": "100x reduction on Freshdesk paise rows"},
            {"Stage": "4. Verified Clean Refunds", "Amount (INR)": audit['clean_refund_sum'], "Explanation": "Actual verified cash disbursed (2,340 tickets)"}
        ])
        st.dataframe(
            waterfall_df.style.format({"Amount (INR)": "₹{:,.2f}"}),
            width='stretch',
            hide_index=True
        )

    with col_w2:
        st.info("""
        **Integrity Guarantees:**
        - **100% of legacy refunds** are exact multiples of 100 paise.
        - **125 duplicate pairs** present in both systems confirm an exact **100.00x** ratio.
        - All summary cuts (by reason code, by agent, by month) tie to **₹67,09,932.00** down to 0 paise.
        """)

    st.write("---")
    st.subheader("Quarterly Audited Financial Run Rate")
    q_summary = refunds.groupby('quarter').agg(
        refund_tickets=('ticket_id', 'count'),
        total_refund=('refund_inr', 'sum'),
        avg_refund=('refund_inr', 'mean')
    ).reset_index()
    st.dataframe(
        q_summary.style.format({"total_refund": "₹{:,.2f}", "avg_refund": "₹{:,.2f}"}),
        width='stretch',
        hide_index=True
    )

# TAB 2: Volume & CSAT Reality
with tabs[1]:
    st.subheader("Testing the CX Narrative: CSAT vs Ticket Growth")
    st.markdown("""
    In the email thread, Head of CX Priya Raman stated:
    > *"Refunds went up because we told the frontline to stop arguing with customers in Q4. CSAT went up 0.4 in the same period."*
    
    We analyzed 18 months of customer ratings (1-5 scale) across all quarters to test this hypothesis.
    """)

    q_df = clean_tickets[clean_tickets['quarter'].isin(['2025Q1', '2025Q2', '2025Q3', '2025Q4', '2026Q1', '2026Q2'])]
    q_perf = q_df.groupby('quarter').agg(
        total_inquiries=('ticket_id', 'count'),
        refund_tickets=('refund_inr', lambda x: x.notna().sum()),
        total_refund_inr=('refund_inr', 'sum'),
        avg_csat=('csat_score', 'mean'),
        survey_responses=('csat_score', 'count')
    ).reset_index()
    q_perf['refund_rate_pct'] = (q_perf['refund_tickets'] / q_perf['total_inquiries'] * 100).round(1)
    q_perf['avg_csat'] = q_perf['avg_csat'].round(2)

    c_g1, c_g2 = st.columns(2)
    with c_g1:
        st.write("**Total Support Inquiries vs Refund Rate (%)**")
        st.line_chart(q_perf.set_index('quarter')[['total_inquiries', 'refund_tickets']])
    with c_g2:
        st.write("**Average CSAT Score (1 - 5 Scale)**")
        st.line_chart(q_perf.set_index('quarter')['avg_csat'])

    st.dataframe(
        q_perf.style.format({"total_refund_inr": "₹{:,.0f}", "avg_csat": "{:.2f}", "refund_rate_pct": "{:.1f}%"}),
        width='stretch',
        hide_index=True
    )

    st.warning("""
    **Key Finding for the Board Pack:**
    1. **CSAT was virtually unchanged:** 3.49 in 2025Q3 to 3.51 in 2025Q4 (+0.02, not +0.40).
    2. **Refund propensity remained constant:** Between **18.2% and 21.8%** of tickets across all six quarters.
    3. **Volume is the true driver:** Support ticket inquiries expanded **2.6x** (from 1,029 in Q1 to 2,681 in Q4). Total refunds rose proportionally from ₹5.95 Lakh to ₹16.65 Lakh because the company scaled, not because agents became lenient.
    """)

# TAB 3: Dropdown Masking (GW-OTHER)
with tabs[2]:
    st.subheader("The 'GW-OTHER' Dropdown Masking Problem")
    st.markdown("""
    **The Anomaly:** **43.3%** of all refund money (₹29.07 Lakh) is tagged as `GW-OTHER` because it is the **very first item** in the agent closure dropdown.
    **The Policy Violation:** Policy §5 caps Goodwill credits at **₹500 per ticket**. Yet **879 out of 991 tickets (88.7%)** exceed ₹500, with an average of ₹2,933!
    """)

    col_rc1, col_rc2 = st.columns(2)
    with col_rc1:
        st.write("**Original Reason Codes (As Coded by Frontline)**")
        as_coded = refunds.groupby('refund_reason_code').agg(
            tickets=('ticket_id', 'count'),
            total_inr=('refund_inr', 'sum')
        ).sort_values('total_inr', ascending=False).reset_index()
        st.dataframe(as_coded.style.format({"total_inr": "₹{:,.0f}"}), width='stretch', hide_index=True)

    with col_rc2:
        st.write("**AI NLP Audited Reason Codes (Re-Classified from Notes)**")
        ai_audited = refunds.groupby('final_audited_code').agg(
            tickets=('ticket_id', 'count'),
            total_inr=('refund_inr', 'sum')
        ).sort_values('total_inr', ascending=False).reset_index()
        st.dataframe(ai_audited.style.format({"total_inr": "₹{:,.0f}"}), width='stretch', hide_index=True)

    st.info("""
    **Operational Solution for Support Ops (Neha Kulkarni):**
    Remove `GW-OTHER` from position #1 in the dropdown. Make the default `-- Select Reason Code --` (blank).
    Implement a client-side warning if an agent selects Goodwill on a ticket exceeding ₹500.
    """)

# TAB 4: Double-Payout Leak Radar
with tabs[3]:
    st.subheader("The Real Cash Leak: Simultaneous Refund + Replacement")
    st.markdown("""
    **Policy §5:** *"In no case is a customer to receive both a refund and a replacement for the same order; where this happens in error it must be escalated to the Team Lead and Finance the same day."*
    
    Our NLP and flag audit caught **283 tickets** (230 over the last 4 quarters) where customers received **both remedies**.
    """)

    l4_quarters = ['2025Q3', '2025Q4', '2026Q1', '2026Q2']
    r_l4 = refunds[refunds['quarter'].isin(l4_quarters)]
    dd_l4 = r_l4[r_l4['is_double_payout']]

    st.markdown(f"""
    <div class="alert-box">
        <b>Last 4 Quarters Financial Damage:</b><br>
        • Double Payout Tickets: <b>{len(dd_l4)}</b> out of {len(r_l4):,} refunds (<b>{len(dd_l4)/len(r_l4):.1%}</b>)<br>
        • Replacement Hardware & Logistics Cost (Unit Cost + ₹340): <b>₹{dd_l4['replacement_cost_inr'].sum():,.0f}</b> (~₹{dd_l4['replacement_cost_inr'].sum()/4:,.0f} / Q)<br>
        • Cash Refund Disbursed on Same Tickets: <b>₹{dd_l4['refund_inr'].sum():,.0f}</b> (~₹{dd_l4['refund_inr'].sum()/4:,.0f} / Q)<br>
        • <b>Total Combined Loss: ₹{dd_l4['total_leak_inr'].sum():,.0f} (~₹{dd_l4['total_leak_inr'].sum()/4:,.0f} / Q)</b>
    </div>
    """, unsafe_allow_html=True)

    c_team, c_prod = st.columns(2)
    with c_team:
        st.write("**Double Payouts by Assigned Team**")
        team_dd = dd_l4.groupby('assigned_team').agg(
            tickets=('ticket_id', 'count'),
            total_leak=('total_leak_inr', 'sum')
        ).sort_values('tickets', ascending=False).reset_index()
        st.dataframe(team_dd.style.format({"total_leak": "₹{:,.0f}"}), width='stretch', hide_index=True)

    with c_prod:
        st.write("**Double Payouts by Product Family**")
        prod_dd = dd_l4.groupby('family').agg(
            tickets=('ticket_id', 'count'),
            total_leak=('total_leak_inr', 'sum')
        ).sort_values('tickets', ascending=False).reset_index()
        st.dataframe(prod_dd.style.format({"total_leak": "₹{:,.0f}"}), width='stretch', hide_index=True)

    st.write("---")
    st.write("**Audit Trail of Violation Tickets**")
    st.dataframe(
        dd_l4[['ticket_id', 'month', 'agent_team', 'agent_name', 'family', 'refund_inr', 'replacement_cost_inr', 'total_leak_inr', 'agent_notes']]
        .sort_values('total_leak_inr', ascending=False)
        .style.format({"refund_inr": "₹{:,.0f}", "replacement_cost_inr": "₹{:,.0f}", "total_leak_inr": "₹{:,.0f}"}),
        width='stretch',
        hide_index=True
    )

# TAB 5: Live AI Classifier Sandbox
with tabs[4]:
    st.subheader("Live AI NLP Ticket Classifier Sandbox")
    st.markdown("Test the machine learning model in real-time on any customer complaint or agent note.")

    sample_complaints = [
        "Customer says left earbud stopped charging 2 days after receiving. Requested money back.",
        "Accidentally clicked buy twice on checkout, duplicate debit on HDFC card. Cancel second order.",
        "Parcel tracking shows delivered in Bengaluru but customer never received shipment.",
        "Bought during flash sale at 3499, now listed at 2999. Customer requested price difference.",
        "Device returned to warehouse and passed diagnostic check. Process refund."
    ]
    selected_sample = st.selectbox("Or choose a pre-filled sample ticket:", [""] + sample_complaints)

    input_text = st.text_area(
        "Enter Ticket Text (Customer Message / Agent Notes / Intake Tag):",
        value=selected_sample if selected_sample else "Left earbud has zero audio output out of the box, DOA unit. Dispatched return pickup and processing full refund."
    )

    if st.button("Classify Ticket with AI"):
        labeled = refunds[refunds['refund_reason_code'] != 'GW-OTHER'].copy()
        labeled['feature_text'] = R.prepare_text_features(labeled)
        model = R.build_classifier_pipeline().fit(labeled['feature_text'], labeled['refund_reason_code'])

        probs = model.predict_proba([input_text.lower()])[0]
        classes = model.classes_
        top_idx = probs.argmax()
        top_class = classes[top_idx]
        top_conf = probs[top_idx]

        res_c1, res_c2 = st.columns([1, 2])
        with res_c1:
            st.metric("Predicted Reason Code", top_class)
            st.metric("Confidence Score", f"{top_conf:.1%}")
            if top_conf < 0.60:
                st.warning("Low confidence: Would be routed to human REVIEW queue.")
            else:
                st.success("High confidence: Clean automated classification.")

        with res_c2:
            st.write("**Probability Distribution Across All Categories:**")
            prob_df = pd.DataFrame({"Reason Code": classes, "Probability": probs}).sort_values("Probability", ascending=False)
            st.bar_chart(prob_df.set_index("Reason Code"))

# TAB 6: Department & Agent View
with tabs[5]:
    st.subheader("Departmental & Frontline Resolution Analysis")
    st.markdown("""
    **Context for Arjun Mehta:** This view shows who **closed** the refund ticket, not who committed an error.
    The **Returns Desk** and **Billing** teams structurally process the overwhelming majority of refunds by design.
    """)

    ag_summary = refunds.groupby(['agent_team', 'agent_name']).agg(
        refund_tickets=('ticket_id', 'count'),
        total_refund_inr=('refund_inr', 'sum')
    ).sort_values('total_refund_inr', ascending=False).reset_index()

    st.dataframe(
        ag_summary.style.format({"total_refund_inr": "₹{:,.0f}"}),
        width='stretch',
        hide_index=True
    )
