"""Domain 4.0: Snowflake Document AI section."""

from __future__ import annotations

import streamlit as st

from src.config import SECTIONS
from src.utils import initialize_session_state, mark_section_complete, is_section_complete

# Page configuration
st.set_page_config(
    page_title="Domain 4.0: Snowflake Document AI",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Initialize session state
initialize_session_state()

# Header
section_info = SECTIONS[4]
st.title(f"{section_info['icon']} {section_info['title']}")
st.caption(f"Estimated time: {section_info['time']} | Exam weight: {section_info['weight']}%")

st.markdown("---")

# Important note
st.warning("""
**Important:** Older `<model_build_name>!PREDICT` paths are **deprecated**. 
Prefer **AISQL** functions (`AI_EXTRACT`, `AI_PARSE_DOCUMENT`) and **Document Processing Playground** for workflows.
""")

# Subdomains
st.markdown("## Subdomains & Objectives")

subdomains = [
    {
        "title": "1. Setup & Privileges",
        "objectives": "Create warehouse/schema/stage; grant roles (creator & usage); configure encryption.",
        "readings": [
            ("Setting up Document AI", "https://docs.snowflake.com/en/user-guide/snowflake-cortex/document-ai/setting-up"),
        ],
    },
    {
        "title": "2. Prepare Documents",
        "objectives": "Meet format/size/page limits; use SNOWFLAKE_SSE for internal stages.",
        "readings": [
            ("Working with Document AI (overview & requirements)", "https://docs.snowflake.com/en/user-guide/snowflake-cortex/document-ai/overview"),
        ],
    },
    {
        "title": "3. Extract Values",
        "objectives": "Use AI_EXTRACT prompts to capture entities/tables; combine with AI_PARSE_DOCUMENT layout mode.",
        "readings": [
            ("Parsing documents (guide)", "https://docs.snowflake.com/en/user-guide/snowflake-cortex/parse-document"),
            ("Document Processing Playground", "https://docs.snowflake.com/en/user-guide/snowflake-cortex/document-processing-playground"),
        ],
    },
    {
        "title": "4. Troubleshooting, Cost & Limitations",
        "objectives": "Solve presigned URL expiry, stage encryption mismatch, and doc limits; manage costs.",
        "readings": [
            ("Troubleshooting", "https://docs.snowflake.com/en/user-guide/snowflake-cortex/document-ai/troubleshooting"),
            ("Cost governance", "https://docs.snowflake.com/en/user-guide/snowflake-cortex/document-ai/cost-governance"),
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
        "task": "Create stage with SNOWFLAKE_SSE and upload PDFs",
        "link": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/document-ai/setting-up",
    },
    {
        "task": "Parse & extract invoice fields in Playground",
        "link": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/document-processing-playground",
    },
    {
        "task": "Generate presigned URL for batch processing",
        "link": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/document-ai/troubleshooting",
    },
]

for i, task in enumerate(practice_tasks, 1):
    st.markdown(f"**{i}. {task['task']}**")
    st.markdown(f"   📖 [Documentation]({task['link']})")
    st.checkbox(f"Completed task {i}", key=f"task_4_{i}")

st.markdown("---")

# Key Concepts
st.markdown("## Key Document AI Concepts")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### Setup Requirements
    - **Stages**: Internal stages with SNOWFLAKE_SSE encryption
    - **Roles**: Document AI creator and usage roles
    - **Warehouse**: Required for processing
    - **Format Support**: PDF, DOCX, images
    
    ### Document Processing
    - **AI_PARSE_DOCUMENT**: Layout parsing (markdown output)
    - **AI_EXTRACT**: Entity extraction with prompts
    - **Modes**: LAYOUT, OCR, TEXT
    """)

with col2:
    st.markdown("""
    ### Best Practices
    - Use **Document Processing Playground** for testing
    - Combine parsing + extraction for pipelines
    - Handle presigned URL expiry (24 hours)
    - Monitor costs via usage views
    
    ### Troubleshooting
    - Stage encryption mismatch
    - Document size/page limits
    - Presigned URL expiration
    - Format compatibility issues
    """)

st.markdown("---")

# Completion checkbox
if st.checkbox("✅ Mark this section as complete", value=is_section_complete(5)):
    mark_section_complete(5)
    st.success("Section marked as complete! Great job! 🎉")
    st.balloons()

