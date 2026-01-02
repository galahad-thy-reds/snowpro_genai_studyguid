"""Content for Domain 3.0: Snowflake Gen AI Governance."""

from __future__ import annotations

from src.data_loader import PracticeTask, Reading, Subdomain

# Domain 3.0 Subdomains
DOMAIN_3_SUBDOMAINS = [
    Subdomain(
        title="1. Model Access Controls",
        objectives="Implement allowlists and model-level RBAC; grant AI features only to required roles.",
        readings=[
            Reading(
                "Opt out/roles & PUBLIC revocation",
                "https://docs.snowflake.com/en/user-guide/snowflake-cortex/opting-out",
            ),
            Reading(
                "Model RBAC release note",
                "https://docs.snowflake.com/en/release-notes/2025/other/2025-04-28-cortex-llm-model-rbac",
            ),
        ],
        key_points=[
            "**Limits on which models can be used** - Control model access at organization/account level",
            "**Restrict access to specific models** - Fine-grained model permissions",
            "**CORTEX_MODELS_ALLOWLIST parameter** - Restrict which models can be used (account-level setting)",
            "**Model-level RBAC** - Fine-grained access control for specific models and roles",
            "**Affected Interfaces**: Cortex LLM REST API, COMPLETE (SNOWFLAKE.CORTEX), TRY_COMPLETE (SNOWFLAKE.CORTEX), Cortex LLM Playground (Public Preview)",
            "**Data safety and security considerations** - Verify data doesn't leave Snowflake, ensure data residency",
            "**REST API authentication methods** - OAuth, key pairs, token-based authentication",
            "**DB Roles**: SNOWFLAKE.CORTEX_USER, SNOWFLAKE.COPILOT_USER - Grant to specific roles instead of PUBLIC",
            "**Opt-out pattern**: Revoke PUBLIC access, grant to specific roles - Best practice for security",
        ],
        exam_focus="CORTEX_MODELS_ALLOWLIST parameter for model restrictions. Model-level RBAC for fine-grained control. DB roles (CORTEX_USER, COPILOT_USER). Opt-out pattern (revoke PUBLIC). REST API authentication methods.",
    ),
    Subdomain(
        title="2. Guardrails & Safety",
        objectives="Enable filtering via guardrails in Complete options to reduce unsafe output.",
        readings=[
            Reading(
                "CompleteOptions (guardrails)",
                "https://docs.snowflake.com/en/developer-guide/snowpark-ml/reference/latest/api/cortex/snowflake.cortex.CompleteOptions",
            ),
            Reading(
                "Trust & Safety FAQs",
                "https://www.snowflake.com/en/legal/compliance/snowflake-ai-trust-and-safety/",
            ),
        ],
        key_points=[
            "**Cortex Guard** - Filtering system for unsafe content",
            "**COMPLETE arguments** - guardrails parameter in COMPLETE function options",
            "**Methods to reduce model hallucinations** - Prompt engineering, temperature control, context management",
            "**Methods to reduce bias** - Diverse training data considerations, output filtering, evaluation criteria",
            "**Error conditions** - Handling unsafe content detection, error response handling",
            "**Enable guardrails** - Configure in CompleteOptions to filter harmful or unsafe LLM responses",
            "**Safety filtering** - Automatic detection and filtering of unsafe content",
        ],
        exam_focus="Cortex Guard for filtering unsafe content. guardrails parameter in COMPLETE. Methods to reduce hallucinations (prompt engineering, temperature) and bias. Error handling for unsafe content.",
    ),
    Subdomain(
        title="3. Monitor & Optimize Costs",
        objectives="Use Account Usage views to monitor tokens/credits and Search costs; understand compute/serverless/cloud services.",
        readings=[
            Reading(
                "AISQL usage history (GA)",
                "https://docs.snowflake.com/en/sql-reference/account-usage/cortex_aisql_usage_history",
            ),
            Reading(
                "Cortex Search daily usage",
                "https://docs.snowflake.com/en/sql-reference/account-usage/cortex_search_daily_usage_history",
            ),
            Reading(
                "Compute cost fundamentals",
                "https://docs.snowflake.com/en/user-guide/cost-understanding-compute",
            ),
            Reading(
                "Snowflake Service Consumption Table",
                "https://docs.snowflake.com/en/sql-reference/account-usage/service_consumption_table",
            ),
        ],
        key_points=[
            "**Cortex Search costs** - Different types: virtual warehouse, EMBED_TEXT, Serving costs",
            "**Cortex Analyst costs** - Monitor via Service Consumption Table and usage views",
            "**Snowflake Service Consumption Table** - Central view for service-level cost tracking",
            "**Cortex LLM functions** - Token-based pricing, minimize tokens for cost optimization",
            "**Token cost implications** - Understand token pricing models and usage patterns",
            "**Tracking model usage and consumption** - Monitor via Account Usage views",
            "**Usage quotas** - Set limits to control costs",
            "**CORTEX_AISQL_USAGE_HISTORY view** - Monitor AISQL function usage (GA, preferred over older views)",
            "**CORTEX_FUNCTIONS_USAGE_HISTORY view** - Legacy view (check if still updated)",
            "**CORTEX_FUNCTIONS_QUERY_USAGE_HISTORY view** - Query-level usage details",
            "**CORTEX_SEARCH_DAILY_USAGE_HISTORY view** - Daily Search service usage and costs",
            "**METERING_DAILY_HISTORY view** - Daily metering and credit consumption",
            "**Minimize tokens** - Use AI_COUNT_TOKENS to estimate, optimize prompts to reduce token usage",
            "**Compute cost fundamentals** - Understand serverless vs compute vs cloud services costs",
        ],
        exam_focus="CORTEX_AISQL_USAGE_HISTORY (GA) for function usage. CORTEX_SEARCH_DAILY_USAGE_HISTORY for Search costs. Service Consumption Table for overall tracking. Token minimization strategies. Understand cost types: compute/serverless/cloud services.",
    ),
    Subdomain(
        title="4. AI Observability",
        objectives="Evaluate/trace AI apps with TruLens; view metrics and runs in Snowsight.",
        readings=[
            Reading(
                "AI Observability overview",
                "https://docs.snowflake.com/en/user-guide/snowflake-cortex/ai-observability",
            ),
            Reading(
                "Evaluate AI applications",
                "https://docs.snowflake.com/en/user-guide/snowflake-cortex/ai-observability/evaluate-ai-applications",
            ),
        ],
        key_points=[
            "**Snowflake AI observability (Public Preview)** - Tools for monitoring and evaluating AI applications",
            "**Evaluation metrics** - Measure AI application performance and quality",
            "**Comparisons** - Compare different model versions or configurations",
            "**Tracing** - Track AI application execution and data flow",
            "**Logging** - Capture AI application events and interactions",
            "**Event tables** - Store observability data for analysis",
            "**Implementation methods** - Configure observability for AI applications",
            "**Trulens SDK** - External SDK for AI application evaluation and monitoring",
            "**View metrics and runs in Snowsight** - UI for monitoring AI observability data",
            "**Evaluate AI applications** - Test and measure AI application quality and performance",
        ],
        exam_focus="AI Observability (Public Preview) features: evaluation metrics, comparisons, tracing, logging, event tables. Trulens SDK for external evaluation. View metrics in Snowsight. Know implementation methods.",
    ),
]

# Domain 3.0 Practice Tasks
DOMAIN_3_PRACTICE_TASKS = [
    PracticeTask(
        description="Configure allowlist & RBAC pattern (role-grant model access)",
        url="https://docs.snowflake.com/en/user-guide/snowflake-cortex/opting-out",
    ),
    PracticeTask(
        description="Turn on guardrails and test prompts",
        url="https://docs.snowflake.com/en/developer-guide/snowpark-ml/reference/latest/api/cortex/snowflake.cortex.CompleteOptions",
    ),
    PracticeTask(
        description="Query AISQL usage for last 7 days",
        url="https://docs.snowflake.com/en/sql-reference/account-usage/cortex_aisql_usage_history",
    ),
    PracticeTask(
        description="Run an Observability evaluation on a RAG app",
        url="https://docs.snowflake.com/en/user-guide/snowflake-cortex/ai-observability/evaluate-ai-applications",
    ),
]

