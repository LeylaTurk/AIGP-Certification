#!/usr/bin/env python3
"""Build plan/study-plan.json and plan/aigp-study-plan.md from one data definition,
then validate them against research/resources.json.

Run from the repo root:  python3 plan/build_study_plan.py
"""
import datetime as dt
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RES = json.loads((ROOT / "research" / "resources.json").read_text())

# --- URL allow-lists --------------------------------------------------------
VERIFIED = {r["id"]: r["url"] for r in RES["resources"] if r.get("verified") is True}
UNVERIFIED_URLS = {r["url"] for r in RES["resources"] if r.get("verified") is not True}
# practiceExams entries carry no per-entry `verified` flag. Only the recommended /
# optional ones are allowed, and the validator reports them separately.
PE = {p["id"]: p["url"] for p in RES["practiceExams"] if p["verdict"] in ("Recommend", "Optional")}


def url_for(rid):
    if not rid:
        return ""
    if rid in VERIFIED:
        return VERIFIED[rid]
    if rid in PE:
        return PE[rid]
    raise KeyError(f"resource id {rid!r} not in verified resources or allowed practiceExams")


START = dt.date(2026, 9, 23)
EXAM = dt.date(2026, 10, 27)
BOOK_BY = dt.date(2026, 10, 12)
GO_NO_GO = dt.date(2026, 10, 25)
FALLBACK = dt.date(2026, 11, 10)


def T(title, rid, typ, mins, dom, opt=False, ms=None, sub=None):
    return dict(title=title, rid=rid, type=typ, minutes=mins, domain=dom,
                optional=opt, milestone=ms, sub=sub or dom)


def O(*a, **k):
    k["opt"] = True
    return T(*a, **k)


REST = "REST"  # marker for a rest day

# Each week: theme, domains, list of 7 day entries (Wed..Tue). The final week ends on exam day.
# Pattern: most study on weekdays (Wed, Thu, Fri, Mon, Tue ~1.5-2 h each), Saturday is the one
# longer weekend session (the full mocks), Sunday is the rest day.
WEEKS = [
    dict(theme="Blueprint, diagnostic, Domain I (governance programme) and EU AI Act orientation",
         dom=["I", "II"], days=[
        [  # Wed 23 Sep
            T("Read the AIGP BoK v2.1 PDF: all four domains' competencies and performance indicators; tag each line Strong / Partial / Weak against your BlueDot background", "iapp-bok-v2-1", "read", 50, "All"),
            T("Request the free IAPP AIGP study guide (form); check it shows the 4-domain structure before using it", "iapp-aigp-fsg-request", "read", 10, "All"),
            T("Read the IAPP Candidate Handbook PDF: scheduling, rescheduling/cancellation cut-offs, ID rules, OnVUE requirements. Note the reschedule cut-off: it sets your real go/no-go date", "iapp-handbook-pdf", "read", 25, "All"),
            T("Read EU AI Act Article 4 (AI literacy duty)", "aia-art-4", "read", 10, "I"),
            O("Watch 'AIGP v2.1 Full Course Update Explained' (what changed in v2.1)", "yt-v21-update", "watch", 45, "All"),
        ],
        [  # Thu 24 Sep
            T("Diagnostic part 1: IAPP free study guide sample questions, untimed", "iapp-aigp-fsg-request", "practice", 35, "All", ms="Diagnostic"),
            T("Diagnostic part 2: AIGP Playbook 15-question free mock preview, untimed", "pe-aigpplaybook", "practice", 25, "All"),
            T("Start a gap log: tag every diagnostic miss by BoK competency and rank the four domains weakest to strongest", "", "review", 20, "All"),
            T("Read Commission Guidelines on the AI-system definition: the 7 definitional elements only (fast)", "ec-guidelines-ai-definition", "read", 20, "I", sub="I.A"),
            T("Skim OECD AI Principles: 5 values-based principles + 5 recommendations (fast, BlueDot-covered)", "oecd-ai-principles", "read", 15, "II", sub="II.D"),
            O("Read Veronica Lin's 'How I passed the AIGP exam' (what worked, what didn't)", "rep-veronica-lin", "read", 15, "All"),
        ],
        [  # Fri 25 Sep
            T("Read AIGP Playbook Domain I notes: skim I.A; study I.B (roles, committees, cross-functional collaboration, AI literacy) and I.C (policies across the lifecycle)", "aigpplaybook-d1", "read", 75, "I"),
            T("Make Anki flashcards: Domain I roles, governance committee/RACI, policy types, AI inventory", "", "flashcards", 30, "I"),
            O("Listen: AIGP Audio Course Ep. 1, decoding the exam blueprint", "pod-baremetal-ep1", "watch", 25, "All"),
        ],
        [  # Sat 26 Sep
            T("Read NIST AI RMF Playbook GOVERN 1-6 (policies, accountability, workforce, culture, stakeholder engagement, third-party risk)", "nist-playbook-govern", "read", 60, "I"),
            T("Listen: AIGP Audio Course Ep. 11, updating privacy, security, data-governance and IP policies for AI (I.C.2)", "pod-baremetal-ep11-spotify", "watch", 30, "I"),
            O("Read IAPP AI Governance Profession Report 2025: where governance sits, team structures", "iapp-profession-report-2025", "read", 45, "I"),
        ],
        REST,  # Sun 27 Sep
        [  # Mon 28 Sep
            T("Read IAPP AI Governance in Practice Report 2024: programme set-up sections (governance structures, inventories, risk assessment)", "iapp-in-practice-2024", "read", 55, "I"),
            T("Read the IAPP Key Terms for AI Governance glossary end to end; flag unfamiliar terms", "iapp-glossary", "read", 45, "I", sub="I.A"),
            O("Skim NIST AI 600-1 GenAI Profile Section 2 (the 12 GAI risks); BlueDot-covered, just map names", "nist-600-1", "read", 30, "I", sub="I.A"),
        ],
        [  # Tue 29 Sep
            T("Read the EU AI Act high-level summary (whole page): risk tiers, provider vs deployer duties, GPAI", "aia-high-level-summary", "read", 45, "II", sub="II.C"),
            T("Read EU AI Act Article 3 definitions: points (1) AI system, (3) provider, (4) deployer, (5)-(7) authorised rep/importer/distributor, (63)-(66) GPAI", "aia-art-3", "read", 25, "II", sub="II.C"),
            T("Make Anki flashcards from ~40 flagged glossary terms (IAPP wording) + the Art 3 role definitions", "", "flashcards", 30, "I", sub="I.A"),
            T("Week 1 recap: Anki review of all Week 1 cards + write a one-page Domain I summary from memory", "", "review", 20, "I"),
            O("Skim Oliver Patel's Unofficial AIGP Resource Guide and bookmark links for your Weak competencies", "oliverpatel-aigp-guide", "read", 20, "All"),
        ],
    ]),
    dict(theme="First pass: GDPR for AI, Domain III (governing development) and Domain IV (governing deployment)",
         dom=["III", "IV", "II"], days=[
        [  # Wed 30 Sep
            T("Read NIST AI RMF 1.0 PDF Part 1, Section 3 (7 trustworthy-AI characteristics) and Section 5 overview of the Core", "nist-ai-rmf-pdf", "read", 45, "II", sub="II.D"),
            T("Read the AIRC AI RMF Core page: Govern/Map/Measure/Manage and their category IDs (GOVERN 1-6, MAP 1-5, MEASURE 1-4, MANAGE 1-4)", "nist-airc-core", "read", 35, "II", sub="II.D"),
            T("Read GDPR Article 5 (principles): note how purpose limitation and minimisation bite on AI training data", "gdpr-art-5", "read", 20, "II", sub="II.A"),
            T("Read GDPR Article 6 (lawful bases): legitimate interest vs consent for training and deployment", "gdpr-art-6", "read", 20, "II", sub="II.A"),
            O("Watch 'NIST AI RMF deep dive: GOVERN vs MAP vs MEASURE vs MANAGE'", "yt-nist-rmf-functions", "watch", 30, "II", sub="II.D"),
        ],
        [  # Thu 1 Oct
            T("Read NIST AI RMF Playbook MAP 1-5 (context, categorisation, capabilities, risks/benefits, impacts): the design-stage checklist", "nist-playbook-map", "read", 50, "III"),
            T("Read EU AI Act Article 9 (risk management system for high-risk AI)", "aia-art-9", "read", 20, "III"),
            T("Read EU AI Act Article 10 (data and data governance: training, validation, test sets; bias examination)", "aia-art-10", "read", 25, "III"),
            T("Read GDPR Article 22 (automated individual decision-making, incl. profiling)", "gdpr-art-22", "read", 15, "II", sub="II.A"),
            T("Add MAP categories, Art 9 steps and Art 10 data duties to Anki", "", "flashcards", 10, "III"),
        ],
        [  # Fri 2 Oct
            T("Read ICO guidance: 'How should we assess security and data minimisation in AI?'", "ico-ai-security-minimisation", "read", 40, "III"),
            T("Read Datasheets for Datasets (Gebru et al.): abstract + the question sets (motivation, composition, collection, preprocessing, uses)", "datasheets", "read", 25, "III"),
            T("Read Model Cards for Model Reporting (Mitchell et al.): abstract + the model-card sections", "model-cards", "read", 20, "III"),
            T("Make Anki flashcards: Domain III lifecycle stages and the artefact produced at each (intake form, impact assessment, datasheet, model card, test report)", "", "flashcards", 25, "III"),
        ],
        [  # Sat 3 Oct
            T("Read NIST AI RMF Playbook MEASURE 1-4 (metrics, TEVV, bias/fairness, feedback); skim the eval parts you know from BlueDot", "nist-playbook-measure", "read", 50, "III"),
            T("Read NIST AI RMF Playbook MANAGE 1-4 (risk response, third-party risk, post-deployment monitoring, incident communication)", "nist-playbook-manage", "read", 50, "IV"),
            T("Read GDPR Article 35 (DPIA: when required, minimum contents)", "gdpr-art-35", "read", 20, "II", sub="II.A"),
            O("Read OWASP Top 10 for LLM Applications 2025: LLM01-LLM10 titles + mitigations", "owasp-llm-top10", "read", 30, "III"),
        ],
        REST,  # Sun 4 Oct
        [  # Mon 5 Oct
            T("Read EU AI Act Article 26 (obligations of deployers of high-risk AI)", "aia-art-26", "read", 25, "IV"),
            T("Read EU AI Act Article 27 (fundamental rights impact assessment)", "aia-art-27", "read", 20, "IV"),
            T("Work through the ICO AI and data protection risk toolkit: its risk areas and example controls", "ico-ai-toolkit", "read", 30, "IV"),
            T("Read IAPP: 'EU model contractual clauses for AI procurement: a practical guide' (vendor terms, IV.B)", "iapp-mcc-article", "read", 30, "IV"),
            T("Make Anki flashcards: deployer duties, FRIA, DPIA triggers, vendor contract terms", "", "flashcards", 10, "IV"),
            O("Watch 'AIGP How They Passed - July 2026' (the only v2.1-era candidate panel)", "yt-how-they-passed-jul26", "watch", 45, "All"),
        ],
        [  # Tue 6 Oct
            T("Read Singapore Model AI Governance Framework for Agentic AI: agent risks and controls sections (agentic architectures are new in v2.1, IV.A)", "sg-agentic-mgf", "read", 35, "IV"),
            T("Complete Canada's Algorithmic Impact Assessment tool for one invented scenario (e.g., benefits-eligibility triage)", "ca-aia-tool", "practice", 40, "IV"),
            T("Try AI Career Pro's free practice exam / free Domain I-A trial; judge whether the items feel IAPP-like before buying", "pe-aicareerpro", "practice", 30, "All"),
            T("Week 2 recap: cumulative Anki review (Weeks 1-2)", "", "flashcards", 20, "All"),
            O("Read IAPP: 'EDPB weighs in on key questions on personal data in AI models'", "iapp-edpb-article", "read", 20, "II", sub="II.A"),
            O("Drill 20 OpenExamPrep questions untimed (Domains III-IV)", "pe-openexamprep", "practice", 25, "All"),
        ],
    ]),
    dict(theme="EU AI Act article-level deep dive, Mock #1, book the exam, standards (II.C, II.D)",
         dom=["II", "All"], days=[
        [  # Wed 7 Oct
            T("Read AIGP Playbook Domain II notes: II.A (privacy law) and II.B (other laws) sections", "aigpplaybook-d2", "read", 40, "II", sub="II.A"),
            T("Read EU AI Act Article 5 (the prohibited practices)", "aia-art-5", "read", 30, "II", sub="II.C"),
            T("Read EU AI Act Article 6 (high-risk classification rules, incl. the Art 6(3) derogation and profiling carve-back)", "aia-art-6", "read", 20, "II", sub="II.C"),
            T("Read EU AI Act Annex III (the 8 high-risk use-case areas)", "aia-annex-3", "read", 25, "II", sub="II.C"),
            O("Read IAPP Top 10 EU AI Act: 'Understanding and assessing risk'", "iapp-top10-risk", "read", 30, "II", sub="II.C"),
            O("Skim the Commission Guidelines on prohibited AI practices: worked examples for each Art 5 ban", "ec-guidelines-prohibited", "read", 30, "II", sub="II.C"),
        ],
        [  # Thu 8 Oct
            T("Buy ONE v2.1 practice bank: AI Career Pro ($99, 5 full mocks) if its free trial felt IAPP-like; otherwise one Udemy v2.1 bank on sale", "pe-aicareerpro", "practice", 15, "All", ms="Buy practice bank (AI Career Pro, $99)"),
            T("Read EU AI Act Chapter III Section 2 (Arts 8-15 high-risk requirements), focusing on Arts 11 technical documentation, 12 record-keeping, 13 transparency to deployers", "aia-section-3-2", "read", 40, "II", sub="II.C"),
            T("Read EU AI Act Article 14 (human oversight)", "aia-art-14", "read", 20, "III"),
            T("Read EU AI Act Article 25 (value chain: when a deployer/distributor becomes a provider)", "aia-art-25", "read", 25, "II", sub="II.C"),
            T("Read 'Why I failed the AIGP exam' (FAIR Institute): answer as the ideal governance function, not the pragmatic operator", "rep-fair-failed", "read", 10, "All"),
            O("Read IAPP Top 10 EU AI Act: 'Subject matter, definitions, key actors and scope'", "iapp-top10-scope", "read", 30, "II", sub="II.C"),
        ],
        [  # Fri 9 Oct
            T("Read EU AI Act Article 50 (transparency: chatbots, synthetic content, deepfakes, emotion recognition)", "aia-art-50", "read", 20, "II", sub="II.C"),
            T("Read EU AI Act Article 99 (penalty tiers: EUR35m/7%, EUR15m/3%, EUR7.5m/1%)", "aia-art-99", "read", 15, "II", sub="II.C"),
            T("Read the AI Act implementation timeline: ORIGINAL dates (2 Feb 2025, 2 Aug 2025, 2 Aug 2026, 2 Aug 2027)", "aia-timeline", "read", 20, "II", sub="II.C"),
            T("Read Morgan Lewis on the Digital Omnibus: NEW dates (Annex III to 2 Dec 2027, Annex I to 2 Aug 2028)", "omnibus-morganlewis", "read", 25, "II", sub="II.C"),
            T("Read EU AI Act Articles 51 and 53 (systemic-risk GPAI, 10^25 FLOP presumption; GPAI provider obligations); fast, BlueDot-covered", "aia-art-53", "read", 15, "II", sub="II.C"),
            O("Read IAPP Top 10 EU AI Act: 'Obligations for general-purpose AI models'", "iapp-top10-gpai", "read", 25, "II", sub="II.C"),
        ],
        [  # Sat 10 Oct
            T("FULL MOCK #1: AI Career Pro Mock 1, 100 Qs, timed 165 min, no notes (target >=60% overall, >=55% on III and IV)", "pe-aicareerpro", "practice", 165, "All", ms="First practice exam"),
            T("Score Mock #1 by domain; update the gap log; apply the decision rule (keep 27 Oct or move to 10 Nov? fallback course?)", "", "review", 20, "All"),
        ],
        REST,  # Sun 11 Oct
        [  # Mon 12 Oct
            T("BOOK THE EXAM (gated on Mock #1): >=60% and >=55% on III/IV -> book Tue 27 Oct 2026; otherwise book fallback Tue 10 Nov 2026. Book via the IAPP AIGP page, then Pearson VUE (morning slot, or take the afternoon off)", "iapp-aigp-page", "review", 15, "All", ms="Book exam by (gated on Mock #1)"),
            T("Review every Mock #1 item (right and wrong): write why each distractor is wrong", "pe-aicareerpro", "review", 90, "All"),
            O("Run the EU AI Act Compliance Checker on 5 invented scenarios (HR screening, chatbot, credit scoring, emotion recognition at work, product safety component)", "aia-compliance-checker", "practice", 45, "II", sub="II.C"),
        ],
        [  # Tue 13 Oct
            T("Make Anki flashcards from every Mock #1 miss + a two-column date card (original vs Omnibus)", "", "flashcards", 25, "All"),
            T("Read the ISO/IEC 42001 page (AIMS scope, clause structure)", "iso-42001", "read", 5, "II", sub="II.D"),
            T("Read ISMS.online on ISO 42001 Annex A controls (A.2-A.10 objectives)", "isms-42001-annex-a", "read", 35, "II", sub="II.D"),
            T("Skim the NIST AI RMF to ISO/IEC 42001 crosswalk: how the functions map to 42001 clauses", "nist-crosswalk-42001", "read", 15, "II", sub="II.D"),
            T("Read the ISO/IEC 42005 page (AI system impact assessment, new in v2.1)", "iso-42005", "read", 5, "II", sub="II.D"),
            T("Skim the ISO/IEC 42005 to NIST AI RMF crosswalk", "nist-crosswalk-42005", "read", 15, "II", sub="II.D"),
            O("Skim the IAPP US State AI Governance Legislation Tracker (which states, which models)", "iapp-us-state-tracker", "read", 20, "II", sub="II.B"),
        ],
    ]),
    dict(theme="II.A/II.B detail, Domain III deep dive, Mock #2, Domain IV deep dive",
         dom=["II", "III", "IV"], days=[
        [  # Wed 14 Oct
            T("Read FTC 'Operation AI Comply' (Section 5 deception/unfairness applied to AI claims)", "ftc-ai-comply", "read", 20, "II", sub="II.B"),
            T("Read NYC DCWP page on Local Law 144 (AEDT bias audits, candidate notice)", "nyc-aedt", "read", 20, "II", sub="II.B"),
            T("Read McDermott: Colorado SB24-205 blocked, replaced by SB26-189 (eff. 1 Jan 2027); keep the developer/deployer duty-of-care concepts", "co-status-mcdermott", "read", 20, "II", sub="II.B"),
            T("Read Wittliff Cutter: Texas TRAIGA, the Colorado reset and federal preemption (2026)", "texas-traiga", "read", 20, "II", sub="II.B"),
            T("Read GDPR Article 13 (incl. 'meaningful information about the logic involved')", "gdpr-art-13", "read", 15, "II", sub="II.A"),
            T("Read FPF on South Korea's AI Framework (Basic) Act, in force 22 Jan 2026 (new in v2.1)", "kr-ai-basic-act-fpf", "read", 20, "II", sub="II.C"),
            O("Read the Dec 2025 White House EO on a national AI policy framework (state-law preemption)", "us-eo-dec-2025", "read", 20, "II", sub="II.C"),
        ],
        [  # Thu 15 Oct
            T("Read ICO Guidance on AI and data protection: accountability, lawfulness, fairness and transparency sections", "ico-ai-guidance", "read", 45, "II", sub="II.A"),
            T("Read EDPB Opinion 28/2024 executive summary (model anonymity, legitimate-interest 3-step test, consequences of unlawful training)", "edpb-op-28-2024", "read", 25, "II", sub="II.A"),
            T("Read EU AI Act Article 15 (accuracy, robustness and cybersecurity) on the AI Act Service Desk", "aia-art-15-sd", "read", 20, "III"),
            T("Read EU AI Act Article 43 (conformity assessment routes) as a III.C release gate", "aia-art-43", "read", 15, "III"),
            O("Read ICO: 'How do we ensure individual rights in our AI systems?'", "ico-ai-rights", "read", 30, "II", sub="II.A"),
        ],
        [  # Fri 16 Oct
            T("Read AIGP Playbook training material: Domain III module (III.A design/build, III.B data, III.C release/monitoring/maintenance)", "aigpplaybook-training", "read", 60, "III"),
            T("Read EU AI Act Articles 47 and 49 (EU declaration of conformity / CE marking; registration in the EU database)", "aia-art-47", "read", 15, "III"),
            T("Read IAPP Top 10 EU AI Act: 'Post-market monitoring, information sharing and enforcement'", "iapp-top10-pmm", "read", 35, "III"),
            O("Skim NIST AI 100-2e2025 adversarial ML taxonomy: the attack classes (evasion, poisoning, privacy, misuse)", "nist-100-2-2025", "read", 40, "III"),
        ],
        [  # Sat 17 Oct
            T("FULL MOCK #2: AI Career Pro Mock 2, timed 165 min (target >=70% overall, no domain <65%; >=75% counts toward the booking rule)", "pe-aicareerpro", "practice", 165, "All", ms="Second practice exam"),
            T("Score Mock #2 by domain; update the gap log; pick the two weakest competencies for Week 5", "", "review", 20, "All"),
        ],
        REST,  # Sun 18 Oct
        [  # Mon 19 Oct
            T("Review every Mock #2 item: why each distractor is wrong", "pe-aicareerpro", "review", 60, "All"),
            T("Buy the IAPP official AIGP practice exam (~$50-60, price unverified); confirm the store page references BoK v2.1", "pe-iapp-official", "practice", 10, "All", ms="Buy IAPP practice exam"),
            T("Read IAPP Top 10 EU AI Act: 'AI assurance across the risk categories'", "iapp-top10-assurance", "read", 35, "III"),
            O("Read Canada's Directive on Automated Decision-Making (impact levels, requirements)", "ca-dadm", "read", 20, "II", sub="II.C"),
            O("Read China's Interim Measures for Generative AI Services (English translation)", "cn-genai-measures", "read", 20, "II", sub="II.C"),
        ],
        [  # Tue 20 Oct
            T("Read AIGP Playbook training material: Domain IV module (IV.A deploy decision incl. agentic, IV.B assessments/vendor due diligence, IV.C monitoring, incidents, decommissioning)", "aigpplaybook-training", "read", 55, "IV"),
            T("Make Anki flashcards: release gates, post-market monitoring, serious-incident reporting + Mock #2 misses", "", "flashcards", 25, "III"),
            T("Week 4 recap: cumulative Anki review (all decks)", "", "flashcards", 20, "All"),
            O("Skim GDPR Chapter 3 (data subject rights, Arts 12-23) for AI-relevant rights: access, erasure, objection", "gdpr-chapter-3", "read", 15, "II", sub="II.A"),
            O("Read the Council of Europe AI treaty (CETS 225) announcement", "coe-portal", "read", 15, "II", sub="II.C"),
        ],
    ]),
    dict(theme="Consolidation and exam week: Mock #3, IAPP official practice exam, go/no-go, exam Tue 27 Oct",
         dom=["All", "IV", "III"], days=[
        [  # Wed 21 Oct
            T("FULL MOCK #3: AI Career Pro Mock 3, timed 165 min (target >=75% overall, no domain <65-70%). Block a long evening", "pe-aicareerpro", "practice", 165, "All"),
            T("Score Mock #3 by domain and compare with Mock #2", "", "review", 15, "All"),
        ],
        [  # Thu 22 Oct
            T("Review Mock #3 misses; re-read your notes on the 3 most-missed competencies", "pe-aicareerpro", "review", 45, "All"),
            T("Gap closure 1 (default IV.B if the gap log agrees): re-read the IAPP guide to EU model contractual clauses; list 10 vendor due-diligence questions", "iapp-mcc-article", "review", 40, "IV"),
            T("Early go/no-go check on Mocks #2 and #3. If the handbook's reschedule cut-off falls before Sun 25 Oct, decide today", "iapp-handbook-page", "review", 10, "All"),
            O("Read AIGP Playbook reference sheets and checklists (impact assessments, vendor review)", "aigpplaybook-resources", "review", 20, "IV"),
        ],
        [  # Fri 23 Oct
            T("Gap closure 2 (default IV.C): re-read NIST Playbook MANAGE 3-4 (third-party risk, post-deployment monitoring, incident response, decommissioning)", "nist-playbook-manage", "review", 40, "IV"),
            T("Re-read EU AI Act Articles 25 and 26 together: build a provider vs deployer vs 'deemed provider' table", "aia-art-25", "review", 25, "II", sub="II.C"),
            T("Run the OnVUE system check on the exam computer (>=48 h ahead) or confirm the test-centre route; re-read the handbook's ID and room rules", "iapp-handbook-page", "review", 20, "All"),
            O("Drill 40 OpenExamPrep questions untimed on your two weakest competencies", "pe-openexamprep", "practice", 40, "All"),
            O("Watch 'Top 3 Tips to Pass Your AIGP Exam on the First Try'", "yt-top3-tips", "watch", 20, "All"),
        ],
        [  # Sat 24 Oct
            T("IAPP OFFICIAL AIGP PRACTICE EXAM: timed 165 min, exam conditions (target >=70-75%)", "pe-iapp-official", "practice", 165, "All", ms="IAPP official practice exam"),
            T("Score the IAPP practice exam by domain", "", "review", 15, "All"),
        ],
        [  # Sun 25 Oct (light day)
            T("GO/NO-GO: Mocks #2 and #3 both >=75% with no domain <65-70%, AND IAPP practice >=70-75%? Yes: keep Tue 27 Oct. No: reschedule to Tue 10 Nov (if still inside the handbook cut-off) and run the 2-week extension", "iapp-handbook-page", "review", 20, "All", ms="Ready to book exam"),
            O("Optional 20-min Anki pass (due cards only)", "", "flashcards", 20, "All"),
        ],
        [  # Mon 26 Oct
            T("Review every IAPP practice-exam miss: note the qualifier (FIRST/BEST/MOST) and the lifecycle stage each item hinged on", "pe-iapp-official", "review", 50, "All"),
            T("Build your one-page cram sheet: AI Act dates (both schedules), penalty tiers, Art 5 bans, Annex III areas, impact-assessment types (DPIA/FRIA/conformity/42005/AEDT audit)", "", "review", 35, "All"),
            T("Read the AIGP Playbook exam-day revision sheet (100 essential facts by domain); star any fact you can't explain. Then stop; early night", "aigpplaybook-revision", "review", 30, "All"),
            T("Prepare: ID matching registration, clear desk/room (OnVUE), alarm, route", "", "review", 10, "All"),
        ],
        [  # Tue 27 Oct
            T("Light: re-skim only your cram sheet and the starred facts (max 20 min)", "aigpplaybook-revision", "review", 15, "All"),
            T("SIT THE AIGP EXAM: 100 Qs, 165 min (+ optional 15-min break; review flagged first-half items BEFORE the break)", "iapp-aigp-page", "practice", 165, "All", ms="Exam day"),
        ],
    ]),
]

WEEKDAY = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


def build():
    weeks_out, flat = [], []
    date = START
    for wi, w in enumerate(WEEKS, 1):
        days_out = []
        for di, day in enumerate(w["days"], 1):
            rest = day == REST
            tasks = []
            if rest:
                tasks.append(dict(id=f"w{wi}d{di}t1", title="Rest day: no study", url="",
                                  type="review", minutes=0, optional=False, domain="All"))
            else:
                for ti, t in enumerate(day, 1):
                    o = dict(id=f"w{wi}d{di}t{ti}", title=t["title"], url=url_for(t["rid"]),
                             type=t["type"], minutes=t["minutes"], optional=t["optional"],
                             domain=t["domain"])
                    if t["milestone"]:
                        o["milestone"] = t["milestone"]
                    tasks.append(o)
                    flat.append((date, o, t["sub"]))
            days_out.append(dict(date=date.isoformat(), weekday=date.strftime("%A"),
                                 isRestDay=rest, tasks=tasks))
            date += dt.timedelta(days=1)
        core = sum(t["minutes"] for d in days_out for t in d["tasks"] if not t["optional"])
        weeks_out.append(dict(week=wi, theme=w["theme"], bokDomains=w["dom"],
                              targetHours=round(core / 60, 1), days=days_out))

    # "50% of plan" milestone: first core task at which cumulative core minutes >= half
    total_core = sum(o["minutes"] for _, o, _ in flat if not o["optional"])
    cum = 0
    for _, o, _ in flat:
        if o["optional"]:
            continue
        cum += o["minutes"]
        if cum >= total_core / 2:
            if "milestone" in o:
                o["milestone"] += " | 50% of plan"
            else:
                o["milestone"] = "50% of plan"
            break
    return weeks_out, flat, total_core


def main():
    weeks, flat, total_core = build()
    total_opt = sum(o["minutes"] for _, o, _ in flat if o["optional"])
    exam_min = 165
    meta = dict(
        startDate=START.isoformat(),
        examTargetDate=EXAM.isoformat(),
        totalWeeks=len(weeks),
        totalHours=round(total_core / 60, 1),
        coreHours=round(total_core / 60, 1),
        stretchHours=round(total_opt / 60, 1),
        studyHoursExcludingExamSitting=round((total_core - exam_min) / 60, 1),
        bookByDate=BOOK_BY.isoformat(),
        goNoGoDate=GO_NO_GO.isoformat(),
        fallbackExamDate=FALLBACK.isoformat(),
        domains=[dict(id=d["id"], name=d["name"], weight=d["weightApprox"],
                      scoredQuestions=f'{d["questionsMin"]}-{d["questionsMax"]}')
                 for d in RES["exam"]["domains"]],
        targetScores=dict(
            diagnostic="No target; ranks domains",
            mock1=">=60% overall and >=55% on Domains III and IV (else fallback course + book 10 Nov)",
            mock2=">=70% overall, no domain <65% (>=75% counts toward the booking rule)",
            mock3=">=75% overall, no domain <65-70%",
            iappOfficial=">=70-75% timed",
            bookingRule="Mocks #2 and #3 (two consecutive) >=75% with no domain <65-70% AND IAPP official >=70-75%",
        ),
    )
    plan = dict(meta=meta, weeks=weeks)
    (ROOT / "plan").mkdir(exist_ok=True)
    (ROOT / "plan" / "study-plan.json").write_text(json.dumps(plan, indent=2, ensure_ascii=False) + "\n")

    # cumulative core hours at each milestone
    cum, ms_at = 0, []
    for d, o, _ in flat:
        if o["optional"]:
            continue
        if "milestone" in o:
            ms_at.append((d, o["milestone"], cum / 60, o))
        cum += o["minutes"]

    # time by sub-area (core)
    by_sub = defaultdict(int)
    for _, o, sub in flat:
        if not o["optional"]:
            by_sub[sub] += o["minutes"]

    write_md(plan, flat, ms_at, by_sub, total_core, total_opt)
    validate(plan, flat)


# --------------------------------------------------------------------------
def fmt_task(t):
    title = f"[{t['title']}]({t['url']})" if t["url"] else t["title"]
    tags = f"`{t['type']}` · {t['minutes']} min · Domain {t['domain']}"
    extra = ""
    if t["optional"]:
        extra += " · **stretch (optional)**"
    if t.get("milestone"):
        extra += f" · 🏁 **{t['milestone']}**"
    return f"- {title} ({tags}{extra})"


def write_md(plan, flat, ms_at, by_sub, total_core, total_opt):
    m = plan["meta"]
    L = []
    A = L.append
    A("# AIGP Study Plan (BoK v2.1): 23 Sep 2026 to 27 Oct 2026\n")
    A("*Study Plan Agent (2 of 3). Generated 2026-09-23 from `research/aigp-research-report.md` and `research/resources.json`. "
      "Machine-readable version: `plan/study-plan.json` (built by `plan/build_study_plan.py`).*\n")
    A("## 1. Headline\n")
    A(f"| Item | Value |\n|---|---|\n"
      f"| Start (Day 1) | Wed 23 Sep 2026 |\n"
      f"| Weeks | {m['totalWeeks']} (weeks run Wed to Tue; week 5 ends on exam day) |\n"
      f"| Core hours | {m['coreHours']} h, including the 2.75-h exam sitting (≈{m['studyHoursExcludingExamSitting']} h of study) |\n"
      f"| Stretch hours (optional) | {m['stretchHours']} h, for 15-h weeks |\n"
      f"| **Book exam by** | **Mon 12 Oct 2026** (gated on Mock #1; check seat availability on Day 1) |\n"
      f"| Go/no-go (readiness gate) | Sun 25 Oct 2026 (early check Thu 22 Oct) |\n"
      f"| **Target exam date** | **Tue 27 Oct 2026** (Pearson VUE test centre or OnVUE; book a morning slot or take the afternoon off) |\n"
      f"| Fallback exam date | Tue 10 Nov 2026 |\n")
    A("## 2. Why 5 weeks (exam Tue 27 Oct)\n")
    A("- **Research estimate:** median ≈ 55 h for passers (range 40–80 h). The research agent's estimate for you is 50–65 h. The evidence is weak and triangulated.\n"
      "- **Minus about 6 h for background.** BlueDot already covers I.A (AI types, risks and harms), GPAI and systemic-risk provisions, the global policy landscape, and evals/red-teaming. The plan skims these (OECD, the AI-definition guidelines, Arts 51/53, NIST 600-1 and OWASP are fast reads or stretch tasks) instead of studying them.\n"
      "- **Plus about 10 h for full-length practice.** The booking rule requires three full timed mocks plus the IAPP practice exam. That is 4 × 165 min ≈ 11 h of sitting, plus reviews. Generic hour estimates under-count this.\n"
      "- **Result:** 55 − 6 + 10 ≈ **59–62 h**. You asked for an exam on **Tue 27 Oct**, which is exactly 5 Wed–Tue weeks from Day 1. At ~12 h/week that gives ≈ 58 h of study plus the exam sitting: inside the estimate, with no spare buffer week. The 6-week version had one. Week 5 carries Mock #3, the IAPP practice exam and the exam itself, so it runs heavier (≈ 11.7 h of study + the 2.75-h exam).\n- **Weekday-first schedule:** Wed, Thu, Fri, Mon and Tue carry about 1.5–2 h each (≈ 79% of core time). **Saturday** is the one longer weekend session: the full mocks go there. **Sunday is the rest day** (in week 5 it is a 20-min go/no-go check).\n"
      "- About 70% of core study time goes to Domains III and IV and to II.A–II.C, the areas BlueDot does not cover (see §5).\n"
      "- **Buffer:** there is no buffer week any more. The safety net is the readiness gate: if it fails, the fallback date Tue 10 Nov adds 2 weeks.\n")
    A("### Booking logic (why there are two booking milestones)\n")
    A("Pearson VUE seats usually need booking about 2–3 weeks ahead. The research readiness rule (two consecutive mocks ≥75% plus the IAPP practice exam ≥70–75%) can only be met in week 5, 2–3 days before the target date. So the plan books in two steps:\n\n"
      "1. **Mon 12 Oct: book**, 15 days ahead, gated on Mock #1 (Sat 10 Oct). If Mock #1 is ≥60% overall and ≥55% on III and IV, book **Tue 27 Oct**. Otherwise book **Tue 10 Nov** and buy the fallback course (§8). On Day 1, check Pearson VUE seat availability for 27 Oct. If seats look scarce, book right away and reschedule later if Mock #1 misses, within the handbook's reschedule rules.\n"
      "2. **Sun 25 Oct: go/no-go (\"Ready to book exam\").** Keep 27 Oct only if the full rule is met. Otherwise reschedule to 10 Nov. There is also an early check on Thu 22 Oct (Mocks #2 and #3).\n\n"
      "Read the Candidate Handbook on Day 1 for the reschedule cut-off and fee; the research could not verify them. Pearson VUE reschedules are often allowed up to 24–48 h before the exam, but IAPP's own cut-off may be earlier. If it falls before Sun 25 Oct, make the call at the Thu 22 Oct early check using Mocks #2 and #3.\n\n"
      "**If 27 Oct is not available:** take the nearest weekday seat (Wed 28 – Fri 30 Oct) and repeat the Mon 26 Oct review pattern on the extra days. OnVUE usually has more availability than test centres.\n")

    A("## 3. Weekly overview\n")
    A("| Week | Dates | Theme | BoK domains | Core h | Stretch h | Milestones |\n|---|---|---|---|---|---|---|")
    for w in plan["weeks"]:
        d0, d1 = w["days"][0]["date"], w["days"][-1]["date"]
        opt = sum(t["minutes"] for d in w["days"] for t in d["tasks"] if t["optional"]) / 60
        ms = [t["milestone"] for d in w["days"] for t in d["tasks"] if t.get("milestone")]
        A(f"| {w['week']} | {d0} → {d1} | {w['theme']} | {', '.join(w['bokDomains'])} | {w['targetHours']} | {opt:.1f} | {'; '.join(ms) or '—'} |")
    A(f"| **Total** | | | | **{total_core/60:.1f}** | **{total_opt/60:.1f}** | |\n")
    A("A normal week looks like this: **weekdays (Wed, Thu, Fri, Mon, Tue) about 1.5–2 h each**; **Sat is one 1.5–3 h session** (the full mocks are on Saturdays); **Sun is the rest day**. About 79% of core time falls on weekdays. Stretch tasks (marked *optional*) add about 2–3 h for a 15-h week. Week 5 is the exam week: Mock #3 on Wed, the IAPP practice exam on Sat, a 20-min go/no-go on Sun, the exam on Tue.\n")

    A("## 4. Practice-exam schedule, targets and what to do if you miss\n")
    A("| # | Date | Cum. core h at start | What | Target | If missed |\n|---|---|---|---|---|---|")
    prow = []
    rows = {
        "Diagnostic": ("IAPP free-guide sample Qs + AIGP Playbook 15-Q preview, untimed", "None. It ranks the domains", "Nothing to fix. Use it to order your gap log"),
        "First practice exam": ("Mock #1: AI Career Pro Mock 1, timed 165 min", "≥60% overall; ≥55% on III and IV", "Buy the fallback course (§8) and use its III/IV modules in the week 4 stretch slots. **Book 10 Nov instead of 27 Oct.**"),
        "Second practice exam": ("Mock #2: AI Career Pro Mock 2, timed", "≥70% overall, no domain <65% (≥75% counts toward the booking rule)", "Spend all week 5 stretch time on the two weakest competencies. If <65%, move to 10 Nov now rather than at the go/no-go"),
        "IAPP official practice exam": ("IAPP official practice exam (PDF), timed 165 min", "≥70–75%", "Reschedule to 10 Nov at the go/no-go. In the extension, re-study the missed competencies and sit AI Career Pro Mocks 4 and 5 as the new 'two consecutive'"),
    }
    for d, ms, h, o in ms_at:
        for key, (what, tgt, miss) in rows.items():
            if key in ms:
                prow.append((d, f"| {key} | {d.strftime('%a %d %b')} | {h:.1f} h | {what} | {tgt} | {miss} |"))
    # Mock 3 has no milestone label; add explicitly
    cum = 0
    for d, o, _ in flat:
        if o["optional"]:
            continue
        if o["title"].startswith("FULL MOCK #3"):
            prow.append((d, f"| Mock #3 | {d.strftime('%a %d %b')} | {cum/60:.1f} h | AI Career Pro Mock 3, timed | ≥75%, no domain <65–70% | Counts with Mock #2 as the 'two consecutive'. If only Mock #3 hits 75%, sit Mock 4 in the extension and reschedule to 10 Nov |"))
        cum += o["minutes"]
    for _, r in sorted(prow, key=lambda x: x[0]):
        A(r)
    A("\n**Booking rule (from research):** two consecutive full mocks ≥75% with no domain below 65–70%, AND the IAPP official practice exam ≥70–75%, AND you can explain why each wrong option is wrong. Third-party scores run optimistic, and IAPP publishes no mapping from practice % to the 300 cut score. OpenExamPrep is for drilling only; don't use its score to judge readiness.\n")
    A("**Two-week extension (only if you move to 10 Nov):** repeat the week 4 pattern (weekdays first, Sunday off). Spend about 12 h/week on the gap log's weakest competencies, then sit AI Career Pro Mock 4 (Sat 31 Oct) and Mock 5 (Sat 7 Nov), with a light Sun 8 and Mon 9 Nov. No new resources are needed.\n")

    A("## 5. Where the time goes (core study minutes by BoK area)\n")
    A("| Area | Core h | Share |\n|---|---|---|")
    total_study = sum(v for k, v in by_sub.items())
    order = ["I.A", "I", "II.A", "II.B", "II.C", "II.D", "III", "IV", "All"]
    labels = {"I.A": "I.A (what AI is; BlueDot-strong, fast)", "I": "I.B–I.C (programme, policies)",
              "II.A": "II.A privacy law", "II.B": "II.B other laws", "II.C": "II.C EU AI Act + other AI laws",
              "II.D": "II.D standards (NIST, ISO, OECD)", "III": "III development", "IV": "IV deployment",
              "All": "Mixed: diagnostic, mocks, reviews, recaps, logistics, exam"}
    for k in order:
        if k in by_sub:
            A(f"| {labels[k]} | {by_sub[k]/60:.1f} | {100*by_sub[k]/total_study:.0f}% |")
    focus = sum(by_sub.get(k, 0) for k in ["II.A", "II.B", "II.C", "III", "IV"])
    non_mixed = total_study - by_sub.get("All", 0)
    A(f"\nIII + IV + II.A–C = **{100*focus/non_mixed:.0f}% of topic study time** (excluding mixed practice/review). Most of the mixed practice time is also III/IV-weighted, because those domains are ~54% of the questions.\n")

    A("## 6. Daily plan\n")
    A("Each task shows: type · minutes · BoK domain. Stretch tasks are optional. 🏁 marks a milestone. The Anki deck is self-made, built from the IAPP glossary, EU AI Act articles and your mock misses; no link is given because Anki's site is not in the verified resource list.\n")
    for w in plan["weeks"]:
        core = w["targetHours"]
        opt = sum(t["minutes"] for d in w["days"] for t in d["tasks"] if t["optional"]) / 60
        A(f"### Week {w['week']}: {w['theme']}")
        A(f"**{w['days'][0]['date']} → {w['days'][-1]['date']} · Core {core} h · Stretch {opt:.1f} h · Total if all done {core+opt:.1f} h · Domains {', '.join(w['bokDomains'])}**\n")
        for d in w["days"]:
            dd = dt.date.fromisoformat(d["date"])
            mins = sum(t["minutes"] for t in d["tasks"] if not t["optional"])
            label = " (REST)" if d["isRestDay"] else f" ({mins} min core)"
            A(f"#### {d['weekday']} {dd.strftime('%d %b %Y')}{label}")
            if d["isRestDay"]:
                A("- Rest day: no study.\n")
                continue
            for t in d["tasks"]:
                A(fmt_task(t))
            A("")
    A("## 7. Exam-week checklist\n")
    A("""**By Fri 23 Oct (≥48 h before)**
- [ ] Confirmation email from Pearson VUE: date, time, time zone, test centre or OnVUE.
- [ ] Name on your ID matches your registration exactly (see the [Candidate Handbook](https://prod.iapp.org/media/pdf/certification/IAPP_Certification_Handbook_Updated.pdf)).
- [ ] OnVUE: run the system check on the *same* computer and network. Use a walled room with the door closed, a clear desk, no second monitor, and no one entering. Turn off VPNs, corporate device-management software and notifications. Test centre: plan the route and arrive 30 min early.
- [ ] Stop new material. Only revision from here: the cram sheet, the 100-facts sheet, Anki.

**Sun 25 – Mon 26 Oct**
- [ ] Go/no-go on Sunday. Monday: final review only (cram sheet, 100-facts sheet). No new material. Early night on Monday.
- [ ] OnVUE: dry-run the room set-up the evening before. Keep your phone out of reach but available for the check-in photos.

**Exam day, Tue 27 Oct**
- [ ] Eat, hydrate, and log in or arrive early (OnVUE check-in opens about 30 min before).
- [ ] Pacing: 165 min for 100 Qs ≈ 1.65 min each. Aim to finish the first half in about 75 min.
- [ ] If you take the optional 15-min break, **review flagged first-half items before the break**, because the first half locks.
- [ ] For each scenario, ask: who is the actor (provider/deployer/importer; controller/processor)? What lifecycle stage is it? What does the governance *process* require next?
- [ ] Watch for FIRST / BEST / MOST / PRIMARY. Choose the ideal-governance answer (assess, document, consult, follow or update policy, escalate), not the pragmatic shortcut.
- [ ] EU AI Act dates: know both the original schedule (Aug 2026 / Aug 2027) and the Omnibus schedule (2 Dec 2027 Annex III; 2 Aug 2028 Annex I). Answer from the concept.
- [ ] Colorado: SB24-205 was blocked and replaced by SB26-189 (effective 1 Jan 2027). The developer/deployer duty-of-care concepts are still testable.
- [ ] No penalty for guessing, so answer every item. 15 items are unscored pilots you can't identify, so treat all 100 as real.

**After**
- [ ] Pass: note the certification maintenance requirements from the [IAPP AIGP page](https://iapp.org/certify/aigp).
- [ ] Fail: the retake fee is $625 ($475 for members), with a wait of at least 7 days (verify in the handbook). Re-enter the extension plan, focused on the domains in your score report.
""")
    A("## 8. Budget\n")
    A("""All study materials in the plan are free except the practice exams. The research could not verify prices marked *unverified*; check them at purchase.

| Item | Cost (USD) | Status | When to buy | Link |
|---|---|---|---|---|
| AI Career Pro AIGP Exam Prep (5 full v2.1 mocks, 700+ Qs) | $99 | Core (the Mock #1–#3 bank) | Thu 8 Oct, after trying its free trial on Tue 6 Oct | [governance.aicareer.pro](https://governance.aicareer.pro/course/aigp-exam-prep) |
| *Alternative to the above:* one Udemy v2.1 bank (6×100 "600 Questions" set or the rebuilt 800-Q set) | sale price unverified (usually below AI Career Pro) | Only if the AI Career Pro trial doesn't feel IAPP-like | Thu 8 Oct | see `research/resources.json` → practiceExams |
| IAPP official AIGP practice exam (digital) | ~$50–60 *(unverified)* | Core | Mon 19 Oct (the plan uses it Sat 24 Oct) | [store.iapp.org](https://store.iapp.org/aigp-practice-exam-digital/) |
| **AIGP exam fee** | **$799** non-member / $649 member (membership ≈ $295/yr, *unverified*, so non-member is cheaper unless you want membership anyway) | Core | Mon 12 Oct (after Mock #1) | [IAPP AIGP page](https://iapp.org/certify/aigp) |
| Fallback prep course: Kyle David AIGP Masterclass (Udemy, video-only) | Udemy sale price *unverified* (typically well under $150) | **Conditional**: only if Mock #1 is <60% or <55% on III/IV. Confirm the page says v2.1 | Mon 12 Oct (after Mock #1) | [udemy.com/course/aigp-masterclass](https://www.udemy.com/course/aigp-masterclass/) |
| Retake fee (contingency) | $625 non-member / $475 member | Only if needed | — | — |

**Expected spend: ≈ $799 + $99 + ~$55 ≈ $953** (non-member). The worst case adds the Udemy fallback course (sale price) and a $625 retake. The free resources are the BoK, IAPP glossary/trackers/Top-10 series, the AIGP Playbook, NIST/ICO/EDPB/EUR-Lex/artificialintelligenceact.eu, OpenExamPrep and Anki.
""")
    A("## 9. Caveats\n")
    A("""- **Links:** every task link comes from `research/resources.json`. Study links are all `verified: true` entries, meaning the exact URL appeared in a live web search on 2026-09-23; the sandbox could not open the pages. The practice-exam links (AI Career Pro, AIGP Playbook preview, OpenExamPrep, IAPP store) come from the `practiceExams` section, which has no per-entry `verified` flag; research §5 lists them as Recommend/Optional. The four `verified: false` GDPR URLs (Arts 9, 14, 15, 25 on gdpr-info.eu) are not used.
- **BoK wording:** the research could not open the BoK v2.1 PDF, so the competency wording is reconstructed. Day 1's BoK read is where you correct the plan's domain tags if the PDF differs.
- **Hours:** the estimates rest on weak evidence. This 5-week version has no buffer week. If Mocks #1–#2 are weak, move to 10 Nov early rather than cramming.
- **AIGP Playbook "training material" (Domain III/IV modules):** the research verified the hub page, not per-domain pages. Open the hub and pick the Domain III / IV section.
""")
    (ROOT / "plan" / "aigp-study-plan.md").write_text("\n".join(L))


# --------------------------------------------------------------------------
def validate(plan, flat):
    ok = True
    print("=== VALIDATION ===")
    ids = [t["id"] for w in plan["weeks"] for d in w["days"] for t in d["tasks"]]
    dup = len(ids) - len(set(ids))
    print(f"[{'PASS' if dup == 0 else 'FAIL'}] unique task IDs: {len(ids)} ids, {dup} duplicates")
    ok &= dup == 0

    bad_fmt = []
    for w in plan["weeks"]:
        for di, d in enumerate(w["days"], 1):
            for ti, t in enumerate(d["tasks"], 1):
                if t["id"] != f"w{w['week']}d{di}t{ti}":
                    bad_fmt.append(t["id"])
    print(f"[{'PASS' if not bad_fmt else 'FAIL'}] ID format w{{week}}d{{day}}t{{task}} matches position: {len(bad_fmt)} mismatches")
    ok &= not bad_fmt

    vurls = {r["url"] for r in RES["resources"] if r.get("verified") is True}
    peurls = set(PE.values())
    n_v = n_pe = n_empty = 0
    bad_url = []
    for w in plan["weeks"]:
        for d in w["days"]:
            for t in d["tasks"]:
                u = t["url"]
                if not u:
                    n_empty += 1
                elif u in vurls:
                    n_v += 1
                elif u in peurls:
                    n_pe += 1
                else:
                    bad_url.append((t["id"], u))
                if u in UNVERIFIED_URLS and u not in vurls:
                    bad_url.append((t["id"], "UNVERIFIED " + u))
    print(f"[{'PASS' if not bad_url else 'FAIL'}] URLs: {n_v} in resources[] with verified=true; "
          f"{n_pe} from practiceExams (Recommend/Optional, no per-entry verified flag); {n_empty} empty; {len(bad_url)} invalid")
    for b in bad_url:
        print("    invalid:", b)
    ok &= not bad_url
    print("    practiceExams URLs used:", sorted({t['url'] for w in plan['weeks'] for d in w['days'] for t in d['tasks'] if t['url'] in peurls and t['url'] not in vurls}))

    bad_wd, expected = [], START
    for w in plan["weeks"]:
        for d in w["days"]:
            dd = dt.date.fromisoformat(d["date"])
            if dd != expected or WEEKDAY[dd.weekday()] != d["weekday"]:
                bad_wd.append(d["date"])
            expected += dt.timedelta(days=1)
        if w["days"][0]["weekday"] != "Wednesday":
            bad_wd.append(f"week {w['week']} does not start Wednesday")
    last = plan["weeks"][-1]["days"][-1]["date"]
    print(f"[{'PASS' if not bad_wd else 'FAIL'}] dates consecutive from {START}, weekdays correct (datetime), weeks start Wed: {len(bad_wd)} errors; last day {last} (exam {plan['meta']['examTargetDate']})")
    ok &= not bad_wd and last == plan["meta"]["examTargetDate"]

    enums_bad = [t["id"] for w in plan["weeks"] for d in w["days"] for t in d["tasks"]
                 if t["type"] not in {"read", "watch", "practice", "review", "flashcards"}
                 or t["domain"] not in {"I", "II", "III", "IV", "All"}]
    print(f"[{'PASS' if not enums_bad else 'FAIL'}] type/domain enums: {len(enums_bad)} bad")
    ok &= not enums_bad

    print("Per-week totals (core must match targetHours; 10-13 h core except exam week; rest day present):")
    tot = 0
    for w in plan["weeks"]:
        core = sum(t["minutes"] for d in w["days"] for t in d["tasks"] if not t["optional"])
        opt = sum(t["minutes"] for d in w["days"] for t in d["tasks"] if t["optional"])
        rest = any(d["isRestDay"] for d in w["days"])
        light = any((not d["isRestDay"]) and sum(t["minutes"] for t in d["tasks"] if not t["optional"]) <= 30 for d in w["days"])
        match = abs(round(core / 60, 1) - w["targetHours"]) < 1e-9
        in_range = 10 <= core / 60 <= 13 or w["week"] == len(plan["weeks"])
        good = match and in_range and (rest or light)
        ok &= good
        tot += core
        print(f"  [{'PASS' if good else 'FAIL'}] W{w['week']}: core {core/60:.1f} h (targetHours {w['targetHours']}), stretch {opt/60:.1f} h, total {(core+opt)/60:.1f} h, rest day {rest}, light day {light}")
    mt = abs(round(tot / 60, 1) - plan["meta"]["totalHours"]) < 1e-9
    print(f"[{'PASS' if mt else 'FAIL'}] meta.totalHours {plan['meta']['totalHours']} == sum of core {tot/60:.1f}")
    ok &= mt

    need = ["Diagnostic", "First practice exam", "50% of plan", "Second practice exam",
            "IAPP official practice exam", "Ready to book exam", "Exam day", "Buy IAPP practice exam"]
    have = " | ".join(t.get("milestone", "") for w in plan["weeks"] for d in w["days"] for t in d["tasks"])
    missing = [n for n in need if n not in have]
    print(f"[{'PASS' if not missing else 'FAIL'}] required milestones present: missing {missing}")
    ok &= not missing

    schema_ok = set(plan) == {"meta", "weeks"} and all(
        set(w) == {"week", "theme", "bokDomains", "targetHours", "days"} and all(
            set(d) == {"date", "weekday", "isRestDay", "tasks"} and all(
                {"id", "title", "url", "type", "minutes", "optional", "domain"} <= set(t) <= {"id", "title", "url", "type", "minutes", "optional", "domain", "milestone"}
                for t in d["tasks"]) for d in w["days"]) for w in plan["weeks"])
    print(f"[{'PASS' if schema_ok else 'FAIL'}] schema keys match spec")
    ok &= schema_ok
    print("OVERALL:", "PASS" if ok else "FAIL")


if __name__ == "__main__":
    main()
