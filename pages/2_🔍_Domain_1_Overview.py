"""Domain 1.0: Snowflake for Gen AI Overview section."""

from __future__ import annotations

import streamlit as st

from src.config import SECTIONS
from src.utils import initialize_session_state, mark_section_complete, is_section_complete

# Page configuration
st.set_page_config(
    page_title="Domain 1.0: Snowflake for Gen AI Overview",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Initialize session state
initialize_session_state()

# Header
section_info = SECTIONS[1]
st.title(f"{section_info['icon']} {section_info['title']}")
st.caption(f"Estimated time: {section_info['time']} | Exam weight: {section_info['weight']}%")

st.markdown("---")

# Subdomains
st.markdown("## Subdomains & Objectives")

subdomains = [
    {
        "title": "1. Principles, Features & Best Practices",
        "objectives": "Differentiate Cortex components and where to use each (AISQL vs Analyst vs Search vs Agents vs Copilot).",
        "readings": [
            ("AISQL (incl. LLM functions)", "https://docs.snowflake.com/en/user-guide/snowflake-cortex/aisql"),
            ("Cortex Analyst", "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst"),
            ("Cortex Search", "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-search/cortex-search-overview"),
            ("Cortex Agents", "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents"),
        ],
    },
    {
        "title": "2. Interfaces (SQL, REST, Python)",
        "objectives": "Call functions via SQL; stream tokens with REST; use the Python APIs where needed.",
        "readings": [
            ("Cortex REST API", "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-rest-api"),
            ("REST Authentication", "https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/authentication"),
        ],
    },
    {
        "title": "3. RBAC & Access Control",
        "objectives": "Use DB roles (e.g., SNOWFLAKE.CORTEX_USER, SNOWFLAKE.COPILOT_USER) and model-level RBAC.",
        "readings": [
            ("Opt out & DB roles", "https://docs.snowflake.com/en/user-guide/snowflake-cortex/opting-out"),
            ("Model RBAC release note", "https://docs.snowflake.com/en/release-notes/2025/other/2025-04-28-cortex-llm-model-rbac"),
        ],
    },
    {
        "title": "4. Cross-region inference",
        "objectives": "Configure CORTEX_ENABLED_CROSS_REGION for model availability across regions; billing/latency considerations.",
        "readings": [
            ("Cross-region inference", "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cross-region-inference"),
        ],
    },
    {
        "title": "5. Snowflake Copilot",
        "objectives": "Use Copilot panels and inline Copilot; understand RBAC respect.",
        "readings": [
            ("Copilot", "https://docs.snowflake.com/en/user-guide/snowflake-copilot"),
            ("Copilot inline", "https://docs.snowflake.com/en/user-guide/snowflake-copilot-inline"),
        ],
    },
    {
        "title": "6. BYOM: Model Registry & Snowpark Container Services",
        "objectives": "Log models in Model Registry and deploy via SPCS with compute pools (CPU/GPU).",
        "readings": [
            ("Model Registry overview", "https://docs.snowflake.com/en/developer-guide/snowflake-ml/model-registry/overview"),
            ("SPCS overview", "https://docs.snowflake.com/en/developer-guide/snowpark-container-services/overview"),
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
        "task": "Explore models/settings in Cortex Playground",
        "link": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-playground",
    },
    {
        "task": "Revoke PUBLIC and grant AI roles to a custom role",
        "link": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/opting-out",
    },
    {
        "task": "Set CORTEX_ENABLED_CROSS_REGION and test AI_COMPLETE",
        "link": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cross-region-inference",
    },
]

for i, task in enumerate(practice_tasks, 1):
    st.markdown(f"**{i}. {task['task']}**")
    st.markdown(f"   📖 [Documentation]({task['link']})")
    st.checkbox(f"Completed task {i}", key=f"task_1_{i}")

st.markdown("---")

# Completion checkbox
if st.checkbox("✅ Mark this section as complete", value=is_section_complete(2)):
    mark_section_complete(2)
    st.success("Section marked as complete! Great job! 🎉")
    st.balloons()

