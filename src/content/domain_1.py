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

