# AIGP Exam Research Report

*Research Agent (1 of 3). Generated 2026-09-23. Companion data file: `research/resources.json`.*

> **Read this first: how the evidence was gathered.** Everything here came from live web searches on 2026-09-23. The sandbox's egress proxy blocked `curl` and `WebFetch` to every target host (iapp.org, contentstack (BoK PDF host), nist.gov, eur-lex, artificialintelligenceact.eu, youtube, medium, linkedin, udemy and others). Two consequences:
> 1. **No link could be HTTP-status-checked.** A link marked "verified" means the exact URL came back in a live search result on 2026-09-23, which is strong evidence that it exists. It does not prove the page opens without a login or paywall. A few URLs are pattern-inferred and are marked "unverified".
> 2. **Reddit could not be searched at all.** The search tool's crawler is blocked from reddit.com, and old.reddit.com was also blocked. The candidate evidence below therefore comes from blogs, Medium, Substack, LinkedIn snippets and YouTube titles only.
>
> I could not open the BoK v2.1 PDF itself. Its version, dates and domain question ranges agree across several independent secondary sources. The competency wording for each domain is reconstructed and should be checked against the PDF.

---

## 1. Exam Facts

| Item | Value | Confidence / source |
|---|---|---|
| **BoK version** | **v2.1** (file `AIGP_BOK_2.1.0_FINAL.pdf`) | High [1][2][3] |
| BoK approved | 9 Sep 2025 by the AIGP Exam Development Board. It supersedes v2.0.1 | High [2] |
| **BoK effective** | **2 Feb 2026**, for exams taken on or after that date | High [1][2][4] |
| Did the BoK change recently? | **Yes, twice.** v1.0 (2023–24, 7 domains) was replaced by v2.0.1 (Feb 2025, 4 domains), which was replaced by v2.1 (Feb 2026, same 4 domains, recalibrated). **Treat any resource with 6–7 domains as obsolete. Treat anything not mentioning v2.1 as suspect for new topics.** | High |
| No newer version announced? | No v2.2 or 2027 BoK found in search on 2026-09-23. Re-check iapp.org before booking. | Medium |
| Questions | **100** (**85 scored + 15 unscored pilot**, mixed in and indistinguishable) | High [7][9][15] |
| Format | Multiple choice, mostly single-answer. One Jan-2026 passer reported 2–3 multi-select items [15]. About 30% of questions are tied to case-study scenarios (third-party claim [9]). | Medium |
| **Time** | **2 h 45 min (165 min) testing time**, plus an optional 15-min break at the halfway point. If you take the break, the first half is submitted and locked. That makes a ~3 h appointment. | Medium-High [7][9]. Some sources say "3 hours" (break included). One vendor's "90 Q / 2.5 h" appears wrong. |
| **Scoring** | Scaled **100–500; 300 = pass**. Each scored item is worth 1 point. Raw scores are converted to the scale to equalise forms, so **300 ≠ 60%**. No penalty for wrong answers, so never leave a blank. | High [8][15] |
| **Fee** | **US$649 member / US$799 non-member** | High, consistent across sources incl. IAPP store snippet [7] |
| **Retake fee** | **US$475 member / US$625 non-member**. Wait ≥7 days between attempts (store snippet; confirm in the Handbook). | Medium-High [7] |
| Membership | ≈US$295/yr. It saves $150 on the exam and covers certification maintenance. | Medium (unverified on iapp.org) |
| Delivery | Pearson VUE test centre or **OnVUE** online proctoring | High |
| Pass rate | **IAPP does not publish pass rates** [32]. Vendor figures of "45–55% first attempt" are unsourced; ignore them. | High that it is unpublished |

### Domains and weights (BoK v2.1)

IAPP publishes a **minimum–maximum number of scored questions** per domain, not percentages [3]. The approximate percentages below are midpoints / 85.

| Domain | Scored Qs (min–max) | ≈ Weight | Competencies (reconstructed; verify against PDF) |
|---|---|---|---|
| **I. Understanding the foundations of AI governance** | 16–20 | ~21% | I.A What AI is and why it needs governance (definitions, types, risks and harms). I.B Establish and communicate organisational expectations (roles, cross-functional collaboration, training / AI literacy). I.C Establish policies and procedures across the AI lifecycle (privacy, security, data governance **and IP** policies, third parties). I.C is the heaviest competency in Domain I at ~6–8 Qs [31]. |
| **II. Understanding how laws, standards and frameworks apply to AI** | 19–23 | ~25% | II.A Privacy law applied to AI (GDPR etc.). II.B Other existing laws (IP, anti-discrimination, consumer protection, product liability). II.C EU AI Act main elements, **plus other enacted AI laws** such as South Korea's AI Basic Act in v2.1 [4][5][30]. II.D Industry standards and tools (OECD, NIST AI RMF, ISO/IEC 42001, **ISO/IEC 42005** newly named) [5][30]. |
| **III. Understanding how to govern AI development** | 21–25 | ~27% | III.A Govern design and build of the AI system. III.B Govern collection and use of data for training and testing. III.C Govern release, monitoring and maintenance. |
| **IV. Understanding how to govern AI deployment and use** | 21–25 | ~27% | IV.A Evaluate factors and risks in the decision to deploy: business objectives, performance requirements, data availability, ethics, workforce readiness; deployment options incl. **agentic architectures**. IV.B Perform key assessment activities (impact assessments, vendor due diligence, contracts). IV.C Govern deployment and use (monitoring, incidents, secondary use, decommissioning). **IV.C is reportedly the single heaviest competency** [31]. |

**What changed in v2.1** [4][5][6][30]:
- "AI models" became "AI **systems**" throughout, so governance covers the whole system, its supply chain and its downstream uses.
- Provider responsibilities are made explicit.
- More weight on legal basis and transparency, fundamental rights impact assessments (FRIA), third-party AI risk and IP governance. I.C.2 now covers IP policies.
- Other national AI laws are included, e.g. South Korea.
- ISO/IEC 42005 is named.
- Agentic architectures are added.

**Current-law caveat (important):**
- **EU AI Act.** The **EU Digital Omnibus on AI** has been in force since **27 Jul 2026** [25][26]. It deferred Annex III high-risk obligations to **2 Dec 2027** and Annex I (product-embedded) obligations to **2 Aug 2028**. BoK v2.1 was approved in Sep 2025, before the Omnibus, so exam items may still assume the original dates (2 Aug 2026 / 2 Aug 2027). Learn both, and answer from the concept (who must do what), not the calendar.
- **Colorado AI Act (SB24-205).** Its enforcement was blocked in federal court in Apr 2026, and it was replaced by SB26-189 (narrower, effective 1 Jan 2027) [27]. The developer/deployer duty-of-care concepts remain exam-relevant.

### Free official IAPP materials

The official free baseline set is: the BoK v2.1 PDF, the Candidate Handbook, the Certification FAQs, the free AIGP study guide (with sample Qs), the Key Terms glossary, the Global AI Law & Policy Tracker plus jurisdiction overviews, the US State AI Governance Tracker, the "Top 10 operational impacts of the EU AI Act" series, IAPP news explainers (EDPB Opinion 28/2024, EU model contractual clauses), and the AI Governance Profession / In Practice reports. URLs are in §4 and in resources.json.

Caution: the direct FSG PDF (`pages.iapp.org/.../AIGP FSG.pdf?version=3`) is described in some snippets with the old 6/7-domain structure. Request the current guide through the form and check that it shows 4 domains.

---

## 2. What Passed Candidates Recommend

### Candidate reports found (last ~18 months unless flagged)

Reddit was inaccessible, so there are only 14 reports and several of them are thin. LinkedIn post bodies are behind a login; where only the title or a snippet was visible, that is stated. Dates for LinkedIn posts were decoded from activity IDs.

| # | Who / where | Date | BoK era | Method & resources | Hours / duration | Practice exams | Surprises / tips |
|---|---|---|---|---|---|---|---|
| 1 | Veronica Lin, aigouvernance.com + LinkedIn [15] | Passed end Jan 2026; post Feb 2026 (LinkedIn 16 Apr 2026) | v2.0.1 | Dr Kyle David AIGP course (paid ~€180, Nov 2025) was "the main reason I passed". Plain-language, builds understanding; good for non-technical people. | "Around two months, mostly after work". Hours not stated. | 2 practice exams bundled in the course | Treat all 100 Qs seriously (the 15 pilots are hidden). Scenario-heavy, application not definitions. 2–3 multi-select Qs. Scaled scoring. |
| 2 | Joe Sabado, Substack [16] | 29 Jun 2026 | **v2.1** | **BoK/blueprint as "the spine": study nothing that doesn't map to it.** For each sub-topic, find material and move on only when you can explain it plainly. Used AI as a research partner. Already works in AI governance (UC AI Council). | Not stated | Not specified | **Avoid brain dumps.** |
| 3 | Nathan Chappell, Medium [17] | 31 Oct 2025 | v2.0.1 | Studied with a partner. Shared notes of focus areas and practice Qs, used between calls / on flights. Chief AI Officer, so experienced. | Not stated | Practice Qs (source unspecified) | Framed it as "translating experience into validation". |
| 4 | Ammett W, startcloudnow (Medium) [18] | 27 Jan 2026 | v2.0.1 | IAPP official online training (modules + reference material). Works with AI systems daily. | Not stated | Not stated | Check the exam fits your goals first. Use the official material. |
| 5 | Donna Gallaher, FAIR Institute (failed) [19] | ~Oct 2025 | v2.0.1 | Risk-management practitioner | n/a | n/a | **Failed.** The exam rewards "utopian" ideal-governance answers over pragmatic business trade-offs, has a legal-perspective bias, and gives no feedback on wrong answers. **Lesson: answer as the textbook governance function would, not as a pragmatic operator.** |
| 6 | Barbora Studihrad, LinkedIn article | 2025 | v2.0.1 | "How I Passed the Updated AIGP Exam in 2025: Study Resources". Body behind login. | unknown | unknown | unknown |
| 7 | Prabh Nair, LinkedIn article | unknown | unknown | "How I cleared AIGP". Body behind login. | unknown | unknown | unknown |
| 8 | Philipa Farley, LinkedIn post | 9 May 2025 | v2.0.1 | Snippet: "Passed the AIGP exam this morning. The practice…" (truncated) | unknown | Mentions practice (truncated) | unknown |
| 9 | Caiky Avellar, LinkedIn post | 11 Jun 2025 | v2.0.1 | "How I passed the AIGP certification with AI tools". Published study notes. | unknown | unknown | unknown |
| 10 | Kyle David "How They Passed", 3 recent grads (YouTube) | 5 Feb 2026 | v2.0.1 | Panel of his students. **Vendor-hosted, not neutral.** | unknown | His course mocks | Not reviewed (video not accessible) |
| 11 | Kyle David "How They Passed – July 2026" (YouTube) | 6 Jul 2026 | **v2.1** | As above | unknown | unknown | Not reviewed |
| 12 | "How to Pass the AIGP Exam Without an Official Textbook" (YouTube) | 22 Aug 2025 | v2.0.1 | First-attempt passer's strategy with no official textbook | unknown | unknown | Not reviewed |
| 13 | Oliver Patel (IAPP AIGP faculty) [20] | Passed 2024; guide Feb 2025 | v1.0 (old) | Built a free 100-link resource guide mapped to the BoK, plus "Top 10 tips" (Jul 2024) | n/a | n/a | Older, but the author is authoritative |
| 14 | Julian Pedraza, LinkedIn "AIGP Exam Analysis" + "Usual and Unusual Study Resources" | ~2024–25 | likely v1.0 | Body behind login | unknown | unknown | unknown |

**Honest bottom line.** Only 5 reports (#1–5) have readable substance, and **none states total study hours.** The consistent themes are:
1. Use the BoK as the checklist.
2. The exam is scenario/application-based, and many candidates were surprised by that.
3. Practice questions are essential, used from early on as a diagnostic.
4. Don't use braindumps.
5. Choose the "ideal governance process" answer.
6. The only named paid resource with independent praise is Kyle David's course.

---

## 3. BoK coverage vs. your BlueDot background

This is based on BlueDot unit descriptions: Frontier AI Governance has 6 units (state of play at the frontier, actors/power mapping, competing governance approaches, stress-testing, open-weights debate, career planning). AGI Strategy covers the race to AGI, drivers of progress, the threat landscape, transition strategies and contributing. I did not review BlueDot readings in depth.

| Rating | BoK areas | Why |
|---|---|---|
| **Strong** | I.A (AI types, capabilities, risks and harms, societal/catastrophic). GenAI risk taxonomy (NIST AI 600-1 concepts). II.C *GPAI / systemic-risk* provisions and the GPAI Code of Practice at a high level. Global policy landscape (US federal stance, EU, UK, China, CoE treaty, OECD). III.C evals / red-teaming / system cards. IV.A open vs closed deployment debates. | Core BlueDot content |
| **Partial** | I.B *why* governance and stakeholder mapping (BlueDot works at state/lab level, not enterprise). II.D OECD principles (known), NIST AI RMF (known by name, probably not at category level). | Different altitude |
| **Weak (your assumption confirmed)** | **I.B/I.C enterprise program mechanics:** committees, RACI, AI inventory, policies, training, third-party and IP policy updates. **II.A GDPR applied to AI:** lawful basis, purpose limitation, DPIA triggers, Art 22, data subject rights, EDPB Op. 28/2024. **II.B non-privacy law:** IP/copyright, anti-discrimination, FTC Section 5, product liability. **II.C high-risk EU AI Act detail:** Art 6 + Annex III classification, provider duties (Arts 9–17) vs deployer duties (Art 26), Art 25 role shifts, FRIA (Art 27), Art 50 transparency, conformity/registration, penalty tiers, timelines. **II.D standards:** ISO/IEC 42001 (AIMS, Annex A), 42005, 23894; NIST AI RMF categories. **III.A–B lifecycle:** use-case intake, impact assessment, data lineage/quality/bias testing, documentation (model cards, datasheets). **IV.B vendor due diligence and contracts. IV.C monitoring, incidents, secondary use, decommissioning.** **US state/local:** Colorado, NYC LL144, Texas TRAIGA. **Other jurisdictions:** Korea, Canada ADM directive, China GenAI measures, Singapore frameworks. | Not covered by BlueDot |

**Implication.** Domains III and IV are ~54% of scored items. With II.A–II.C detail, they should get ~70% of study time.

**Watch your instincts.** BlueDot trains strategic, frontier-risk reasoning. AIGP rewards the organisation-level, process-correct governance step: document, assess, consult stakeholders, follow the policy, escalate. The FAIR Institute failure report [19] is exactly this trap.

---

## 4. Resource Library

Ratings are 1–5. All costs are free unless noted. "Updated" is the source's date where known. Link status is covered in the header note: every link below appeared in a live search on 2026-09-23, except where marked *(unverified)*. The full list, including more granular links, is in `resources.json` (≈180 entries with `bokSubtopics` tags).

### 4.1 Official IAPP

| Name | Link | Format | Cost | BoK | Updated | Rating | Notes |
|---|---|---|---|---|---|---|---|
| AIGP BoK v2.1 PDF | https://assets.contentstack.io/v3/assets/bltd4dd5b2d705252bc/blt579bac3f0b35f278/69494b068965be6043ba2815/AIGP_BOK_2.1.0_FINAL.pdf | PDF | free | all | eff. 2026-02-02 | 5 | The syllabus. Alt: https://assets.contentstack.io/v3/assets/bltd4dd5b2d705252bc/blt0d33152fd20bc134/AIGP_Cert%20BOK.pdf |
| AIGP cert page | https://iapp.org/certify/aigp | web | free | all | live | 5 | Hub |
| Candidate Handbook | https://iapp.org/certify/candidate-handbook | web/PDF | free | logistics | live | 5 | OnVUE rules, retakes, confidentiality |
| Certification FAQs | https://iapp.org/certify/faqs | web | free | logistics | live | 4 | Scoring |
| Free AIGP study guide (form) | https://iapp.org/l/aigp-study-guide-request | PDF | free | all | check 4-domain | 4 | Sample Qs |
| Key Terms for AI Governance | https://iapp.org/resources/ai-governance-glossary | glossary | free | I | 2025–26 | 5 | IAPP's own vocabulary |
| Global AI Law & Policy Tracker | https://iapp.org/resources/article/global-ai-legislation-tracker | web | free | II.C | 2026-02-03 | 5 | Jurisdictions |
| US State AI Gov. Tracker | https://iapp.org/resources/article/us-state-ai-governance-legislation-tracker | web | free | II | live | 4 | |
| Top 10 impacts of EU AI Act (hub) | https://iapp.org/resources/article/top-impacts-eu-ai-act | articles | free | II.C | 2024–25 | 5 | Sub-pages: scope, risk, GPAI, assurance, post-market (see JSON) |
| EDPB on AI models (IAPP) | https://iapp.org/news/a/edpb-weighs-in-on-key-questions-on-personal-data-in-ai-models | article | free | II.A | 2024-12 | 4 | |
| EU MCCs for AI procurement (IAPP) | https://iapp.org/news/a/eu-model-contractual-clauses-for-ai-procurement-a-practical-guide | article | free | IV.A/B | 2025 | 4 | Vendor terms |

**Top 3 (official):**
1. **BoK v2.1.** It defines what is examinable.
2. **Key Terms glossary.** Exam wording follows IAPP vocabulary.
3. **Global AI Law & Policy Tracker + Top-10 EU AI Act series.** These are IAPP-authored framings of Domain II.

### 4.2 Primary sources: laws and frameworks

| Name | Link | Format | Cost | BoK | Updated | Rating | Notes |
|---|---|---|---|---|---|---|---|
| EU AI Act (EUR-Lex OJ) | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ%3AL_202401689 | law | free | II.C | 2024-07 | 5 | Original text |
| EU AI Act consolidated (post-Omnibus) | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A02024R1689-20260727 | law | free | II.C | 2026-07-27 | 4 | New dates |
| AI Act high-level summary | https://artificialintelligenceact.eu/high-level-summary/ | article | free | II.C | 2024 | 5 | Best single read |
| AI Act Art. 3 / 5 / 6 / Annex III | https://artificialintelligenceact.eu/article/3/ · /article/5/ · /article/6/ · /annex/3/ | law | free | II.C | — | 5 | Definitions, prohibitions, classification |
| AI Act Arts 9, 10, 14 (+ §3-2 overview) | https://artificialintelligenceact.eu/article/9/ · /article/10/ · /article/14/ · /section/3-2/ | law | free | II.C, III | — | 5 | Provider requirements |
| AI Act Arts 25, 26, 27 | https://artificialintelligenceact.eu/article/25/ · /article/26/ · /article/27/ | law | free | II.C, IV | — | 5 | Value chain, deployers, FRIA |
| AI Act Arts 4, 50, 51, 53, 99 | https://artificialintelligenceact.eu/article/4/ · /article/50/ · /article/51/ · /article/53/ · /article/99/ | law | free | II.C | — | 5 | Literacy, transparency, GPAI, fines |
| AI Act Arts 2, 43, 47, 49 | https://artificialintelligenceact.eu/article/2/ · /article/43/ · /article/47/ · /article/49/ | law | free | II.C, III.C | — | 4 | Scope, conformity, registration |
| GDPR Arts 5, 6, 13, 22, 35 | https://gdpr-info.eu/art-5-gdpr/ · /art-6-gdpr/ · /art-13-gdpr/ · /art-22-gdpr/ · /art-35-gdpr/ | law | free | II.A | — | 5 | Arts 9, 14, 15, 25 follow the same pattern *(unverified)*. Ch. 3: https://gdpr-info.eu/chapter-3/ |
| EDPB Opinion 28/2024 | https://www.edpb.europa.eu/system/files/2024-12/edpb_opinion_202428_ai-models_en.pdf | PDF | free | II.A | 2024-12 | 4 | Exec summary only |
| ICO Guidance on AI & data protection | https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/guidance-on-ai-and-data-protection/ | guidance | free | II.A, III.B | live | 5 | Best practitioner explanation |
| NIST AI RMF 1.0 | https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf | framework | free | II.D | 2023 (revision pending) | 5 | 7 trustworthiness traits + core |
| NIST AI RMF Core (HTML) | https://airc.nist.gov/airmf-resources/airmf/5-sec-core/ | framework | free | II.D | — | 5 | |
| NIST Playbook Govern / Map / Measure / Manage | https://airc.nist.gov/airmf-resources/playbook/govern/ · /map/ · /measure/ · /manage/ | framework | free | I–IV | live | 5 | Suggested actions |
| NIST AI 600-1 GenAI Profile | https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf | framework | free | II.D | 2024-07 | 4 | 12 risks |
| NIST RMF ↔ ISO 42001 crosswalk | https://airc.nist.gov/docs/NIST_AI_RMF_to_ISO_IEC_42001_Crosswalk.pdf | PDF | free | II.D | 2024 | 4 | Free route into 42001 |
| ISO 42005 ↔ NIST crosswalk | https://airc.nist.gov/documents/2/ai-2025-00108_ISO_IEC_42005_to_NIST_AI_RMF_Crosswalk.pdf | PDF | free | II.D, IV.B | 2025 | 4 | New in v2.1 |
| ISO/IEC 42001 / 42005 (abstracts) | https://www.iso.org/standard/42001 · https://www.iso.org/standard/42005 | web | free page | II.D | — | 4 | Don't buy the standards |
| ISO 42001 Annex A explained | https://www.isms.online/iso-42001/annex-a-controls/ | article | free | II.D | 2025–26 | 4 | A.2–A.10 objectives |
| OECD AI Principles | https://oecd.ai/en/ai-principles | framework | free | II.D, I | 2024-05 | 5 | 5 principles + 5 recs |
| CoE Framework Convention (CETS 225) | https://rm.coe.int/1680afae3c | treaty | free | II.C | 2024-09 | 4 | Entry into force **unverified** |
| Colorado SB24-205 | https://leg.colorado.gov/bills/sb24-205 | law | free | II.B/C | replaced 2026 | 4 | Status: https://www.mcdermottlaw.com/insights/colorado-ai-law-in-flux-comprehensive-replacement-bill-signed-after-federal-court-blocks-predecessors-enforcement/ |
| NYC LL144 (AEDT) | https://www.nyc.gov/site/dca/about/automated-employment-decision-tools.page | law | free | II.B | live | 5 | Bias audits |
| FTC Operation AI Comply | https://www.ftc.gov/business-guidance/blog/2024/09/operation-ai-comply-continuing-crackdown-overpromises-ai-related-lies | guidance | free | II.B | 2024-09 | 4 | |
| White House EO Dec 2025 (state preemption) | https://www.whitehouse.gov/presidential-actions/2025/12/eliminating-state-law-obstruction-of-national-artificial-intelligence-policy/ | EO | free | II.C | 2025-12 | 3 | EO 14110 was revoked Jan 2025 |
| S. Korea AI Basic Act (FPF) | https://fpf.org/blog/south-koreas-new-ai-framework-act-a-balancing-act-between-innovation-and-regulation/ | article | free | II.C | 2025 | 4 | In force 22 Jan 2026 |
| Canada ADM Directive + AIA tool | https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/algorithmic-impact-assessment.html | tool | free | II.C, IV.B | live | 4 | |
| China GenAI Interim Measures (EN) | https://www.chinalawtranslate.com/en/generative-ai-interim/ | law | free | II.C | 2023 | 3 | |
| Singapore GenAI Model Framework | https://aiverifyfoundation.sg/wp-content/uploads/2024/05/Model-AI-Governance-Framework-for-Generative-AI-May-2024-1-1.pdf | framework | free | II | 2024-05 | 3 | Agentic MGF also in JSON |
| Model Cards / Datasheets | https://arxiv.org/abs/1810.03993 · https://arxiv.org/abs/1803.09010 | papers | free | III | 2018 | 4 | Documentation artefacts |
| OWASP Top 10 for LLM 2025 | https://genai.owasp.org/resource/owasp-top-10-for-llm-applications-2025/ | framework | free | III.C, IV.C | 2024-11 | 3 | |

**Top 3 (primary):**
1. **EU AI Act via artificialintelligenceact.eu**: high-level summary plus Arts 3, 5, 6, 9–15, 25–27, 50, 53, 99 and Annex III. Your biggest point gain.
2. **NIST AI RMF 1.0 + Playbook** (Govern/Map/Measure/Manage). It organises Domains III–IV.
3. **GDPR Arts 5, 6, 13, 22, 35 + ICO AI guidance**, for II.A.

### 4.3 Free study guides and notes

| Name | Link | Format | Cost | BoK | Updated | Rating | Notes |
|---|---|---|---|---|---|---|---|
| AIGP Playbook: domain training notes | https://aigpplaybook.com/training.html (D1: /aigp-domain-1.html, D2: /aigp-domain-2.html) | slide notes + knowledge checks | free | all | 2026 (v2.1) | 4 | Independent practitioner; includes "exam traps" |
| Oliver Patel: Unofficial AIGP Resource Guide | https://oliverpatel.substack.com/p/the-unofficial-aigp-resource-guide | reading list (100 links) | free | all | 2025-02 | 5 | IAPP faculty; mapped to pre-v2.1 BoK |
| AIGP Playbook: exam-day revision (100 facts) | https://aigpplaybook.com/aigp-exam-revision.html | cram sheet | free | all | 2026 | 4 | Final 48 h |
| Training Camp: v2.1 learning path | https://trainingcamp.com/articles/how-to-study-for-the-aigp-a-learning-path-built-around-the-bok-v2-1-blueprint/ | article | free | all | 2026 | 4 | Vendor blog |
| Training Camp: AIGP ↔ EU AI Act / NIST / ISO mapping | https://trainingcamp.com/articles/how-aigp-maps-to-the-eu-ai-act-nist-ai-rmf-and-iso-42001/ | article | free | II | 2026 | 4 | |
| AIGP Playbook: study guide / weekly plan | https://aigpplaybook.com/aigp-study-guide/ | guide | free | all | 2026 | 4 | |
| InfosecTrain / FlashGenius / PSG: v2.1 change summaries | https://www.infosectrain.com/blog/whats-new-in-the-aigp-2026-exam · https://flashgenius.net/blog-article/navigating-the-aigp-2026-bok-update-the-shift-from-models-to-systems · https://privacystudygroup.com/aigp-2026-update/ | articles | free | all | 2026 | 3 | |
| lmakoti GitHub AIGP study guide | https://github.com/lmakoti/ai_governance_professional_iapp/blob/main/AIGP%20Study%20Guide.pdf | notes | free | all | unknown | 2 | Likely pre-v2.1; **suspect** |
| Captain Compliance free guide | (7-domain, v1) | slides | free | — | old | 1 | **Drop: obsolete BoK** |

**Top 3 (guides):**
1. **AIGP Playbook domain notes**: v2.1-structured and free.
2. **Oliver Patel's guide**: authoritative curation.
3. **AIGP Playbook exam-revision sheet**.

### 4.4 Flashcards

| Name | Link | Cost | Rating | Notes |
|---|---|---|---|---|
| Build your own Anki deck from the IAPP glossary + EU AI Act articles | https://iapp.org/resources/ai-governance-glossary | free | 5 | Recommended: no trustworthy pre-made v2.1 deck found |
| Quizlet: AIGP Exam Flashcards | https://quizlet.com/1085612395/aigp-exam-flash-cards/ | free | 2 | User-made; terminology only |
| Brainscape: AIGP Definitions (user deck) | https://www.brainscape.com/packs/aigp-definitions-22228332 | free | 2 | User-made |

### 4.5 Video (YouTube)

| Name | Link | Date | Rating | Notes |
|---|---|---|---|---|
| AIGP v2.1 Full Course Update Explained | https://www.youtube.com/watch?v=cmWGspcCdkc | 2026-02-02 | 4 | What changed in v2.1 |
| AIGP How They Passed, July 2026 (Kyle David) | https://www.youtube.com/watch?v=rdASQWETQyY | 2026-07-06 | 3 | Most recent candidate panel (vendor-hosted) |
| AIGP Success: 3 recent grads (Kyle David) | https://www.youtube.com/watch?v=1oxoujLLALk | 2026-02-05 | 3 | Vendor-hosted |
| NIST AI RMF deep dive: Govern vs Map vs Measure vs Manage | https://www.youtube.com/watch?v=IbKXHfkFcBQ | 2026-03-01 | 3 | Function discrimination |
| NIST AI RMF: A Practical Guide | https://www.youtube.com/watch?v=3B0ELJTViMs | 2026-03-21 | 3 | |
| Understanding the EU AI Act: Roles, Risks, Compliance | https://www.youtube.com/watch?v=mpSWJP-LGEE | 2026-02 | 3 | |
| EU AI Act Article 3 Explained | https://www.youtube.com/watch?v=5us83jc1-6I | 2025-12 | 3 | |
| Top 3 Tips to Pass AIGP on the First Try | https://www.youtube.com/watch?v=0muZy8Pcxks | 2025-12-15 | 3 | |
| How to Pass AIGP Without an Official Textbook | https://www.youtube.com/watch?v=Vak8vBRa5FM | 2025-08-22 | 3 | |
| AIGP Full Course (playlist) | https://www.youtube.com/playlist?list=PLboJ9yx0c_SVAS8yUnczrktK5PuB_MT22 | unknown | 3 | Author unverified; spot-check vs BoK |
| "AIGP Lectures Domain 1 to 7" (playlist) | https://www.youtube.com/playlist?list=PLMKPofCI5XFdAZ7DSHe9EZYmslzDcLqb3 | old | 1 | **Avoid: v1 BoK** |

**Top 3 (video):**
1. **v2.1 update explainer**.
2. **How They Passed – July 2026**, the only v2.1-era candidate panel.
3. **AIGP Full Course playlist**, as a supplement only. No video could be watched, so these ratings are provisional.

### 4.6 Interactive tools

| Name | Link | Rating | Use |
|---|---|---|---|
| EU AI Act Compliance Checker | https://artificialintelligenceact.eu/assessment/eu-ai-act-compliance-checker/ | 5 | Run 5–6 invented scenarios (HR screening, chatbot, credit scoring, emotion recognition at work) to drill role + risk tier |
| Canada Algorithmic Impact Assessment tool | https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/algorithmic-impact-assessment.html | 4 | Hands-on impact assessment (IV.B) |
| ICO AI & data protection risk toolkit | https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/guidance-on-ai-and-data-protection/ai-and-data-protection-risk-toolkit/ | 4 | Risk-assessment template |
| AI Act Explorer | https://artificialintelligenceact.eu/ai-act-explorer/ | 5 | Navigation |
| AI Act implementation timeline | https://artificialintelligenceact.eu/implementation-timeline/ | 5 | Dates |

**Top 3 (interactive):**
1. **Compliance Checker**.
2. **Canada AIA tool**.
3. **ICO toolkit**.

### 4.7 Podcasts

| Name | Link | Rating | Notes |
|---|---|---|---|
| Certified: The IAPP AIGP Audio Course (Bare Metal Cyber) | https://podcasts.apple.com/us/podcast/certified-the-iapp-aigp-audio-course/id1890735004 | 4 | Episode titles track v2.1 performance indicators (e.g., Ep 11 on privacy/security/data-governance/IP policies: https://open.spotify.com/episode/3ca2ImW1KV6MZ8gH1WFwU3). Good for commutes. Quality not independently reviewed. |
| The Privacy Advisor Podcast (IAPP) | https://podcasts.apple.com/us/podcast/the-privacy-advisor-podcast/id1095382766 | 3 | Background only |
| EU AI Act Newsletter (Substack) | https://artificialintelligenceact.substack.com/p/the-eu-ai-act-newsletter-63-standards | 3 | News, optional |

**Top 3 (audio):**
1. **Bare Metal Cyber AIGP Audio Course**.
2. **Privacy Advisor Podcast**.
3. **EU AI Act Newsletter**, which is text, not audio.

---

## 5. Practice Exam Assessment

For almost every third-party bank there is **no independent evidence of closeness to the real exam**. One Udemy vendor's own description admits earlier AIGP banks were criticised as "too easy, too repetitive, nothing like the real exam" [34]. Treat third-party scores as optimistic.

| Option | Price | Qs | Expl. | BoK | Verdict | Reasoning |
|---|---|---|---|---|---|---|
| **IAPP official AIGP Practice Exam** (https://store.iapp.org/aigp-practice-exam-digital/) | **Unverified**: ~$50–60 per third parties [11] | 100 (PDF) | Yes | "Same BoK as exam"; v2.1 refresh **not verified** | **Recommend** | Only IAPP-written items, so it is the best style signal. Use as the final calibration. Check that the store page says v2.1 before buying. |
| IAPP free study-guide sample Qs | free | few | ? | check 4-domain | **Recommend** | Day-1 diagnostic |
| AI Career Pro AIGP Exam Prep ($99) (https://governance.aicareer.pro/course/aigp-exam-prep) | $99 | 700+ incl. 5×100 mocks | claimed | v2.1 (claimed) | **Optional** | Only affordable v2.1 package with full mocks. The author passed AIGP and is an ex-AWS/Microsoft governance lead. **No independent reviews.** Try its free Domain I-A + free practice exam first. |
| AIGP Playbook mock (15-Q free preview) + Question of the Week | preview free | 300+ bank | yes | v2.1 (claimed) | **Optional** | Free scenario practice. Accuracy unknown. |
| OpenExamPrep (https://open-exam-prep.com/practice/aigp) | free | 200 | claimed | v2.1 (claimed) | **Optional** | Free drilling volume. Don't use its score to judge readiness. |
| Sybex Study Guide (Gregory) + online test bank | **unverified** (book) | 2 mocks + review Qs | yes | 2025 + v2.1 supplement | **Optional** | Reputable publisher. Borrow from a library to keep the $0 budget. |
| Udemy "6 Full Tests, 600 Qs" (Mr ExamMaster) | unverified (Udemy sale) | 600 | claimed | v2.1 (claimed) | **Optional** | If you buy **one** Udemy bank, pick one whose recent reviews mention v2.1 and closeness to the real exam |
| Udemy "AIGP Certification Practice" (rebuilt Summer 2026, 800 Qs) | unverified | 800 | claimed | v2.1 (claimed) | **Optional** | Recent rebuild; unreviewed |
| Other Udemy banks (500-Q, 2026 edition, "All 4 Domains" 800+, 300 unofficial, Vol 1/2) | unverified | 300–800 | varies | unverified | **Avoid** | No quality evidence; likely AI-generated; redundant |
| 22Academy AIGP 4-Tests Package | unverified | 200 | yes | v2.1 (claimed) | **Optional** | Established IAPP-prep firm. Price and reviews unknown. |
| Dr Kyle David site version (600 Qs + flashcards) | ~€180 (Nov 2025) | 600 | yes | v2.1 (Jul 2026) | **Optional (over budget)** | Best independent evidence of any paid product |
| **Braindump sites** (ExamTopics, CertEmpire "real exam questions", Pass4Success, ITExams, CertsHero, Study4Exam, P2PExams, CertShield, DumpsGate) | varies | — | often wrong | — | **Avoid** | Breaches IAPP confidentiality (certification can be revoked). Answers are unreliable. Passers explicitly warn against them [16]. |
| IAPP official training | ~$995+ | — | — | v2.1 | **Excluded (> $150)** | Not required |

**Suggested practice stack**
- **Free:** IAPP samples, AIGP Playbook preview/QotW, OpenExamPrep.
- **Paid:** the **IAPP official practice exam** is the one purchase to make. Add **one** v2.1 third-party bank only if needed: AI Career Pro ($99, after its free trial) or a well-reviewed Udemy bank bought on sale.

---

## 6. Prep Course Verdict (≤ $150)

**Verdict: none required.** No 2025–26 evidence is strong enough to justify a paid course for this candidate.

The best-evidenced course is **Dr Kyle David's AIGP Masterclass**. Its evidence is:
- one detailed first-person report (V. Lin, passed Jan 2026: "main reason I passed");
- a ~4.7★ rating from ~1.8k ratings on Udemy (search snippet);
- vendor-hosted testimonial videos.

That is suggestive, not strong. Its full version (~€180) is also over budget.

**Conditional fallback:**
- **Trigger:** mock #1 (at ~25 h) comes in under ~60% overall, or under 55% on Domains III/IV.
- **Option:** the **Udemy video-only version** (https://www.udemy.com/course/aigp-masterclass/), bought on sale. The price is unverified, but Udemy sale prices are far below $150.
- **Before buying:** one snippet said the Udemy page covers v2.0.1 with in-place updates promised. Confirm it now says **v2.1**.
- **Alternative:** AI Career Pro ($99). It has no independent reviews, so try its free sample first.

---

## 7. Readiness Thresholds

**Evidence quality: low to moderate.** No passer report stated total hours. The figures below triangulate:
- IAPP's "at least 30 hours" recommendation, reported secondhand [2]. I could not confirm it on iapp.org.
- Vendor guides: 40–60 h for privacy-certified people with AI exposure, 80–120 h for newcomers [13], and 60–120 h generally [12].
- One passer: "~2 months mostly after work" [15].

| Metric | Value |
|---|---|
| Typical total hours (passers) | **Median ≈ 55 h, range ≈ 40–80 h.** Cold career-changers can need 100+ h. |
| This user (strong frontier/policy context, weak operational/legal detail) | **~50–65 h ≈ 5 weeks at 12 h/week**, plus a 1-week buffer. Background saves time on I.A and GPAI/policy but not on Domains II–IV detail, which are most of the exam. |
| Diagnostic | **At ~3 h**, after reading the BoK: IAPP sample Qs + a free 15–25-Q set, untimed. Purpose: learn the style and rank the domains. Several sources recommend practice from Week 1 [15]. |
| **First full-length timed mock** | **At ~25 h**, after one pass through all 4 domains. 100 Qs, 165 min, no notes. |
| Mock #2 | ~40 h, from a different bank |
| IAPP official practice exam | ~50 h, timed. Treat it as the calibration test. |
| **Target to book** | **≥75% on two consecutive full-length v2.1-aligned third-party mocks, no domain below ~65–70%, AND ≥70–75% on the IAPP official practice exam.** You should also be able to explain why each distractor is wrong. |
| Caveat | IAPP publishes no mapping from practice % to the 300 cut. The widely repeated "consistent 75%+" is community/vendor guidance. Vendor tables like "80%+ → 85% pass" are unsourced marketing [14]. |

**Common failure reasons** [15][19] plus vendor guides:
- Treating the exam as memorisation or law-only, then under-studying Domains III–IV (~54%).
- The reverse: technical people under-studying EU AI Act detail (risk classification, prohibited practices, high-risk obligations).
- Getting provider vs deployer roles wrong, and missing the Art 25 role flip.
- Choosing the pragmatic business answer instead of the "ideal governance process" answer.
- Using old-BoK or low-quality banks and being overconfident from inflated scores.
- Fatigue and time pressure on long scenarios.
- OnVUE technical problems.

---

## 8. Pitfalls & Exam-Day Tips

**Question strategy**
- Watch qualifiers such as **FIRST, BEST, MOST appropriate, PRIMARY**. Several options are often "true"; pick the one that fits the lifecycle stage and the role.
- For each scenario, ask:
  1. Who is the actor (provider, deployer, importer, controller, processor)?
  2. What lifecycle stage is it (design, data, release, deploy, monitor, retire)?
  3. What does the governance process require next?
- Default to process-correct actions: assess, document, involve stakeholders, follow or update policy, escalate.
- No penalty for guessing. Answer everything and flag items for review.

**Time management**
- 165 min for 100 Qs is about 1.65 min per question.
- Aim to finish the first half in about 75 min. If you take the optional 15-min break, first-half answers lock, so review flagged items **before** the break.

**Content traps**
- **EU AI Act dates.** Know the original schedule and the 2026 Omnibus deferrals. Apply the concept.
- **Colorado.** The law was blocked and replaced (SB26-189, effective 2027). The concept is still testable.
- **US federal policy.** EO 14110 was revoked (Jan 2025). There is a Dec 2025 EO on state-law preemption.
- **Impact assessments.** Distinguish DPIA (GDPR Art 35), FRIA (AI Act Art 27), conformity assessment (AI Act Art 43), algorithmic/AI impact assessments (ISO 42005, Canada AIA) and bias audits (NYC LL144).

**OnVUE (online proctoring)**
- Run the system check well ahead (≥48 h) and do a full dry run the day before.
- You need a walled room with the door closed, a clear desk, no second monitor, and no one entering.
- Don't talk or read aloud.
- Study groups report scroll glitches, webcam failures, proctor queues and small text. If you have a reliable test centre, it removes that risk.

**Logistics**
- ID must match your registration exactly. The exam must be taken within 1 year of purchase.
- The retake wait is ≥7 days (verify), and the retake fee is $475 / $625.

---

## 9. Sources

1. AIGP BoK v2.1 PDF (IAPP; titled "VERSION 2.1 Effective date: 2 February 2026"), https://assets.contentstack.io/v3/assets/bltd4dd5b2d705252bc/blt579bac3f0b35f278/69494b068965be6043ba2815/AIGP_BOK_2.1.0_FINAL.pdf (approved 2025-09-09). Seen in search only; not opened.
2. Privacy Bootcamp, "New 2026 AIGP Body of Knowledge version 2.1", https://www.privacybootcamp.com/Resources/Article/aigp-body-of-knowledge-2026 (2025–26)
3. Training Camp, "How to Study for the AIGP: A Learning Path Built Around the BoK v2.1 Blueprint", https://trainingcamp.com/articles/how-to-study-for-the-aigp-a-learning-path-built-around-the-bok-v2-1-blueprint/ (2026)
4. FlashGenius, "Navigating the AIGP 2026 BoK Update", https://flashgenius.net/blog-article/navigating-the-aigp-2026-bok-update-the-shift-from-models-to-systems (2026)
5. InfosecTrain, "What's New in the AIGP 2026 Exam?", https://www.infosectrain.com/blog/whats-new-in-the-aigp-2026-exam (2026)
6. Privacy Study Group, "AIGP 2026 Update", https://privacystudygroup.com/aigp-2026-update/ (2026)
7. IAPP Store, AIGP Exam, https://store.iapp.org/aigp-exam/ (search snippet, 2026-09-23)
8. Privacy Bootcamp, "What is a Passing Score on IAPP Exams", https://www.privacybootcamp.com/Resources/Article/What-Is-a-Passing-Score-on-IAPP-Exams (n.d.)
9. InfosecTrain, "AIGP Exam Preparation Guide", https://www.infosectrain.com/blog/aigp-exam-preparation-guide (2025–26)
10. IAPP Store, AIGP Practice Exam Digital, https://store.iapp.org/aigp-practice-exam-digital/ (2026-09-23)
11. Training Camp, "AIGP Certification: What It Costs…", https://trainingcamp.com/articles/aigp-certification-what-it-costs-what-it-pays-and-who-should-get-it/ (2026)
12. aigptest.com, "How Long to Study for the AIGP Exam" (vendor), https://aigptest.com/blog/aigp-study-time (2026)
13. LearnZapp, "AIGP Certification Guide (2026)" (vendor), https://www.learnzapp.com/blog/aigp-certification-guide/ (2026)
14. Certsqill, "What AIGP Mock Scores Say About Readiness" (vendor), https://www.certsqill.com/blog/aigp-mock-scores/ (2026)
15. Veronica Lin, "How I passed the AIGP exam", https://aigouvernance.com/how-i-passed-the-aigp-exam-what-actually-worked-what-didnt/ (Feb 2026)
16. Joe Sabado, "I Used AI to Study for an AI Governance Exam…", https://joesabado.substack.com/p/i-used-ai-to-study-for-an-ai-governance (2026-06-29)
17. Nathan Chappell, Medium, https://medium.com/@nathanchappell/how-i-passed-the-aigp-exam-with-twelve-televisions-blaring-in-my-brain-2e4e7c7fbf3e (2025-10-31)
18. Ammett W, startcloudnow, https://blog.startcloudnow.com/preparing-for-success-with-the-iapp-aigp-ai-governance-professional-exam-2026-276e395109de (2026-01-27)
19. Donna Gallaher, FAIR Institute, "Why I Failed the AIGP Exam", https://www.fairinstitute.org/blog/why-i-failed-the-aigp-exam-and-you-should-too (~2025-10)
20. Oliver Patel, "The Unofficial AIGP Resource Guide", https://oliverpatel.substack.com/p/the-unofficial-aigp-resource-guide (2025-02)
21. Dr David Privacy, "DrDavidPrivacy vs Udemy", https://www.drdavidprivacy.com/drdavidprivacy-vs-udemy (2026)
22. Udemy, Kyle David AIGP Masterclass, https://www.udemy.com/course/aigp-masterclass/ (2026-09-23)
23. AI Career Pro, AIGP Exam Prep, https://governance.aicareer.pro/course/aigp-exam-prep (2026)
24. Wiley, Sybex IAPP AIGP Study Guide, https://www.wiley.com/en-us/IAPP+AIGP+Artificial+Intelligence+Governance+Professional+Study+Guide-p-9781394363940 (2025–26)
25. Gibson Dunn, "EU AI Act Omnibus Agreement", https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/ (2026)
26. EUR-Lex, consolidated AI Act 2026-07-27, https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A02024R1689-20260727
27. McDermott, "Colorado AI law in flux", https://www.mcdermottlaw.com/insights/colorado-ai-law-in-flux-comprehensive-replacement-bill-signed-after-federal-court-blocks-predecessors-enforcement/ (2026-05)
28. BlueDot Impact, Frontier AI Governance, https://bluedot.org/courses/ai-governance (2026)
29. BlueDot Impact, AGI Strategy, https://bluedot.org/courses/agi-strategy (2026)
30. YouTube, "AIGP v2.1 Full Course Update Explained", https://www.youtube.com/watch?v=cmWGspcCdkc (2026-02-02)
31. AIGP Playbook, exam revision / domain notes, https://aigpplaybook.com/aigp-exam-revision.html (2026)
32. aigptest.com, "AIGP Pass Rate 2026" (states IAPP doesn't publish rates), https://aigptest.com/blog/aigp-pass-rate (2026)
33. NIST, AI RMF page, https://www.nist.gov/itl/ai-risk-management-framework (live)
34. Udemy, "AI Governance Professional (AIGP) Certification Practice" description, https://www.udemy.com/course/aigp-exam-practice-tests/ (2026)

### Unverified / could-not-check list

- The BoK v2.1 PDF text itself (competency wording).
- The official practice exam price and whether it has been updated for v2.1.
- Udemy prices and ratings (except Kyle David's, which came from a snippet).
- The 22Academy test package price.
- The Sybex price.
- The retake wait period.
- The membership fee.
- CoE convention entry into force.
- The IAPP "30 hours" recommendation.
- gdpr-info.eu Art 9/14/15/25 URLs (pattern-inferred).
- All YouTube and podcast content quality (titles and dates only).
- All Reddit community evidence (inaccessible).

---

## Addendum (2026-09-23): prep course verdict revised for the candidate's learning style

**Why it changed.** The original verdict ("none required") assumed the candidate could learn from primary sources. The candidate has since said they need a course to introduce the topics and connect them, and that reading alone won't keep them motivated. Motivation and structure are real pass/fail factors, so a course is now **recommended**, within the $150 cap.

**Recommendation: AI Career Pro AIGP Exam Prep, $99. It was already in the plan as the mock-exam bank.**
- Vendor-stated contents: 117 video lessons (~5 min each) across 59 topics, mapped to BoK v2.1. Every lesson also has a written and an audio version. 700+ practice questions (a mix of knowledge and scenario questions) and 5 full 100-question mocks. The vendor also suggests a 13-day study plan, one sub-domain per day. [A1][A2]
- The instructor, James Kavanagh, led AI governance at Microsoft and Amazon and passed the AIGP. [A1][A3]
- An independent comparison site lists it in the same tier as the named-instructor video courses. [A3]
- **Buying it as the course costs nothing extra**: the plan already used its mocks. There is a free trial (Domain I-A plus a practice exam). [A1]
- **Caveat:** we found no independent learner reviews. The free trial on Day 1 is the check.

**Alternative (or optional second teacher): Dr Kyle David's AIGP Certification Masterclass on Udemy.**
- 19–20+ hours of video. [A4]
- It has the strongest independent evidence of any paid product (Veronica Lin, passed Jan 2026) [15].
- It's too long to run alongside the plan as a second full course. Use it instead of AI Career Pro if the trial doesn't suit you, or only for weak domains after Mock #1.
- **v2.1 status is conflicting:** one listing says "current to v2.1 (July 2026)", another says v2.0.1. [A4][A5] Check the Udemy page before buying.
- **Price:** Udemy sale price (not verified). The own-site version with 600 questions and flashcards probably costs more than $150 [A6].

**Budget check.** AI Career Pro ($99) plus the optional Udemy course on sale (≈ $15–25) ≈ $120, within the $150 cap.

Addendum sources (web search, 2026-09-23; the pages themselves could not be opened from the sandbox):
- A1. AI Career Pro, AIGP Exam Prep Course: https://governance.aicareer.pro/course/aigp-exam-prep
- A2. AI Career Pro, "How to Pass the AIGP Exam in 21 Days": https://governance.aicareer.pro/blog/aigp-in-21-days
- A3. aigovernance.study, "Best AIGP Exam Prep: Courses & Materials Compared (2026)": https://aigovernance.study/best-aigp-exam-prep/
- A4. OpenCourser listing, "AI Governance Professional (AIGP) Certification Masterclass" (Udemy): https://opencourser.com/course/y0mo9n/ai-governance-professional-aigp-certification-masterclass
- A5. Dr David Privacy, AIGP Certification Masterclass: https://www.drdavidprivacy.com/course/ai-governance-professional-aigp-certification-masterclass
- A6. Dr David Privacy, course catalogue: https://www.drdavidprivacy.com/courses
