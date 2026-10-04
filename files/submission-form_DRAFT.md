# submission-form.md - DRAFT (the pack's form was not in the files I was given: copy these answers into it)
**Business goal (a number):** Cut refund-plus-replacement tickets from 12.3% to <2% of refund tickets; about Rs 1.0 lakh/quarter (Rs 0.6 lakh if agent-flagged only).
**How to run:** see vireo_refunds/README.md (pip install -r requirements.txt; python refunds.py --data DIR --out out).
**How I know it works:** totals tie to the clean figure in code (assertions) and in the xlsx; paise/duplicate checks in validate.py; classifier 91% 5-fold CV (96% on confident 89%); selection-bias caveat; 40-row human sample prepared but NOT yet labelled.
**How often it is wrong:** reason re-read about 9% (up to more on hardware faults, DOA vs warranty buy-back are ~40-60%); double-payout flag: the agent flag and the notes agree on only 112 of 283 tickets, so there is real uncertainty - treat 137 as floor, 230 as ceiling.
**Decisions I made:** helpdesk copy beats legacy copy; /100 on legacy rows; +5h30 on migrated resolved_at; include open/pending refunds; report as-coded and re-read separately; agents = resolving agent_id.
**Left out and why:** LLM pass, ledger check, SLA/transfer/CSAT, lot defects, agent ranking - cap of 5 hours and no way to verify.
**AI tools used / cost / discarded:** [FILL IN: I used Claude to explore the data and write the code. Cost: your actual spend. Discarded: first reason-code regex, lot-code analysis, agent ranking.]
**Hours spent:** [FILL IN honestly]
