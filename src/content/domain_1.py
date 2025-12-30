"""Content for Domain 1.0: Snowflake for Gen AI Overview."""

from __future__ import annotations

from src.data_loader import PracticeTask, Reading, Subdomain

# Domain 1.0 Subdomains
DOMAIN_1_SUBDOMAINS = [
    Subdomain(
        title="1. Principles, Features & Best Practices",
        objectives="Differentiate Cortex components and where to use each (AISQL vs Analyst vs Search vs Agents vs Copilot).",
        readings=[
            Reading(
                "AISQL (incl. LLM functions)",
                "https://docs.snowflake.com/en/user-guide/snowflake-cortex/aisql",
            ),
            Reading(
                "Cortex Analyst",
                "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst",
            ),
            Reading(
                "Cortex Search",
                "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-search/cortex-search-overview",
            ),
            Reading(
                "Cortex Agents",
                "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents",
            ),
        ],
        key_points=[
            "**AISQL**: SQL interface for LLM functions (AI_COMPLETE, task-specific functions) - Use for direct SQL queries",
            "**Cortex Analyst**: NL2SQL service with high accuracy - Use for natural language to SQL conversion",
            "**Cortex Search**: Vector search for RAG applications - Use for semantic search on unstructured data",
            "**Cortex Agents**: Multi-step task orchestration - Use for complex workflows across data types",
            "**Snowflake Copilot**: Text-to-SQL assistant in UI - Use for interactive natural language queries",
            "**When to use each**: AISQL for SQL-based tasks, Analyst for NL2SQL, Search for RAG, Agents for automation, Copilot for UI assistance",
        ],
        exam_focus="Know when to use each component. AISQL = SQL functions, Analyst = NL2SQL, Search = RAG/vectors, Agents = automation, Copilot = UI assistant.",
    ),
    Subdomain(
        title="2. Interfaces (SQL, REST, Python)",
        objectives="Call functions via SQL; stream tokens with REST; use the Python APIs where needed.",
        readings=[
            Reading(
                "Cortex REST API",
                "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-rest-api",
            ),
            Reading(
                "REST Authentication",
                "https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/authentication",
            ),
        ],
        key_points=[
            "**SQL Interface**: Primary interface for Cortex functions - Use AI_COMPLETE, task functions directly in SQL",
            "**REST API**: Programmatic access with streaming support - Use for applications, token streaming, Python integration",
            "**Python APIs**: Snowpark ML and Snowflake Python APIs - Use for advanced workflows and custom applications",
            "**Authentication**: REST API supports PAT (Programmatic Access Tokens), JWT, OAuth - Know authentication methods",
            "**Streaming**: REST API supports token streaming for real-time responses - Important for chat interfaces",
        ],
        exam_focus="SQL for queries, REST for applications/streaming, Python for advanced use cases. Know authentication methods (PAT/JWT/OAuth).",
    ),
    Subdomain(
        title="3. RBAC & Access Control",
        objectives="Use DB roles (e.g., SNOWFLAKE.CORTEX_USER, SNOWFLAKE.COPILOT_USER) and model-level RBAC.",
        readings=[
            Reading(
                "Opt out & DB roles",
                "https://docs.snowflake.com/en/user-guide/snowflake-cortex/opting-out",
            ),
            Reading(
                "Model RBAC release note",
                "https://docs.snowflake.com/en/release-notes/2025/other/2025-04-28-cortex-llm-model-rbac",
            ),
        ],
        key_points=[
            "**Database Roles**: `SNOWFLAKE.CORTEX_USER` (AISQL functions), `SNOWFLAKE.COPILOT_USER` (Copilot access)",
            "**Opt-out Pattern**: Revoke PUBLIC access, grant specific roles - Best practice for security",
            "**Model-level RBAC**: Fine-grained control over which models can be used (newer capability)",
            "**CORTEX_MODELS_ALLOWLIST**: Parameter to restrict access to specific LLM models",
            "**Default Access**: PUBLIC role has access by default - Should be revoked in production",
            "**Grant Pattern**: `GRANT DATABASE ROLE SNOWFLAKE.CORTEX_USER TO ROLE <role_name>`",
        ],
        exam_focus="Know the DB roles (CORTEX_USER, COPILOT_USER), opt-out pattern, and model-level RBAC. CORTEX_MODELS_ALLOWLIST restricts model access.",
    ),
    Subdomain(
        title="4. Cross-region inference",
        objectives="Configure CORTEX_ENABLED_CROSS_REGION for model availability across regions; billing/latency considerations.",
        readings=[
            Reading(
                "Cross-region inference",
                "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cross-region-inference",
            ),
        ],
        key_points=[
            "**CORTEX_ENABLED_CROSS_REGION**: Parameter to enable models from other regions when local models unavailable",
            "**Use Case**: Ensures model availability when primary region models are down or unavailable",
            "**Latency Impact**: Cross-region calls have higher latency - Consider performance implications",
            "**Billing**: Cross-region inference may have different pricing - Understand cost implications",
            "**Configuration**: Set at account or session level - Know how to configure",
            "**Trade-offs**: Availability vs latency/cost - Understand when to enable",
        ],
        exam_focus="CORTEX_ENABLED_CROSS_REGION enables models from other regions. Understand latency and billing implications.",
    ),
    Subdomain(
        title="5. Snowflake Copilot",
        objectives="Use Copilot panels and inline Copilot; understand RBAC respect.",
        readings=[
            Reading(
                "Copilot",
                "https://docs.snowflake.com/en/user-guide/snowflake-copilot",
            ),
            Reading(
                "Copilot inline",
                "https://docs.snowflake.com/en/user-guide/snowflake-copilot-inline",
            ),
        ],
        key_points=[
            "**Copilot Panels**: Side panel interface in Snowsight for natural language queries",
            "**Inline Copilot**: Inline assistance within SQL editor (Preview in some regions)",
            "**RBAC Respect**: Copilot respects user's role permissions - Only suggests queries user can execute",
            "**Use Case**: Interactive text-to-SQL assistance for users without deep SQL knowledge",
            "**Privileges**: Requires `SNOWFLAKE.COPILOT_USER` database role",
            "**Integration**: Works with Verified Query Repository (VQR) for validated queries",
        ],
        exam_focus="Copilot = UI assistant for text-to-SQL. Respects RBAC. Requires COPILOT_USER role. Inline Copilot is Preview.",
    ),
    Subdomain(
        title="6. BYOM: Model Registry & Snowpark Container Services",
        objectives="Log models in Model Registry and deploy via SPCS with compute pools (CPU/GPU).",
        readings=[
            Reading(
                "Model Registry overview",
                "https://docs.snowflake.com/en/developer-guide/snowflake-ml/model-registry/overview",
            ),
            Reading(
                "SPCS overview",
                "https://docs.snowflake.com/en/developer-guide/snowpark-container-services/overview",
            ),
        ],
        key_points=[
            "**Model Registry**: Centralized model management - Log, version, and track custom models",
            "**SPCS (Snowpark Container Services)**: Deploy containerized models (Docker) with compute pools",
            "**Compute Pools**: CPU or GPU pools for model inference - Know how to create and configure",
            "**BYOM Sources**: Hugging Face, custom models, serialized files - Understand import methods",
            "**Workflow**: Register model → Deploy via SPCS → Serve inference - Know the process",
            "**Use Cases**: Custom models not available in Cortex, fine-tuned models, specialized requirements",
        ],
        exam_focus="Model Registry = model management. SPCS = containerized deployment. Know compute pools (CPU/GPU) and BYOM workflow.",
    ),
]

# Domain 1.0 Practice Tasks
DOMAIN_1_PRACTICE_TASKS = [
    PracticeTask(
        description="Explore models/settings in Cortex Playground",
        url="https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-playground",
    ),
    PracticeTask(
        description="Revoke PUBLIC and grant AI roles to a custom role",
        url="https://docs.snowflake.com/en/user-guide/snowflake-cortex/opting-out",
    ),
    PracticeTask(
        description="Set CORTEX_ENABLED_CROSS_REGION and test AI_COMPLETE",
        url="https://docs.snowflake.com/en/user-guide/snowflake-cortex/cross-region-inference",
    ),
]

