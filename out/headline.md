================================================================================
VIREO AUDIO - SUPPORT REFUND FORENSIC AUDIT & EXECUTIVE SUMMARY
================================================================================
1. AUDITED REFUND TOTAL: Rs 6,709,932 across 2,340 unique tickets.
   - Helpdesk raw export showed: Rs 230,124,081 (~Rs 23.01 Crore).
   - Deduplication removed: 638 duplicate migrated tickets (Rs 36,101,100).
   - Currency correction removed: Legacy Freshdesk paise storage (Rs 187,313,049).
   - Quarterly average refunds: ~Rs 11.2 Lakh/quarter (matching the Helpdesk's internal report).

2. THE POLICY VIOLATION LEAK (Simultaneous Refund + Replacement on Same Ticket):
   - Over the last 4 full quarters (2025Q3 to 2026Q2):
     * Total refund tickets: 1,869
     * Double-payout violations: 230 tickets (12.3% of all refunds).
     * Confirmed by system flag (replacement_issued='Y'): 137 tickets.
     * Identified from agent closing notes: 93 tickets.
   - Financial Impact over 4 Quarters:
     * Replacement unit + logistics cost (unit cost + Rs 340): Rs 418,980 (~Rs 104,745/quarter).
     * Cash refund disbursed on same tickets: Rs 811,680 (~Rs 202,920/quarter).
     * Total combined leak: Rs 1,230,660 (~Rs 307,665/quarter).

3. THE DROPDOWN MASKING ANOMALY (GW-OTHER):
   - Frontline agents assigned 'GW-OTHER' to 991 tickets totaling Rs 2,907,036 (43.3% of all refund value).
   - Under Policy §5, goodwill is capped at Rs 500. Yet 879 tickets (88.7%) exceed this cap.
   - AI re-classification reveals these are genuine operational events (Cancellations, Return QC passed, Lost in transit) mistakenly tagged with the first dropdown option.
================================================================================
