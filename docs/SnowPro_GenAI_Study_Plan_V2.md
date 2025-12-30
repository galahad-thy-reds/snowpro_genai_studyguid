
# Mastering Snowflake GenAI for SnowPro Specialty Certification

_Last updated: Dec 26, 2025 (GMT‑6)_

This Udemy-style course prepares you for the **SnowPro Specialty: Gen AI Certification**. It blends domain-aligned lessons, detailed objectives, hands‑on labs, assignments, curated links (from official docs), and a capstone **Document Processing Framework (DPF)**.

---

## Course Structure & Time

| Domain | Weight | Suggested Time |
|---|---:|---:|
| **1.0 Snowflake for Gen AI Overview** | 26% | **3.0 h** |
| **2.0 Snowflake Gen AI & LLM Functions** | 40% | **4.5 h** |
| **3.0 Snowflake Gen AI Governance** | 22% | **2.0 h** |
| **4.0 Snowflake Document AI** | 12% | **1.5 h** |
| **Capstone (DPF Study Case)** | — | **2.0 h** |
| **Final Exam Prep** | — | **1.0 h** |

> Time budget echoes the original study plan and exam guide alignment.

---

## Section 1 — Introduction (30 min)

### Lessons & Objectives
- **What is Snowflake GenAI?**  
  **Objectives:** Explain Snowflake Cortex AI and how LLM/multimodal features run natively within Snowflake. List the primary capabilities: AISQL functions, Analyst, Search, Agents, Copilot.  
  **Reading (curated):**  
  - Snowflake Cortex AISQL (incl. LLM functions): https://docs.snowflake.com/en/user-guide/snowflake-cortex/aisql  
  - Cortex Analyst: https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst  
  - Cortex Search overview: https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-search/cortex-search-overview  
  - Cortex Agents: https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents  
  - Snowflake Copilot: https://docs.snowflake.com/en/user-guide/snowflake-copilot

- **Why this certification matters**  
  **Objectives:** Tie exam domains/subdomains to real team workflows (analytics, data engineering, ML/AI).  

- **Exam format, prerequisites, success tips**  
  **Objectives:** Review domain weights, practice-first approach, and staying current via official docs/release notes.  

- **Setting up your environment**  
  **Objectives:** Create roles/warehouses/stages; understand REST authentication (PAT/JWT/OAuth).  
  **Reading (curated):**  
  - Programmatic Access Tokens: https://docs.snowflake.com/en/user-guide/programmatic-access-tokens  
  - REST API Authentication: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/authentication

### Hands-on
- Sign in to **Snowsight** → **AI & ML Studio** → open **Cortex Playground**: https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-playground

---

## Section 2 — Domain 1.0: Snowflake for Gen AI Overview (3.0 h)

### Subdomains & Detailed Objectives

1. **Principles, Features & Best Practices**  
   **Objectives:** Differentiate Cortex components and where to use each (AISQL vs Analyst vs Search vs Agents vs Copilot).  
   **Reading:**  
   - AISQL (incl. LLM functions): https://docs.snowflake.com/en/user-guide/snowflake-cortex/aisql  
   - Cortex Analyst: https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst  
   - Cortex Search: https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-search/cortex-search-overview  
   - Cortex Agents: https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents

2. **Interfaces (SQL, REST, Python)**  
   **Objectives:** Call functions via SQL; stream tokens with REST; use the Python APIs where needed.  
   **Reading:**  
   - Cortex REST API: https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-rest-api  
   - REST Authentication: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/authentication

3. **RBAC & Access Control**  
   **Objectives:** Use DB roles (e.g., `SNOWFLAKE.CORTEX_USER`, `SNOWFLAKE.COPILOT_USER`) and **model-level RBAC**.  
   **Reading:**  
   - Opt out & DB roles (defaults & revoking PUBLIC): https://docs.snowflake.com/en/user-guide/snowflake-cortex/opting-out  
   - Model RBAC release note: https://docs.snowflake.com/en/release-notes/2025/other/2025-04-28-cortex-llm-model-rbac

4. **Cross-region inference**  
   **Objectives:** Configure `CORTEX_ENABLED_CROSS_REGION` for model availability across regions; billing/latency considerations.  
   **Reading:**  
   - Cross-region inference: https://docs.snowflake.com/en/user-guide/snowflake-cortex/cross-region-inference

5. **Snowflake Copilot**  
   **Objectives:** Use Copilot panels and inline Copilot; understand RBAC respect.  
   **Reading:**  
   - Copilot: https://docs.snowflake.com/en/user-guide/snowflake-copilot  
   - Copilot inline: https://docs.snowflake.com/en/user-guide/snowflake-copilot-inline

6. **BYOM: Model Registry & Snowpark Container Services**  
   **Objectives:** Log models in **Model Registry** and deploy via **SPCS** with compute pools (CPU/GPU).  
   **Reading:**  
   - Model Registry overview: https://docs.snowflake.com/en/developer-guide/snowflake-ml/model-registry/overview  
   - SPCS overview: https://docs.snowflake.com/en/developer-guide/snowpark-container-services/overview

### Practice Tasks
- Explore models/settings in **Cortex Playground**: https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-playground  
- Revoke PUBLIC and grant AI roles to a custom role: https://docs.snowflake.com/en/user-guide/snowflake-cortex/opting-out  
- Set `CORTEX_ENABLED_CROSS_REGION` and test `AI_COMPLETE`: https://docs.snowflake.com/en/user-guide/snowflake-cortex/cross-region-inference

---

## Section 3 — Domain 2.0: Snowflake Gen AI & LLM Functions (4.5 h)

### Subdomains & Detailed Objectives

1. **Apply GenAI & LLM Functions in Snowflake**  
   **Objectives:** Use **AI_COMPLETE** for general generation; prefer task functions for repetitive tasks.  
   **Reading:**  
   - AI_COMPLETE: https://docs.snowflake.com/en/sql-reference/functions/ai_complete-single-string  
   - AISQL overview (task functions & statuses): https://docs.snowflake.com/en/user-guide/snowflake-cortex/aisql

2. **Perform Data Analysis (structured & unstructured)**  
   **Objectives:** Combine `AI_PARSE_DOCUMENT` + `AI_EXTRACT` for document pipelines; integrate Analyst REST for text-to-SQL.  
   **Reading:**  
   - AI_PARSE_DOCUMENT: https://docs.snowflake.com/en/sql-reference/functions/ai_parse_document  
   - Parsing documents (guide): https://docs.snowflake.com/en/user-guide/snowflake-cortex/parse-document  
   - Cortex Analyst REST API: https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst/rest-api

3. **Build Chat Interfaces**  
   **Objectives:** Implement multi‑turn flows (Analyst REST, Agents threads); persist conversation state.  
   **Reading:**  
   - Analyst REST API: https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst/rest-api  
   - Agents Run API: https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-run

4. **Use Cortex in Data Pipelines**  
   **Objectives:** Add AISQL to ELT; consider token budgets; chunking large text.  
   **Reading:**  
   - AI_COUNT_TOKENS: https://docs.snowflake.com/en/sql-reference/functions/ai_count_tokens  
   - SPLIT_TEXT_RECURSIVE_CHARACTER: https://docs.snowflake.com/en/sql-reference/functions/split_text_recursive_character-snowflake-cortex

5. **Run Third‑party Models in Snowflake**  
   **Objectives:** Deploy models via **SPCS**; create compute pools; serve inference.  
   **Reading:**  
   - SPCS overview: https://docs.snowflake.com/en/developer-guide/snowpark-container-services/overview  
   - Model Registry UI: https://docs.snowflake.com/en/developer-guide/snowflake-ml/model-registry/snowsight-ui

### Practice Tasks
- **Structured outputs** with `response_format` + `show_details` on `AI_COMPLETE`: https://docs.snowflake.com/en/sql-reference/functions/ai_complete-single-string  
- **Classification & sentiment** using AISQL functions: https://docs.snowflake.com/en/user-guide/snowflake-cortex/aisql  
- **Embeddings & similarity** with `AI_EMBED`, `VECTOR` type & vector functions:  
  - AI_EMBED: https://docs.snowflake.com/en/sql-reference/functions/ai_embed  
  - VECTOR data type: https://docs.snowflake.com/en/sql-reference/data-types-vector  
  - Vector functions: https://docs.snowflake.com/en/sql-reference/functions-vector  
- **Document parsing** (LAYOUT + OCR) & extraction: https://docs.snowflake.com/en/sql-reference/functions/ai_parse_document  
- **SPCS service** (create compute pool; simple service): https://docs.snowflake.com/en/developer-guide/snowpark-container-services/overview

### Assignments
- **Mini RAG chatbot** with **Cortex Search** + `AI_COMPLETE`: https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-search/cortex-search-overview  
- **Semantic Q&A app** using **Cortex Analyst** + **Verified Query Repository**: https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst/verified-query-repository

---

## Section 4 — Domain 3.0: Snowflake Gen AI Governance (2.0 h)

### Subdomains & Detailed Objectives

1. **Model Access Controls**  
   **Objectives:** Implement allowlists and **model-level RBAC**; grant AI features only to required roles.  
   **Reading:**  
   - Opt out/roles & PUBLIC revocation: https://docs.snowflake.com/en/user-guide/snowflake-cortex/opting-out  
   - Model RBAC release note: https://docs.snowflake.com/en/release-notes/2025/other/2025-04-28-cortex-llm-model-rbac

2. **Guardrails & Safety**  
   **Objectives:** Enable filtering via `guardrails` in Complete options to reduce unsafe output.  
   **Reading:**  
   - CompleteOptions (guardrails): https://docs.snowflake.com/en/developer-guide/snowpark-ml/reference/latest/api/cortex/snowflake.cortex.CompleteOptions  
   - Trust & Safety FAQs: https://www.snowflake.com/en/legal/compliance/snowflake-ai-trust-and-safety/

3. **Monitor & Optimize Costs**  
   **Objectives:** Use Account Usage views to monitor tokens/credits and Search costs; understand compute/serverless/cloud services.  
   **Reading:**  
   - AISQL usage history (GA): https://docs.snowflake.com/en/sql-reference/account-usage/cortex_aisql_usage_history  
   - Cortex Search daily usage: https://docs.snowflake.com/en/sql-reference/account-usage/cortex_search_daily_usage_history  
   - Compute cost fundamentals: https://docs.snowflake.com/en/user-guide/cost-understanding-compute

4. **AI Observability**  
   **Objectives:** Evaluate/trace AI apps with TruLens; view metrics and runs in Snowsight.  
   **Reading:**  
   - AI Observability overview: https://docs.snowflake.com/en/user-guide/snowflake-cortex/ai-observability  
   - Evaluate AI applications: https://docs.snowflake.com/en/user-guide/snowflake-cortex/ai-observability/evaluate-ai-applications

### Practice Tasks
- Configure allowlist & RBAC pattern (role-grant model access): https://docs.snowflake.com/en/user-guide/snowflake-cortex/opting-out  
- Turn on `guardrails` and test prompts: https://docs.snowflake.com/en/developer-guide/snowpark-ml/reference/latest/api/cortex/snowflake.cortex.CompleteOptions  
- Query **AISQL usage** for last 7 days: https://docs.snowflake.com/en/sql-reference/account-usage/cortex_aisql_usage_history  
- Run an Observability evaluation on a RAG app: https://docs.snowflake.com/en/user-guide/snowflake-cortex/ai-observability/evaluate-ai-applications

---

## Section 5 — Domain 4.0: Snowflake Document AI (1.5 h)

> **Important:** Older `<model_build_name>!PREDICT` paths are **deprecated**. Prefer **AISQL** functions (`AI_EXTRACT`, `AI_PARSE_DOCUMENT`) and **Document Processing Playground** for workflows.

### Subdomains & Detailed Objectives

1. **Setup & Privileges**  
   **Objectives:** Create warehouse/schema/stage; grant roles (creator & usage); configure encryption.  
   **Reading:**  
   - Setting up Document AI: https://docs.snowflake.com/en/user-guide/snowflake-cortex/document-ai/setting-up

2. **Prepare Documents**  
   **Objectives:** Meet format/size/page limits; use SNOWFLAKE_SSE for internal stages.  
   **Reading:**  
   - Working with Document AI (overview & requirements): https://docs.snowflake.com/en/user-guide/snowflake-cortex/document-ai/overview

3. **Extract Values**  
   **Objectives:** Use `AI_EXTRACT` prompts to capture entities/tables; combine with `AI_PARSE_DOCUMENT` layout mode.  
   **Reading:**  
   - Parsing documents (guide): https://docs.snowflake.com/en/user-guide/snowflake-cortex/parse-document  
   - Document Processing Playground: https://docs.snowflake.com/en/user-guide/snowflake-cortex/document-processing-playground

4. **Troubleshooting, Cost & Limitations**  
   **Objectives:** Solve presigned URL expiry, stage encryption mismatch, and doc limits; manage costs.  
   **Reading:**  
   - Troubleshooting: https://docs.snowflake.com/en/user-guide/snowflake-cortex/document-ai/troubleshooting  
   - Cost governance: https://docs.snowflake.com/en/user-guide/snowflake-cortex/document-ai/cost-governance

### Practice Tasks
- Create stage with `SNOWFLAKE_SSE` and upload PDFs: https://docs.snowflake.com/en/user-guide/snowflake-cortex/document-ai/setting-up  
- Parse & extract invoice fields in Playground: https://docs.snowflake.com/en/user-guide/snowflake-cortex/document-processing-playground  
- Generate presigned URL for batch processing: https://docs.snowflake.com/en/user-guide/snowflake-cortex/document-ai/troubleshooting

---

## Section 6 — Capstone: Document Processing Framework (DPF) Study Case (2.0 h)

### Scenario
Design a **DPF** that ingests documents from a stage, parses layout, extracts entities, validates/alarms, and loads outputs into curated tables. Include **streams & tasks**, **AISQL functions**, **usage/cost tracking**, and **AI Observability**.

### Objectives
- Build a repeatable pipeline using **`AI_PARSE_DOCUMENT`** + **`AI_EXTRACT`**.  
- Automate ingestion/validation via **streams & tasks**.  
- Track AISQL usage/costs and evaluate extraction quality with **Observability**.

**Reading (curated):**  
- AI_PARSE_DOCUMENT: https://docs.snowflake.com/en/sql-reference/functions/ai_parse_document  
- Parsing documents: https://docs.snowflake.com/en/user-guide/snowflake-cortex/parse-document  
- AISQL usage history: https://docs.snowflake.com/en/sql-reference/account-usage/cortex_aisql_usage_history  
- AI Observability overview: https://docs.snowflake.com/en/user-guide/snowflake-cortex/ai-observability

### Lab Steps
1. Create `doc_stage` (internal, SNOWFLAKE_SSE) and upload sample docs.  
2. Parse to LAYOUT (markdown) and persist to a staging table.  
3. Extract fields via `AI_EXTRACT` prompts (e.g., vendor_name, invoice_number, total_amount) and validate with rules/thresholds.  
4. Build **stream + task** automation to process new stage files nightly.  
5. Query `CORTEX_AISQL_USAGE_HISTORY` for daily token credits; export summaries.  
6. Add **Observability runs** (context relevance, groundedness) to validate response quality.

### Deliverables
- SQL scripts (stage creation, parse/extract, streams/tasks).  
- A usage/cost report and evaluation dashboard snapshots.

---

## Section 7 — Final Exam Prep (1.0 h)

### Lessons
- **Review key concepts**: AISQL catalog; Analyst/Search/Agents; Document AI deprecations; usage views; cost levers.  
- **Practice**: Scenario-based questions on RBAC, guardrails, pipelines, and document flows.  
- **Exam day tips**: Timeboxing per domain; verifying GA vs preview in questions; using structured outputs for deterministic grading.

---

## Guided Link Distinction — “Latest vs Exam‑Safe”

| Topic | **Exam‑Safe (GA / Stable)** | **Latest / Renamed (Use with care)** |
|---|---|---|
| General LLM completions | **AI_COMPLETE** → https://docs.snowflake.com/en/sql-reference/functions/ai_complete-single-string | `SNOWFLAKE.CORTEX.COMPLETE` (older name; use AI_COMPLETE for latest features) |
| Task functions | **AISQL** catalog → https://docs.snowflake.com/en/user-guide/snowflake-cortex/aisql | New operators may be **Preview** (e.g., AI_AGG/AI_SUMMARIZE_AGG); check status in AISQL pages |
| Document parsing | **AI_PARSE_DOCUMENT** → https://docs.snowflake.com/en/sql-reference/functions/ai_parse_document | Older `<model_build_name>!PREDICT` paths **deprecated** (use AISQL) |
| Usage tracking | **CORTEX_AISQL_USAGE_HISTORY** → https://docs.snowflake.com/en/sql-reference/account-usage/cortex_aisql_usage_history | Older `CORTEX_FUNCTIONS_*` views no longer updated |
| Model access | **Opt-out & DB roles** → https://docs.snowflake.com/en/user-guide/snowflake-cortex/opting-out | Model-level RBAC (newer capability) at: https://docs.snowflake.com/en/release-notes/2025/other/2025-04-28-cortex-llm-model-rbac |
| Copilot | **Copilot** → https://docs.snowflake.com/en/user-guide/snowflake-copilot | **Copilot inline** is **Preview** in some regions: https://docs.snowflake.com/en/user-guide/snowflake-copilot-inline |
| Cross‑region | **CORTEX_ENABLED_CROSS_REGION** → https://docs.snowflake.com/en/user-guide/snowflake-cortex/cross-region-inference | — |

> When studying, prefer **Exam‑Safe** links above. Use **Latest/Preview** for awareness, but always verify GA status inside the reference page before adopting.

---

## References (APA 7)

Snowflake Inc. (2025). *Snowflake Cortex AISQL (including LLM functions)*. https://docs.snowflake.com/en/user-guide/snowflake-cortex/aisql  
Snowflake Inc. (2025). *AI_COMPLETE (single string)*. https://docs.snowflake.com/en/sql-reference/functions/ai_complete-single-string  
Snowflake Inc. (2025). *Cortex Analyst*. https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst  
Snowflake Inc. (2025). *Cortex Search overview*. https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-search/cortex-search-overview  
Snowflake Inc. (2025). *Cortex Agents*. https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents  
Snowflake Inc. (2025). *Cortex Playground*. https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-playground  
Snowflake Inc. (2025). *Programmatic access tokens*. https://docs.snowflake.com/en/user-guide/programmatic-access-tokens  
Snowflake Inc. (2025). *Authenticating Snowflake REST APIs with Snowflake*. https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/authentication  
Snowflake Inc. (2025). *Opt out of Snowflake AI features*. https://docs.snowflake.com/en/user-guide/snowflake-cortex/opting-out  
Snowflake Inc. (2025). *Role-Based Access Control for Cortex LLM Models* (Release note). https://docs.snowflake.com/en/release-notes/2025/other/2025-04-28-cortex-llm-model-rbac  
Snowflake Inc. (2025). *Cross-region inference*. https://docs.snowflake.com/en/user-guide/snowflake-cortex/cross-region-inference  
Snowflake Inc. (2025). *Using Snowflake Copilot*. https://docs.snowflake.com/en/user-guide/snowflake-copilot  
Snowflake Inc. (2025). *Using Snowflake Copilot inline*. https://docs.snowflake.com/en/user-guide/snowflake-copilot-inline  
Snowflake Inc. (2025). *Snowflake Model Registry overview*. https://docs.snowflake.com/en/developer-guide/snowflake-ml/model-registry/overview  
Snowflake Inc. (2025). *Snowpark Container Services overview*. https://docs.snowflake.com/en/developer-guide/snowpark-container-services/overview  
Snowflake Inc. (2025). *AI_PARSE_DOCUMENT*. https://docs.snowflake.com/en/sql-reference/functions/ai_parse_document  
Snowflake Inc. (2025). *Parsing documents with AI_PARSE_DOCUMENT*. https://docs.snowflake.com/en/user-guide/snowflake-cortex/parse-document  
Snowflake Inc. (2025). *Vector data types*. https://docs.snowflake.com/en/sql-reference/data-types-vector  
Snowflake Inc. (2025). *Vector functions*. https://docs.snowflake.com/en/sql-reference/functions-vector  
Snowflake Inc. (2025). *Vector Embeddings*. https://docs.snowflake.com/en/user-guide/snowflake-cortex/vector-embeddings  
Snowflake Inc. (2025). *TRY_COMPLETE (SNOWFLAKE.CORTEX)*. https://docs.snowflake.com/en/sql-reference/functions/try_complete-snowflake-cortex  
Snowflake Inc. (2025). *AI_COUNT_TOKENS*. https://docs.snowflake.com/en/sql-reference/functions/ai_count_tokens  
Snowflake Inc. (2025). *CORTEX_AISQL_USAGE_HISTORY view*. https://docs.snowflake.com/en/sql-reference/account-usage/cortex_aisql_usage_history  
Snowflake Inc. (2025). *CORTEX_SEARCH_DAILY_USAGE_HISTORY view*. https://docs.snowflake.com/en/sql-reference/account-usage/cortex_search_daily_usage_history  
Snowflake Inc. (2025). *AI Observability in Snowflake Cortex*. https://docs.snowflake.com/en/user-guide/snowflake-cortex/ai-observability  
Snowflake Inc. (2025). *Evaluate AI applications*. https://docs.snowflake.com/en/user-guide/snowflake-cortex/ai-observability/evaluate-ai-applications  
Snowflake Inc. (2025). *Document AI overview*. https://docs.snowflake.com/en/user-guide/snowflake-cortex/document-ai/overview  
Snowflake Inc. (2025). *Setting up Document AI*. https://docs.snowflake.com/en/user-guide/snowflake-cortex/document-ai/setting-up  
Snowflake Inc. (2025). *Troubleshooting Document AI*. https://docs.snowflake.com/en/user-guide/snowflake-cortex/document-ai/troubleshooting  
Snowflake Inc. (2025). *Cost governance of Document AI*. https://docs.snowflake.com/en/user-guide/snowflake-cortex/document-ai/cost-governance  
Snowflake Inc. (2024, Aug 12). *Snowflake AI Trust and Safety FAQs*. https://www.snowflake.com/en/legal/compliance/snowflake-ai-trust-and-safety/
