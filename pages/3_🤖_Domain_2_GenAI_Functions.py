"""Domain 2.0: Snowflake Gen AI & LLM Functions section."""

from __future__ import annotations

import streamlit as st

from src.config import SECTIONS
from src.utils import initialize_session_state, mark_section_complete, is_section_complete

# Page configuration
st.set_page_config(
    page_title="Domain 2.0: Snowflake Gen AI & LLM Functions",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Initialize session state
initialize_session_state()

# Header
section_info = SECTIONS[2]
st.title(f"{section_info['icon']} {section_info['title']}")
st.caption(f"Estimated time: {section_info['time']} | Exam weight: {section_info['weight']}%")

st.markdown("---")

# Subdomains
st.markdown("## Subdomains & Objectives")

subdomains = [
    {
        "title": "1. Apply GenAI & LLM Functions in Snowflake",
        "objectives": "Use AI_COMPLETE for general generation; prefer task functions for repetitive tasks.",
        "readings": [
            ("AI_COMPLETE", "https://docs.snowflake.com/en/sql-reference/functions/ai_complete-single-string"),
            ("AISQL overview", "https://docs.snowflake.com/en/user-guide/snowflake-cortex/aisql"),
        ],
    },
    {
        "title": "2. Perform Data Analysis (structured & unstructured)",
        "objectives": "Combine AI_PARSE_DOCUMENT + AI_EXTRACT for document pipelines; integrate Analyst REST for text-to-SQL.",
        "readings": [
            ("AI_PARSE_DOCUMENT", "https://docs.snowflake.com/en/sql-reference/functions/ai_parse_document"),
            ("Parsing documents (guide)", "https://docs.snowflake.com/en/user-guide/snowflake-cortex/parse-document"),
            ("Cortex Analyst REST API", "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst/rest-api"),
        ],
    },
    {
        "title": "3. Build Chat Interfaces",
        "objectives": "Implement multi-turn flows (Analyst REST, Agents threads); persist conversation state.",
        "readings": [
            ("Analyst REST API", "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst/rest-api"),
            ("Agents Run API", "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-run"),
        ],
    },
    {
        "title": "4. Use Cortex in Data Pipelines",
        "objectives": "Add AISQL to ELT; consider token budgets; chunking large text.",
        "readings": [
            ("AI_COUNT_TOKENS", "https://docs.snowflake.com/en/sql-reference/functions/ai_count_tokens"),
            ("SPLIT_TEXT_RECURSIVE_CHARACTER", "https://docs.snowflake.com/en/sql-reference/functions/split_text_recursive_character-snowflake-cortex"),
        ],
    },
    {
        "title": "5. Run Third-party Models in Snowflake",
        "objectives": "Deploy models via SPCS; create compute pools; serve inference.",
        "readings": [
            ("SPCS overview", "https://docs.snowflake.com/en/developer-guide/snowpark-container-services/overview"),
            ("Model Registry UI", "https://docs.snowflake.com/en/developer-guide/snowflake-ml/model-registry/snowsight-ui"),
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
        "task": "Structured outputs with response_format + show_details on AI_COMPLETE",
        "link": "https://docs.snowflake.com/en/sql-reference/functions/ai_complete-single-string",
    },
    {
        "task": "Classification & sentiment using AISQL functions",
        "link": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/aisql",
    },
    {
        "task": "Embeddings & similarity with AI_EMBED, VECTOR type & vector functions",
        "links": [
            ("AI_EMBED", "https://docs.snowflake.com/en/sql-reference/functions/ai_embed"),
            ("VECTOR data type", "https://docs.snowflake.com/en/sql-reference/data-types-vector"),
            ("Vector functions", "https://docs.snowflake.com/en/sql-reference/functions-vector"),
        ],
    },
    {
        "task": "Document parsing (LAYOUT + OCR) & extraction",
        "link": "https://docs.snowflake.com/en/sql-reference/functions/ai_parse_document",
    },
    {
        "task": "SPCS service (create compute pool; simple service)",
        "link": "https://docs.snowflake.com/en/developer-guide/snowpark-container-services/overview",
    },
]

for i, task in enumerate(practice_tasks, 1):
    st.markdown(f"**{i}. {task['task']}**")
    if 'link' in task:
        st.markdown(f"   📖 [Documentation]({task['link']})")
    elif 'links' in task:
        for title, url in task['links']:
            st.markdown(f"   📖 [{title}]({url})")
    st.checkbox(f"Completed task {i}", key=f"task_2_{i}")

st.markdown("---")

# Assignments
st.markdown("## Assignments")

assignments = [
    {
        "title": "Mini RAG chatbot",
        "description": "Build a RAG chatbot with Cortex Search + AI_COMPLETE",
        "link": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-search/cortex-search-overview",
    },
    {
        "title": "Semantic Q&A app",
        "description": "Create a semantic Q&A app using Cortex Analyst + Verified Query Repository",
        "link": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst/verified-query-repository",
    },
]

for i, assignment in enumerate(assignments, 1):
    with st.expander(f"**Assignment {i}: {assignment['title']}**"):
        st.markdown(assignment['description'])
        st.markdown(f"📖 [Documentation]({assignment['link']})")
        st.checkbox(f"Completed assignment {i}", key=f"assignment_{i}")

st.markdown("---")

# Completion checkbox
if st.checkbox("✅ Mark this section as complete", value=is_section_complete(3)):
    mark_section_complete(3)
    st.success("Section marked as complete! Great job! 🎉")
    st.balloons()

