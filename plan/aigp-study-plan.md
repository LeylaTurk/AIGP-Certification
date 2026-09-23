# AIGP Study Plan (BoK v2.1): 23 Sep 2026 to 27 Oct 2026

*Study Plan Agent (2 of 3). Generated 2026-09-23 from `research/aigp-research-report.md` and `research/resources.json`. Machine-readable version: `plan/study-plan.json` (built by `plan/build_study_plan.py`).*

## 1. Headline

| Item | Value |
|---|---|
| Start (Day 1) | Wed 23 Sep 2026 |
| Weeks | 5 (weeks run Wed to Tue; week 5 ends on exam day) |
| Core hours | 60.6 h, including the 2.75-h exam sitting (≈57.8 h of study) |
| Stretch hours (optional) | 8.8 h, for 15-h weeks |
| **Book exam by** | **Mon 12 Oct 2026** (gated on Mock #1; check seat availability on Day 1) |
| Go/no-go (readiness gate) | Sun 25 Oct 2026 (early check Thu 22 Oct) |
| **Target exam date** | **Tue 27 Oct 2026** (Pearson VUE test centre or OnVUE; book a morning slot or take the afternoon off) |
| Fallback exam date | Tue 10 Nov 2026 |

## 2. Why 5 weeks (exam Tue 27 Oct)

- **Research estimate:** median ≈ 55 h for passers (range 40–80 h). The research agent's estimate for you is 50–65 h. The evidence is weak and triangulated.
- **Minus about 6 h for background.** BlueDot already covers I.A (AI types, risks and harms), GPAI and systemic-risk provisions, the global policy landscape, and evals/red-teaming. The plan moves through these fast: the course's I.A lessons at 1.5× speed on Day 1, and OWASP and the GPAI material as stretch tasks.
- **Plus about 10 h for full-length practice.** The booking rule requires three full timed mocks plus the IAPP practice exam. That is 4 × 165 min ≈ 11 h of sitting, plus reviews. Generic hour estimates under-count this.
- **Result:** 55 − 6 + 10 ≈ **59–62 h**. You asked for an exam on **Tue 27 Oct**, which is exactly 5 Wed–Tue weeks from Day 1. At ~12 h/week that gives ≈ 58 h of study plus the exam sitting: inside the estimate, with no spare buffer week. The 6-week version had one. Week 5 carries Mock #3, the IAPP practice exam and the exam itself, so it runs heavier (≈ 11.7 h of study + the 2.75-h exam).
- **Weekday-first schedule:** Wed, Thu, Fri, Mon and Tue carry about 1.5–2 h each (≈ 79% of core time). **Saturday** is the one longer weekend session: the full mocks go there. **Sunday is the rest day** (in week 5 it is a 20-min go/no-go check).
- About 70% of topic study time goes to Domains III and IV and to II.A–II.C, the areas BlueDot does not cover (see §5).
- **Buffer:** there is no buffer week any more. The safety net is the readiness gate: if it fails, the fallback date Tue 10 Nov adds 2 weeks.

### Booking logic (why there are two booking milestones)

Pearson VUE seats usually need booking about 2–3 weeks ahead. The research readiness rule (two consecutive mocks ≥75% plus the IAPP practice exam ≥70–75%) can only be met in week 5, 2–3 days before the target date. So the plan books in two steps:

1. **Mon 12 Oct: book**, 15 days ahead, gated on Mock #1 (Sat 10 Oct). If Mock #1 is ≥60% overall and ≥55% on III and IV, book **Tue 27 Oct**. Otherwise book **Tue 10 Nov** and redo the course lessons for III/IV (§4). On Day 1, check Pearson VUE seat availability for 27 Oct. If seats look scarce, book right away and reschedule later if Mock #1 misses, within the handbook's reschedule rules.
2. **Sun 25 Oct: go/no-go ("Ready to book exam").** Keep 27 Oct only if the full rule is met. Otherwise reschedule to 10 Nov. There is also an early check on Thu 22 Oct (Mocks #2 and #3).

Read the Candidate Handbook on Day 1 for the reschedule cut-off and fee; the research could not verify them. Pearson VUE reschedules are often allowed up to 24–48 h before the exam, but IAPP's own cut-off may be earlier. If it falls before Sun 25 Oct, make the call at the Thu 22 Oct early check using Mocks #2 and #3.

**If 27 Oct is not available:** take the nearest weekday seat (Wed 28 – Fri 30 Oct) and repeat the Mon 26 Oct review pattern on the extra days. OnVUE usually has more availability than test centres.

## 3. How the plan is built: a course first, then hands-on practice

You said you learn best with a course that joins up the topics, and that reading on its own won't keep you going. So the plan is built like this:

- **Weeks 1–3: course-led first pass.** The [AI Career Pro AIGP course](https://governance.aicareer.pro/course/aigp-exam-prep) (v2.1; 117 videos of about 5 minutes, each with a written and an audio version; 700+ questions; 5 full mocks) covers **one BoK sub-domain per study day**, in BoK order: I.A → IV.C, all 13 before Mock #1. Every course day has the same three steps:
  1. **Watch** that sub-domain's lessons (~45 min).
  2. **Quiz**: that topic's course questions straight away (~20 min). Every miss becomes an Anki card.
  3. **Do**: one primary source *or* one hands-on task (~20–30 min), so you see the real text or apply the idea the same day.
- **NovaPay labs.** The hands-on tasks all use one invented company, *NovaPay* (a 500-person EU/US fintech). Each lab builds on the one before, which is how the dots connect: governance structure (Lab 1) → AI policy and inventory (Lab 2) → EU AI Act risk tiers (Lab 3) → datasheet (Lab 4) → vendor questionnaire (Lab 5) → high-risk checklist and FRIA/DPIA (Lab 6) → NIST↔ISO table (Lab 7) → monitoring and incident plan (Lab 8). By exam day you will have walked one company through the whole BoK lifecycle, which is what the scenario questions test.
- **Weeks 3–5: applied deep dive + mocks.** Primary sources, each paired with a lab or recall task, plus Mocks #1–#3 and the IAPP practice exam.
- **Motivation hooks.** A visible streak and progress ring in the tracker; voice-memo teach-backs; a score trend on the practice-exam log; and short course videos with audio versions you can play on a walk or commute.

**Core time by activity:** practice 26.1 h (43%) · read 13.8 h (23%) · watch 10.1 h (17%) · review 8.4 h (14%) · flashcards 2.2 h (4%). Pure reading is about a quarter of the plan; most of the rest is doing.

## 3b. Weekly overview

| Week | Dates | Theme | BoK domains | Core h | Stretch h | Milestones |
|---|---|---|---|---|---|---|
| 1 | 2026-09-23 → 2026-09-29 | Course kick-off, diagnostic, Domain I (foundations) and II.A-II.B (privacy and other laws) | I, II | 10.8 | 2.8 | Diagnostic; Buy course (AI Career Pro, $99) |
| 2 | 2026-09-30 → 2026-10-06 | Course: II.C-II.D (EU AI Act, standards) and III.A-III.C (governing development), plus EU AI Act lab | II, III | 11.2 | 2.2 | — |
| 3 | 2026-10-07 → 2026-10-13 | Course: IV.A-IV.C (governing deployment), Mock #1, book the exam, EU AI Act high-risk deep dive | IV, II, All | 12.6 | 0.5 | First practice exam | 50% of plan; Book exam by (gated on Mock #1) |
| 4 | 2026-10-14 → 2026-10-20 | Applied deep dive: FRIA/DPIA lab, GDPR and US laws, Mock #2, standards, post-market | II, III, IV | 11.9 | 2.3 | Second practice exam; Buy IAPP practice exam |
| 5 | 2026-10-21 → 2026-10-27 | Consolidation and exam week: Mock #3, IAPP official practice exam, go/no-go, exam Tue 27 Oct | All, IV, III | 14.2 | 1.0 | IAPP official practice exam; Ready to book exam; Exam day |
| **Total** | | | | **60.6** | **8.8** | |

A normal week looks like this: **weekdays (Wed, Thu, Fri, Mon, Tue) about 1.5–2 h each**; **Sat is one 1.5–3 h session** (the full mocks are on Saturdays); **Sun is the rest day**. About 79% of core time falls on weekdays. Stretch tasks (marked *optional*) add about 2–3 h for a 15-h week. Week 5 is the exam week: Mock #3 on Wed, the IAPP practice exam on Sat, a 20-min go/no-go on Sun, the exam on Tue.

## 4. Practice-exam schedule, targets and what to do if you miss

| # | Date | Cum. core h at start | What | Target | If missed |
|---|---|---|---|---|---|
| Diagnostic | Thu 24 Sep | 1.8 h | IAPP free-guide sample Qs + AIGP Playbook 15-Q preview, untimed | None. It ranks the domains | Nothing to fix. Use it to order your gap log |
| First practice exam | Sat 10 Oct | 27.6 h | Mock #1: AI Career Pro Mock 1, timed 165 min | ≥60% overall; ≥55% on III and IV | Rewatch the course lessons for III/IV and redo their quiz questions in the week 4 stretch slots. If you want a second teacher, add Kyle David's Udemy course on sale (§8). **Book 10 Nov instead of 27 Oct.** |
| Second practice exam | Sat 17 Oct | 39.3 h | Mock #2: AI Career Pro Mock 2, timed | ≥70% overall, no domain <65% (≥75% counts toward the booking rule) | Spend all week 5 stretch time on the two weakest competencies. If <65%, move to 10 Nov now rather than at the go/no-go |
| Mock #3 | Wed 21 Oct | 46.4 h | AI Career Pro Mock 3, timed | ≥75%, no domain <65–70% | Counts with Mock #2 as the 'two consecutive'. If only Mock #3 hits 75%, sit Mock 4 in the extension and reschedule to 10 Nov |
| IAPP official practice exam | Sat 24 Oct | 52.2 h | IAPP official practice exam (PDF), timed 165 min | ≥70–75% | Reschedule to 10 Nov at the go/no-go. In the extension, re-study the missed competencies and sit AI Career Pro Mocks 4 and 5 as the new 'two consecutive' |

**Booking rule (from research):** two consecutive full mocks ≥75% with no domain below 65–70%, AND the IAPP official practice exam ≥70–75%, AND you can explain why each wrong option is wrong. Third-party scores run optimistic, and IAPP publishes no mapping from practice % to the 300 cut score. OpenExamPrep is for drilling only; don't use its score to judge readiness.

**Two-week extension (only if you move to 10 Nov):** repeat the week 4 pattern (weekdays first, Sunday off). Spend about 12 h/week on the gap log's weakest competencies, then sit AI Career Pro Mock 4 (Sat 31 Oct) and Mock 5 (Sat 7 Nov), with a light Sun 8 and Mon 9 Nov. No new resources are needed.

## 5. Where the time goes (core study minutes by BoK area)

| Area | Core h | Share |
|---|---|---|
| I.A (what AI is; BlueDot-strong, fast) | 0.6 | 1% |
| I.B–I.C (programme, policies) | 3.8 | 6% |
| II.A privacy law | 3.4 | 6% |
| II.B other laws | 2.4 | 4% |
| II.C EU AI Act + other AI laws | 6.2 | 10% |
| II.D standards (NIST, ISO, OECD) | 2.8 | 5% |
| III development | 6.8 | 11% |
| IV deployment | 7.7 | 13% |
| Mixed: diagnostic, mocks, reviews, recaps, logistics, exam | 27.1 | 45% |

III + IV + II.A–C = **79% of topic study time** (excluding mixed practice/review). Most of the mixed practice time is also III/IV-weighted, because those domains are ~54% of the questions.

## 6. Daily plan

Each task shows: type · minutes · BoK domain. Stretch tasks are optional. 🏁 marks a milestone. The Anki deck is self-made, built from your course-quiz and mock misses; NovaPay labs have no link because they are your own work; no link is given because Anki's site is not in the verified resource list.

### Week 1: Course kick-off, diagnostic, Domain I (foundations) and II.A-II.B (privacy and other laws)
**2026-09-23 → 2026-09-29 · Core 10.8 h · Stretch 2.8 h · Total if all done 13.6 h · Domains I, II**

#### Wednesday 23 Sep 2026 (110 min core)
- [Read the AIGP BoK v2.1 PDF: all four domains' competencies and performance indicators; tag each line Strong / Partial / Weak against your BlueDot background](https://assets.contentstack.io/v3/assets/bltd4dd5b2d705252bc/blt579bac3f0b35f278/69494b068965be6043ba2815/AIGP_BOK_2.1.0_FINAL.pdf) (`read` · 45 min · Domain All)
- [Read the IAPP Candidate Handbook PDF: scheduling, rescheduling/cancellation cut-offs, ID rules, OnVUE requirements. Check Pearson VUE seats for Tue 27 Oct](https://prod.iapp.org/media/pdf/certification/IAPP_Certification_Handbook_Updated.pdf) (`read` · 20 min · Domain All)
- [Request the free IAPP AIGP study guide (form); check it shows the 4-domain structure](https://iapp.org/l/aigp-study-guide-request) (`read` · 10 min · Domain All)
- [AI Career Pro FREE trial: course intro + Domain I.A lessons (what AI is, AI types, risks and harms). BlueDot-covered, so watch at 1.5x](https://governance.aicareer.pro/course/aigp-exam-prep) (`watch` · 35 min · Domain I)
- [Watch 'AIGP v2.1 Full Course Update Explained' (what changed in v2.1)](https://www.youtube.com/watch?v=cmWGspcCdkc) (`watch` · 45 min · Domain All · **stretch (optional)**)

#### Thursday 24 Sep 2026 (105 min core)
- [Diagnostic part 1: AI Career Pro free practice exam, untimed; mark every guess](https://governance.aicareer.pro/course/aigp-exam-prep) (`practice` · 40 min · Domain All · 🏁 **Diagnostic**)
- [Diagnostic part 2: IAPP free study guide sample questions](https://iapp.org/l/aigp-study-guide-request) (`practice` · 20 min · Domain All)
- Start a gap log: tag every miss and guess by BoK competency; rank the four domains weakest to strongest (`review` · 15 min · Domain All)
- [Buy the AI Career Pro AIGP Exam Prep course ($99) if the trial lessons and questions felt IAPP-like (else see the plan's budget section for the alternative)](https://governance.aicareer.pro/course/aigp-exam-prep) (`practice` · 10 min · Domain All · 🏁 **Buy course (AI Career Pro, $99)**)
- Set up your Anki deck; add the first 15 cards from diagnostic misses (`flashcards` · 20 min · Domain All)

#### Friday 25 Sep 2026 (100 min core)
- [Course: Domain I.B lessons (roles and responsibilities, governance committees, cross-functional collaboration, AI literacy and training)](https://governance.aicareer.pro/course/aigp-exam-prep) (`watch` · 45 min · Domain I)
- [Course: Domain I.B quiz questions; add every miss to Anki](https://governance.aicareer.pro/course/aigp-exam-prep) (`practice` · 20 min · Domain I)
- [Read EU AI Act Article 4 (AI literacy duty)](https://artificialintelligenceact.eu/article/4/) (`read` · 10 min · Domain I)
- Lab 1 (NovaPay): sketch NovaPay's AI governance structure: committee, owners, RACI for approving a new AI use case (`practice` · 25 min · Domain I)

#### Saturday 26 Sep 2026 (105 min core)
- [Course: Domain I.C lessons (policies and procedures across the AI lifecycle)](https://governance.aicareer.pro/course/aigp-exam-prep) (`watch` · 45 min · Domain I)
- [Course: Domain I.C quiz questions; add misses to Anki](https://governance.aicareer.pro/course/aigp-exam-prep) (`practice` · 20 min · Domain I)
- Lab 2 (NovaPay): draft a 1-page AI use policy + an AI inventory template (fields: owner, purpose, data, vendor, risk tier, status) (`practice` · 40 min · Domain I)
- [Read NIST AI RMF Playbook GOVERN 1-6 and compare with your Lab 1-2 drafts](https://airc.nist.gov/airmf-resources/playbook/govern/) (`read` · 45 min · Domain I · **stretch (optional)**)
- [Listen: AIGP Audio Course Ep. 11, privacy, security, data-governance and IP policies for AI (I.C.2)](https://open.spotify.com/episode/3ca2ImW1KV6MZ8gH1WFwU3) (`watch` · 30 min · Domain I · **stretch (optional)**)

#### Sunday 27 Sep 2026 (REST)
- Rest day: no study.

#### Monday 28 Sep 2026 (110 min core)
- [Course: Domain II.A lessons (privacy and data protection law applied to AI)](https://governance.aicareer.pro/course/aigp-exam-prep) (`watch` · 45 min · Domain II)
- [Course: Domain II.A quiz questions; add misses to Anki](https://governance.aicareer.pro/course/aigp-exam-prep) (`practice` · 20 min · Domain II)
- [Read GDPR Article 22 (automated individual decision-making, incl. profiling)](https://gdpr-info.eu/art-22-gdpr/) (`read` · 15 min · Domain II)
- [Read GDPR Article 35 (DPIA: when required, minimum contents); you'll use it in Lab 6](https://gdpr-info.eu/art-35-gdpr/) (`read` · 15 min · Domain II)
- Anki: GDPR articles that matter for AI (5, 6, 13, 22, 35) in one line each (`flashcards` · 15 min · Domain II)
- [Read GDPR Articles 5 and 6 (principles, lawful bases) for AI training data](https://gdpr-info.eu/art-5-gdpr/) (`read` · 30 min · Domain II · **stretch (optional)**)

#### Tuesday 29 Sep 2026 (115 min core)
- [Course: Domain II.B lessons (IP, anti-discrimination, consumer protection, product liability)](https://governance.aicareer.pro/course/aigp-exam-prep) (`watch` · 40 min · Domain II)
- [Course: Domain II.B quiz questions; add misses to Anki](https://governance.aicareer.pro/course/aigp-exam-prep) (`practice` · 20 min · Domain II)
- [Read FTC 'Operation AI Comply' (Section 5 deception/unfairness applied to AI claims)](https://www.ftc.gov/business-guidance/blog/2024/09/operation-ai-comply-continuing-crackdown-overpromises-ai-related-lies) (`read` · 20 min · Domain II)
- [Read NYC DCWP page on Local Law 144 (AEDT bias audits, candidate notice)](https://www.nyc.gov/site/dca/about/automated-employment-decision-tools.page) (`read` · 15 min · Domain II)
- Week 1 recap: Anki review + teach-back: explain Domain I out loud in 5 minutes (voice memo), then check against your notes (`review` · 20 min · Domain I)
- [Read Veronica Lin's 'How I passed the AIGP exam' (what worked, what didn't)](https://aigouvernance.com/how-i-passed-the-aigp-exam-what-actually-worked-what-didnt/) (`read` · 15 min · Domain All · **stretch (optional)**)

### Week 2: Course: II.C-II.D (EU AI Act, standards) and III.A-III.C (governing development), plus EU AI Act lab
**2026-09-30 → 2026-10-06 · Core 11.2 h · Stretch 2.2 h · Total if all done 13.4 h · Domains II, III**

#### Wednesday 30 Sep 2026 (125 min core)
- [Course: Domain II.C lessons (EU AI Act and other AI-specific laws)](https://governance.aicareer.pro/course/aigp-exam-prep) (`watch` · 55 min · Domain II)
- [Course: Domain II.C quiz questions; add misses to Anki](https://governance.aicareer.pro/course/aigp-exam-prep) (`practice` · 20 min · Domain II)
- [Read the EU AI Act high-level summary: risk tiers, provider vs deployer duties, GPAI](https://artificialintelligenceact.eu/high-level-summary/) (`read` · 30 min · Domain II)
- [Read EU AI Act Article 5 (the prohibited practices)](https://artificialintelligenceact.eu/article/5/) (`read` · 20 min · Domain II)

#### Thursday 01 Oct 2026 (110 min core)
- [Course: Domain II.D lessons (NIST AI RMF, ISO/IEC 42001 and 42005, OECD, other frameworks)](https://governance.aicareer.pro/course/aigp-exam-prep) (`watch` · 45 min · Domain II)
- [Course: Domain II.D quiz questions; add misses to Anki](https://governance.aicareer.pro/course/aigp-exam-prep) (`practice` · 20 min · Domain II)
- [Read the AIRC AI RMF Core page: Govern/Map/Measure/Manage and their category IDs](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) (`read` · 30 min · Domain II)
- Anki: NIST functions + categories; ISO 42001 (management system) vs 42005 (impact assessment) (`flashcards` · 15 min · Domain II)
- [Watch 'NIST AI RMF deep dive: GOVERN vs MAP vs MEASURE vs MANAGE'](https://www.youtube.com/watch?v=IbKXHfkFcBQ) (`watch` · 30 min · Domain II · **stretch (optional)**)

#### Friday 02 Oct 2026 (95 min core)
- [Course: Domain III.A lessons (governing design and build: use-case intake, impact assessment, requirements)](https://governance.aicareer.pro/course/aigp-exam-prep) (`watch` · 45 min · Domain III)
- [Course: Domain III.A quiz questions; add misses to Anki](https://governance.aicareer.pro/course/aigp-exam-prep) (`practice` · 20 min · Domain III)
- [Read NIST AI RMF Playbook MAP 1-5 (the design-stage checklist); skim, note 5 actions NovaPay should take](https://airc.nist.gov/airmf-resources/playbook/map/) (`read` · 30 min · Domain III)
- [Read Model Cards for Model Reporting (Mitchell et al.): the model-card sections](https://arxiv.org/abs/1810.03993) (`read` · 25 min · Domain III · **stretch (optional)**)

#### Saturday 03 Oct 2026 (120 min core)
- [Lab 3 (NovaPay): run the EU AI Act Compliance Checker on 5 NovaPay systems (credit scoring, CV screening, customer chatbot, fraud detection, AI-generated marketing video); record the risk tier and NovaPay's role for each](https://artificialintelligenceact.eu/assessment/eu-ai-act-compliance-checker/) (`practice` · 45 min · Domain II)
- [Check your Lab 3 answers against EU AI Act Article 6 (high-risk classification, incl. Art 6(3) derogation) and Annex III](https://artificialintelligenceact.eu/article/6/) (`read` · 30 min · Domain II)
- [Read EU AI Act Article 3 definitions (provider, deployer, importer, distributor) and fix any role you got wrong in Lab 3](https://artificialintelligenceact.eu/article/3/) (`read` · 15 min · Domain II)
- [Week 2 recap: Anki review + drill 20 OpenExamPrep questions (Domains I-II)](https://open-exam-prep.com/practice/aigp) (`practice` · 30 min · Domain All)
- [Watch 'AIGP How They Passed - July 2026' (v2.1-era candidate panel)](https://www.youtube.com/watch?v=rdASQWETQyY) (`watch` · 45 min · Domain All · **stretch (optional)**)

#### Sunday 04 Oct 2026 (REST)
- Rest day: no study.

#### Monday 05 Oct 2026 (110 min core)
- [Course: Domain III.B lessons (data governance, training and testing, bias and fairness)](https://governance.aicareer.pro/course/aigp-exam-prep) (`watch` · 45 min · Domain III)
- [Course: Domain III.B quiz questions; add misses to Anki](https://governance.aicareer.pro/course/aigp-exam-prep) (`practice` · 20 min · Domain III)
- [Read EU AI Act Article 10 (data and data governance)](https://artificialintelligenceact.eu/article/10/) (`read` · 20 min · Domain III)
- [Lab 4 (NovaPay): answer 10 key questions from Datasheets for Datasets for NovaPay's credit-scoring training data](https://arxiv.org/abs/1803.09010) (`practice` · 25 min · Domain III)

#### Tuesday 06 Oct 2026 (110 min core)
- [Course: Domain III.C lessons (testing, release readiness, monitoring and maintenance during development)](https://governance.aicareer.pro/course/aigp-exam-prep) (`watch` · 45 min · Domain III)
- [Course: Domain III.C quiz questions; add misses to Anki](https://governance.aicareer.pro/course/aigp-exam-prep) (`practice` · 20 min · Domain III)
- [Read NIST AI RMF Playbook MEASURE 1-4 (metrics, TEVV, bias, feedback); skim the eval parts you know from BlueDot](https://airc.nist.gov/airmf-resources/playbook/measure/) (`read` · 30 min · Domain III)
- Anki: Domain III lifecycle stages and the artefact produced at each (intake form, impact assessment, datasheet, model card, test report) (`flashcards` · 15 min · Domain III)
- [Read OWASP Top 10 for LLM Applications 2025: LLM01-LLM10 titles + mitigations](https://genai.owasp.org/resource/owasp-top-10-for-llm-applications-2025/) (`read` · 30 min · Domain III · **stretch (optional)**)

### Week 3: Course: IV.A-IV.C (governing deployment), Mock #1, book the exam, EU AI Act high-risk deep dive
**2026-10-07 → 2026-10-13 · Core 12.6 h · Stretch 0.5 h · Total if all done 13.1 h · Domains IV, II, All**

#### Wednesday 07 Oct 2026 (115 min core)
- [Course: Domain IV.A lessons (deciding whether and how to deploy, incl. agentic AI)](https://governance.aicareer.pro/course/aigp-exam-prep) (`watch` · 45 min · Domain IV)
- [Course: Domain IV.A quiz questions; add misses to Anki](https://governance.aicareer.pro/course/aigp-exam-prep) (`practice` · 20 min · Domain IV)
- [Read Singapore Model AI Governance Framework for Agentic AI: agent risks and controls sections](https://www.imda.gov.sg/-/media/imda/files/about/emerging-tech-and-research/artificial-intelligence/mgf-for-agentic-ai.pdf) (`read` · 30 min · Domain IV)
- [Read EU AI Act Article 26 (obligations of deployers of high-risk AI)](https://artificialintelligenceact.eu/article/26/) (`read` · 20 min · Domain IV)

#### Thursday 08 Oct 2026 (115 min core)
- [Course: Domain IV.B lessons (assessments, third-party/vendor due diligence, contracts)](https://governance.aicareer.pro/course/aigp-exam-prep) (`watch` · 45 min · Domain IV)
- [Course: Domain IV.B quiz questions; add misses to Anki](https://governance.aicareer.pro/course/aigp-exam-prep) (`practice` · 20 min · Domain IV)
- [Read IAPP: 'EU model contractual clauses for AI procurement: a practical guide'](https://iapp.org/news/a/eu-model-contractual-clauses-for-ai-procurement-a-practical-guide) (`read` · 25 min · Domain IV)
- Lab 5 (NovaPay): write a 12-question vendor due-diligence questionnaire for buying a third-party CV-screening tool (`practice` · 25 min · Domain IV)

#### Friday 09 Oct 2026 (110 min core)
- [Course: Domain IV.C lessons (post-deployment monitoring, incidents, decommissioning)](https://governance.aicareer.pro/course/aigp-exam-prep) (`watch` · 45 min · Domain IV)
- [Course: Domain IV.C quiz questions; add misses to Anki](https://governance.aicareer.pro/course/aigp-exam-prep) (`practice` · 20 min · Domain IV)
- [Read NIST AI RMF Playbook MANAGE 1-4 (risk response, third-party risk, monitoring, incident communication); skim](https://airc.nist.gov/airmf-resources/playbook/manage/) (`read` · 30 min · Domain IV)
- Anki: deployer duties, vendor contract terms, incident steps (`flashcards` · 15 min · Domain IV)

#### Saturday 10 Oct 2026 (185 min core)
- [FULL MOCK #1: AI Career Pro Mock 1, 100 Qs, timed 165 min, no notes (target >=60% overall, >=55% on III and IV)](https://governance.aicareer.pro/course/aigp-exam-prep) (`practice` · 165 min · Domain All · 🏁 **First practice exam | 50% of plan**)
- Score Mock #1 by domain; update the gap log; apply the decision rule (keep 27 Oct or move to 10 Nov?) (`review` · 20 min · Domain All)

#### Sunday 11 Oct 2026 (REST)
- Rest day: no study.

#### Monday 12 Oct 2026 (110 min core)
- [BOOK THE EXAM (gated on Mock #1): >=60% and >=55% on III/IV -> book Tue 27 Oct 2026; otherwise book fallback Tue 10 Nov 2026. Book via the IAPP AIGP page, then Pearson VUE (morning slot, or take the afternoon off)](https://iapp.org/certify/aigp) (`review` · 15 min · Domain All · 🏁 **Book exam by (gated on Mock #1)**)
- [Review every Mock #1 item (right and wrong): write why each distractor is wrong](https://governance.aicareer.pro/course/aigp-exam-prep) (`review` · 75 min · Domain All)
- Anki: a card for every Mock #1 miss (`flashcards` · 20 min · Domain All)

#### Tuesday 13 Oct 2026 (120 min core)
- [Read EU AI Act Chapter III Section 2 (Arts 8-15 high-risk requirements): Arts 9 risk management, 11 documentation, 12 logs, 13 transparency](https://artificialintelligenceact.eu/section/3-2/) (`read` · 40 min · Domain II)
- [Read EU AI Act Article 14 (human oversight)](https://artificialintelligenceact.eu/article/14/) (`read` · 15 min · Domain III)
- Lab 6a (NovaPay): high-risk checklist for the credit-scoring model: map each of Arts 9-15 to an owner and an artefact (`practice` · 30 min · Domain III)
- [Read the AI Act implementation timeline: ORIGINAL dates](https://artificialintelligenceact.eu/implementation-timeline/) (`read` · 15 min · Domain II)
- [Read Morgan Lewis on the Digital Omnibus: NEW dates (Annex III to 2 Dec 2027, Annex I to 2 Aug 2028); make a two-column date card](https://www.morganlewis.com/pubs/2026/06/eu-approves-delays-and-other-amendments-to-certain-eu-ai-act-obligations-what-businesses-should-know) (`read` · 20 min · Domain II)
- [Read IAPP Top 10 EU AI Act: 'Understanding and assessing risk'](https://iapp.org/resources/article/top-impacts-eu-ai-act-understanding-assessing-risk) (`read` · 30 min · Domain II · **stretch (optional)**)

### Week 4: Applied deep dive: FRIA/DPIA lab, GDPR and US laws, Mock #2, standards, post-market
**2026-10-14 → 2026-10-20 · Core 11.9 h · Stretch 2.3 h · Total if all done 14.2 h · Domains II, III, IV**

#### Wednesday 14 Oct 2026 (100 min core)
- [Read EU AI Act Article 25 (value chain: when a deployer becomes a provider)](https://artificialintelligenceact.eu/article/25/) (`read` · 20 min · Domain II)
- [Read EU AI Act Article 27 (fundamental rights impact assessment)](https://artificialintelligenceact.eu/article/27/) (`read` · 20 min · Domain IV)
- Lab 6b (NovaPay): mini FRIA + DPIA for deploying the CV-screening tool (use the Art 27 and GDPR Art 35 headings; 1 page) (`practice` · 45 min · Domain IV)
- Anki: provider vs deployer vs 'deemed provider'; FRIA vs DPIA (`flashcards` · 15 min · Domain II)
- [Complete Canada's Algorithmic Impact Assessment tool for the same CV-screening scenario and compare](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/algorithmic-impact-assessment.html) (`practice` · 40 min · Domain IV · **stretch (optional)**)

#### Thursday 15 Oct 2026 (95 min core)
- [Read ICO Guidance on AI and data protection: accountability, lawfulness, fairness and transparency sections](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/guidance-on-ai-and-data-protection/) (`read` · 40 min · Domain II)
- [Read EDPB Opinion 28/2024 executive summary (model anonymity, legitimate-interest 3-step test)](https://www.edpb.europa.eu/system/files/2024-12/edpb_opinion_202428_ai-models_en.pdf) (`read` · 25 min · Domain II)
- [Read GDPR Article 13 (incl. 'meaningful information about the logic involved')](https://gdpr-info.eu/art-13-gdpr/) (`read` · 15 min · Domain II)
- [Course: re-do the II.A quiz questions you missed the first time](https://governance.aicareer.pro/course/aigp-exam-prep) (`practice` · 15 min · Domain II)
- [Read ICO: 'How do we ensure individual rights in our AI systems?'](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/guidance-on-ai-and-data-protection/how-do-we-ensure-individual-rights-in-our-ai-systems/) (`read` · 30 min · Domain II · **stretch (optional)**)

#### Friday 16 Oct 2026 (95 min core)
- [Read McDermott: Colorado SB24-205 blocked, replaced by SB26-189 (eff. 1 Jan 2027); keep the developer/deployer duty-of-care concepts](https://www.mcdermottlaw.com/insights/colorado-ai-law-in-flux-comprehensive-replacement-bill-signed-after-federal-court-blocks-predecessors-enforcement/) (`read` · 20 min · Domain II)
- [Read Wittliff Cutter: Texas TRAIGA, the Colorado reset and federal preemption (2026)](https://www.wittliffcutter.com/news-insights/ai-regulation-texas-colorado-federal-2026) (`read` · 15 min · Domain II)
- [Read FPF on South Korea's AI Framework (Basic) Act (new in v2.1)](https://fpf.org/blog/south-koreas-new-ai-framework-act-a-balancing-act-between-innovation-and-regulation/) (`read` · 20 min · Domain II)
- [Read EU AI Act Article 50 (transparency: chatbots, synthetic content, deepfakes) and Article 99 penalty tiers](https://artificialintelligenceact.eu/article/50/) (`read` · 25 min · Domain II)
- Teach-back: 5-minute voice memo on 'which AI laws apply to NovaPay in the EU and US, and why' (`review` · 15 min · Domain II)
- [Read the Dec 2025 White House EO on a national AI policy framework (state-law preemption)](https://www.whitehouse.gov/presidential-actions/2025/12/eliminating-state-law-obstruction-of-national-artificial-intelligence-policy/) (`read` · 20 min · Domain II · **stretch (optional)**)

#### Saturday 17 Oct 2026 (185 min core)
- [FULL MOCK #2: AI Career Pro Mock 2, timed 165 min (target >=70% overall, no domain <65%; >=75% counts toward the booking rule)](https://governance.aicareer.pro/course/aigp-exam-prep) (`practice` · 165 min · Domain All · 🏁 **Second practice exam**)
- Score Mock #2 by domain; update the gap log; pick the two weakest competencies for Week 5 (`review` · 20 min · Domain All)

#### Sunday 18 Oct 2026 (REST)
- Rest day: no study.

#### Monday 19 Oct 2026 (125 min core)
- [Review every Mock #2 item: why each distractor is wrong](https://governance.aicareer.pro/course/aigp-exam-prep) (`review` · 60 min · Domain All)
- [Buy the IAPP official AIGP practice exam (~$50-60, price unverified); confirm the store page references BoK v2.1](https://store.iapp.org/aigp-practice-exam-digital/) (`practice` · 10 min · Domain All · 🏁 **Buy IAPP practice exam**)
- [Read ISMS.online on ISO 42001 Annex A controls (A.2-A.10 objectives)](https://www.isms.online/iso-42001/annex-a-controls/) (`read` · 30 min · Domain II)
- [Lab 7: using the NIST AI RMF to ISO/IEC 42001 crosswalk, build a 1-page table: NIST function -> 42001 clause -> NovaPay artefact](https://airc.nist.gov/docs/NIST_AI_RMF_to_ISO_IEC_42001_Crosswalk.pdf) (`practice` · 25 min · Domain II)
- [Skim the ISO/IEC 42005 to NIST AI RMF crosswalk](https://airc.nist.gov/documents/2/ai-2025-00108_ISO_IEC_42005_to_NIST_AI_RMF_Crosswalk.pdf) (`read` · 15 min · Domain II · **stretch (optional)**)

#### Tuesday 20 Oct 2026 (115 min core)
- [Read IAPP Top 10 EU AI Act: 'Post-market monitoring, information sharing and enforcement'](https://iapp.org/resources/article/top-impacts-eu-ai-act-post-market-monitoring-sharing-enforcement) (`read` · 30 min · Domain III)
- [Read EU AI Act Article 43 (conformity assessment routes) as a release gate](https://artificialintelligenceact.eu/article/43/) (`read` · 15 min · Domain III)
- Lab 8 (NovaPay): 1-page monitoring and incident plan for the credit-scoring model (drift trigger, owner, serious-incident reporting, decommissioning) (`practice` · 25 min · Domain IV)
- [Course: rewatch the lessons for your two weakest competencies from Mock #2](https://governance.aicareer.pro/course/aigp-exam-prep) (`watch` · 25 min · Domain All)
- Week 4 recap: cumulative Anki review (all decks) (`flashcards` · 20 min · Domain All)
- [Read IAPP Top 10 EU AI Act: 'AI assurance across the risk categories'](https://iapp.org/resources/article/top-impacts-eu-ai-act-ai-assurance-risk-categories) (`read` · 35 min · Domain III · **stretch (optional)**)

### Week 5: Consolidation and exam week: Mock #3, IAPP official practice exam, go/no-go, exam Tue 27 Oct
**2026-10-21 → 2026-10-27 · Core 14.2 h · Stretch 1.0 h · Total if all done 15.2 h · Domains All, IV, III**

#### Wednesday 21 Oct 2026 (180 min core)
- [FULL MOCK #3: AI Career Pro Mock 3, timed 165 min (target >=75% overall, no domain <65-70%). Block a long evening](https://governance.aicareer.pro/course/aigp-exam-prep) (`practice` · 165 min · Domain All)
- Score Mock #3 by domain and compare with Mock #2 (`review` · 15 min · Domain All)

#### Thursday 22 Oct 2026 (85 min core)
- [Review Mock #3 misses; rewatch the course lessons for the 3 most-missed competencies](https://governance.aicareer.pro/course/aigp-exam-prep) (`review` · 45 min · Domain All)
- Gap closure: redo your weakest NovaPay lab (default Lab 5 vendor questionnaire) using what the mocks taught you (`practice` · 30 min · Domain IV)
- [Early go/no-go check on Mocks #2 and #3. If the handbook's reschedule cut-off falls before Sun 25 Oct, decide today](https://iapp.org/certify/candidate-handbook) (`review` · 10 min · Domain All)
- [Read AIGP Playbook reference sheets and checklists (impact assessments, vendor review)](https://aigpplaybook.com/resources/) (`review` · 20 min · Domain IV · **stretch (optional)**)

#### Friday 23 Oct 2026 (80 min core)
- [Course: take 40 mixed questions from the course bank you haven't seen, timed (~1.5 min each)](https://governance.aicareer.pro/course/aigp-exam-prep) (`practice` · 60 min · Domain All)
- [Run the OnVUE system check on the exam computer (>=48 h ahead) or confirm the test-centre route; re-read the handbook's ID and room rules](https://iapp.org/certify/candidate-handbook) (`review` · 20 min · Domain All)
- [Watch 'Top 3 Tips to Pass Your AIGP Exam on the First Try'](https://www.youtube.com/watch?v=0muZy8Pcxks) (`watch` · 20 min · Domain All · **stretch (optional)**)

#### Saturday 24 Oct 2026 (180 min core)
- [IAPP OFFICIAL AIGP PRACTICE EXAM: timed 165 min, exam conditions (target >=70-75%)](https://store.iapp.org/aigp-practice-exam-digital/) (`practice` · 165 min · Domain All · 🏁 **IAPP official practice exam**)
- Score the IAPP practice exam by domain (`review` · 15 min · Domain All)

#### Sunday 25 Oct 2026 (20 min core)
- [GO/NO-GO: Mocks #2 and #3 both >=75% with no domain <65-70%, AND IAPP practice >=70-75%? Yes: keep Tue 27 Oct. No: reschedule to Tue 10 Nov (if still inside the handbook cut-off) and run the 2-week extension](https://iapp.org/certify/candidate-handbook) (`review` · 20 min · Domain All · 🏁 **Ready to book exam**)
- Optional 20-min Anki pass (due cards only) (`flashcards` · 20 min · Domain All · **stretch (optional)**)

#### Monday 26 Oct 2026 (125 min core)
- [Review every IAPP practice-exam miss: note the qualifier (FIRST/BEST/MOST) and the lifecycle stage each item hinged on](https://store.iapp.org/aigp-practice-exam-digital/) (`review` · 50 min · Domain All)
- Build your one-page cram sheet: AI Act dates (both schedules), penalty tiers, Art 5 bans, Annex III areas, impact-assessment types (DPIA/FRIA/conformity/42005/AEDT audit) (`review` · 35 min · Domain All)
- [Read the AIGP Playbook exam-day revision sheet (100 essential facts by domain); star any fact you can't explain. Then stop; early night](https://aigpplaybook.com/aigp-exam-revision.html) (`review` · 30 min · Domain All)
- Prepare: ID matching registration, clear desk/room (OnVUE), alarm, route (`review` · 10 min · Domain All)

#### Tuesday 27 Oct 2026 (180 min core)
- [Light: re-skim only your cram sheet and the starred facts (max 20 min)](https://aigpplaybook.com/aigp-exam-revision.html) (`review` · 15 min · Domain All)
- [SIT THE AIGP EXAM: 100 Qs, 165 min (+ optional 15-min break; review flagged first-half items BEFORE the break)](https://iapp.org/certify/aigp) (`practice` · 165 min · Domain All · 🏁 **Exam day**)

## 7. Exam-week checklist

**By Fri 23 Oct (≥48 h before)**
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

## 8. Budget

All study materials in the plan are free except the practice exams. The research could not verify prices marked *unverified*; check them at purchase.

| Item | Cost (USD) | Status | When to buy | Link |
|---|---|---|---|---|
| **Prep course:** AI Career Pro AIGP Exam Prep (117 video lessons with written + audio versions, 700+ Qs, 5 full v2.1 mocks) | **$99** | **Core: the course spine for weeks 1–3 and the Mock #1–#3 bank** | Thu 24 Sep, after the free trial on Wed 23 Sep | [governance.aicareer.pro](https://governance.aicareer.pro/course/aigp-exam-prep) |
| *Alternative to the above:* Kyle David AIGP Masterclass (Udemy; 19–20 h of video; one listing says v2.1, July 2026, another still says v2.0.1) plus one Udemy v2.1 question bank | Udemy sale prices *unverified* (usually $15–25 each) | Only if the AI Career Pro trial doesn't suit you. It's longer (20 h), so it would replace, not add to, the course steps | Thu 24 Sep | [udemy.com/course/aigp-masterclass](https://www.udemy.com/course/aigp-masterclass/) |
| IAPP official AIGP practice exam (digital) | ~$50–60 *(unverified)* | Core | Mon 19 Oct (the plan uses it Sat 24 Oct) | [store.iapp.org](https://store.iapp.org/aigp-practice-exam-digital/) |
| **AIGP exam fee** | **$799** non-member / $649 member (membership ≈ $295/yr, *unverified*, so non-member is cheaper unless you want membership anyway) | Core | Mon 12 Oct (after Mock #1) | [IAPP AIGP page](https://iapp.org/certify/aigp) |
| Optional second teacher: Kyle David AIGP Masterclass (Udemy, video-only) | Udemy sale price *unverified* (usually $15–25) | **Conditional**: only if Mock #1 is <60% or <55% on III/IV and a second explanation would help. Confirm the page says v2.1. Keeps total course spend ≤ $150 | Mon 12 Oct (after Mock #1) | [udemy.com/course/aigp-masterclass](https://www.udemy.com/course/aigp-masterclass/) |
| Retake fee (contingency) | $625 non-member / $475 member | Only if needed | — | — |

**Expected spend: ≈ $799 + $99 + ~$55 ≈ $953** (non-member). Course spend is $99, inside your $150 cap (≈ $120 even with the optional Udemy second teacher on sale). The worst case adds a $625 retake. The free resources are the BoK, IAPP glossary/trackers/Top-10 series, the AIGP Playbook, NIST/ICO/EDPB/EUR-Lex/artificialintelligenceact.eu, OpenExamPrep and Anki.

## 9. Caveats

- **Links:** every task link comes from `research/resources.json`. Study links are all `verified: true` entries, meaning the exact URL appeared in a live web search on 2026-09-23; the sandbox could not open the pages. The practice-exam links (AI Career Pro, AIGP Playbook preview, OpenExamPrep, IAPP store) come from the `practiceExams` section, which has no per-entry `verified` flag; research §5 lists them as Recommend/Optional. The four `verified: false` GDPR URLs (Arts 9, 14, 15, 25 on gdpr-info.eu) are not used.
- **BoK wording:** the research could not open the BoK v2.1 PDF, so the competency wording is reconstructed. Day 1's BoK read is where you correct the plan's domain tags if the PDF differs.
- **Hours:** the estimates rest on weak evidence. This 5-week version has no buffer week. If Mocks #1–#2 are weak, move to 10 Nov early rather than cramming.
- **AI Career Pro course:** its lesson counts, v2.1 alignment and $99 price come from the vendor's own pages (search results on 2026-09-23). The research found no independent reviews, so the free trial on Day 1 is your check: if it doesn't click, switch to the alternative in §8 on Day 2. The per-day lesson times (~45 min per sub-domain) are estimates (117 videos × ~5 min ≈ 10 h across 13 sub-domains).
