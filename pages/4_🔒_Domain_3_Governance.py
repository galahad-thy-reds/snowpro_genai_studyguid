"""Domain 3.0: Snowflake Gen AI Governance section."""

from __future__ import annotations

import streamlit as st

from src.config import SECTIONS
from src.utils import initialize_session_state, mark_section_complete, is_section_complete

# Page configuration
st.set_page_config(
    page_title="Domain 3.0: Snowflake Gen AI Governance",
    page_icon="🔒",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Initialize session state
initialize_session_state()

# Header
section_info = SECTIONS[3]
st.title(f"{section_info['icon']} {section_info['title']}")
st.caption(f"Estimated time: {section_info['time']} | Exam weight: {section_info['weight']}%")

st.markdown("---")

# Subdomains
st.markdown("## Subdomains & Objectives")

subdomains = [
    {
        "title": "1. Model Access Controls",
        "objectives": "Implement allowlists and model-level RBAC; grant AI features only to required roles.",
        "readings": [
            ("Opt out/roles & PUBLIC revocation", "https://docs.snowflake.com/en/user-guide/snowflake-cortex/opting-out"),
            ("Model RBAC release note", "https://docs.snowflake.com/en/release-notes/2025/other/2025-04-28-cortex-llm-model-rbac"),
        ],
    },
    {
        "title": "2. Guardrails & Safety",
        "objectives": "Enable filtering via guardrails in Complete options to reduce unsafe output.",
        "readings": [
            ("CompleteOptions (guardrails)", "https://docs.snowflake.com/en/developer-guide/snowpark-ml/reference/latest/api/cortex/snowflake.cortex.CompleteOptions"),
            ("Trust & Safety FAQs", "https://www.snowflake.com/en/legal/compliance/snowflake-ai-trust-and-safety/"),
        ],
    },
    {
        "title": "3. Monitor & Optimize Costs",
        "objectives": "Use Account Usage views to monitor tokens/credits and Search costs; understand compute/serverless/cloud services.",
        "readings": [
            ("AISQL usage history (GA)", "https://docs.snowflake.com/en/sql-reference/account-usage/cortex_aisql_usage_history"),
            ("Cortex Search daily usage", "https://docs.snowflake.com/en/sql-reference/account-usage/cortex_search_daily_usage_history"),
            ("Compute cost fundamentals", "https://docs.snowflake.com/en/user-guide/cost-understanding-compute"),
        ],
    },
    {
        "title": "4. AI Observability",
        "objectives": "Evaluate/trace AI apps with TruLens; view metrics and runs in Snowsight.",
        "readings": [
            ("AI Observability overview", "https://docs.snowflake.com/en/user-guide/snowflake-cortex/ai-observability"),
            ("Evaluate AI applications", "https://docs.snowflake.com/en/user-guide/snowflake-cortex/ai-observability/evaluate-ai-applications"),
        ],
    },
]

for i, subdomain in enumerate(subdomains, 1):
    with st.expander(f"**{subdomain['title']}**"):
        st.markdown(f"**Objectives:** {subdomain['objectives']}")
        st.markdown("**Reading:**")
        for title, url in subdomain['readings']:
            st.markdown(f"- [{title}]({url})")

st.markdown("---")

# Practice Tasks
st.markdown("## Practice Tasks")

practice_tasks = [
    {
        "task": "Configure allowlist & RBAC pattern (role-grant model access)",
        "link": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/opting-out",
    },
    {
        "task": "Turn on guardrails and test prompts",
        "link": "https://docs.snowflake.com/en/developer-guide/snowpark-ml/reference/latest/api/cortex/snowflake.cortex.CompleteOptions",
    },
    {
        "task": "Query AISQL usage for last 7 days",
        "link": "https://docs.snowflake.com/en/sql-reference/account-usage/cortex_aisql_usage_history",
    },
    {
        "task": "Run an Observability evaluation on a RAG app",
        "link": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/ai-observability/evaluate-ai-applications",
    },
]

for i, task in enumerate(practice_tasks, 1):
    st.markdown(f"**{i}. {task['task']}**")
    st.markdown(f"   📖 [Documentation]({task['link']})")
    st.checkbox(f"Completed task {i}", key=f"task_3_{i}")

st.markdown("---")

# Key Concepts
st.markdown("## Key Governance Concepts")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### Access Control
    - **DB Roles**: `SNOWFLAKE.CORTEX_USER`, `SNOWFLAKE.COPILOT_USER`
    - **Model-level RBAC**: Fine-grained model access control
    - **Opt-out**: Revoke PUBLIC access, grant to specific roles
    - **Allowlists**: Control which models can be used
    """)

with col2:
    st.markdown("""
    ### Cost Management
    - **AISQL Usage**: Monitor via `CORTEX_AISQL_USAGE_HISTORY`
    - **Search Costs**: Track via `CORTEX_SEARCH_DAILY_USAGE_HISTORY`
    - **Compute Types**: Understand serverless vs compute costs
    - **Token Budgets**: Use `AI_COUNT_TOKENS` for estimation
    """)

st.markdown("---")

# Completion checkbox
if st.checkbox("✅ Mark this section as complete", value=is_section_complete(4)):
    mark_section_complete(4)
    st.success("Section marked as complete! Great job! 🎉")
    st.balloons()

