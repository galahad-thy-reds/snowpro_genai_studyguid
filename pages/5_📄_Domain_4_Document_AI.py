"""Domain 4.0: Snowflake Document AI section."""

from __future__ import annotations

import streamlit as st

from src.config import SECTIONS
from src.content.domain_4 import DOMAIN_4_PRACTICE_TASKS, DOMAIN_4_SUBDOMAINS
from src.utils import initialize_session_state, is_section_complete, mark_section_complete

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

# Important note
st.warning("""
**Important:** Older `<model_build_name>!PREDICT` paths are **deprecated**. 
Prefer **AISQL** functions (`AI_EXTRACT`, `AI_PARSE_DOCUMENT`) and **Document Processing Playground** for workflows.
""")

# Reference to study plan
with st.expander("📚 **Study Plan References**", expanded=False):
    st.markdown("""
    This section is based on:
    - **[SnowPro GenAI Study Plan V2](docs/SnowPro_GenAI_Study_Plan_V2.md)** - Section 5: Domain 4.0
    - **[Official SnowPro Study Guide PDF](docs/SnowProGenAIStudyGuide.pdf)** - Domain 4.0 (Page 12)
    
    **Exam Coverage**: This domain represents **12%** of the exam. Focus on understanding:
    - Setup requirements (privileges, stages, encryption)
    - Document preparation (formats, limits, SNOWFLAKE_SSE)
    - Value extraction (AI_EXTRACT, AI_PARSE_DOCUMENT)
    - Troubleshooting (URL expiry, encryption mismatch, costs)
    """)

st.markdown("---")

# Subdomains
st.markdown("## Subdomains & Objectives")

st.info(
    "💡 **Study Tip**: Document AI uses AISQL functions (not deprecated PREDICT paths). "
    "Focus on SNOWFLAKE_SSE encryption requirement and the AI_EXTRACT + AI_PARSE_DOCUMENT workflow. "
    "Reference: [Study Plan V2](docs/SnowPro_GenAI_Study_Plan_V2.md) Section 5"
)

for subdomain in DOMAIN_4_SUBDOMAINS:
    with st.expander(f"**{subdomain.title}**"):
        st.markdown(f"**📋 Objectives:** {subdomain.objectives}")
        
        # Exam Focus
        if subdomain.exam_focus:
            st.markdown("---")
            st.markdown("### 🎯 Exam Focus")
            st.markdown(f"*{subdomain.exam_focus}*")
        
        # Key Points
        if subdomain.key_points:
            st.markdown("---")
            st.markdown("### 🔑 Key Points to Remember")
            for point in subdomain.key_points:
                # Render markdown which will convert markdown links to clickable links
                st.markdown(f"- {point}")
        
        # Reading Resources
        st.markdown("---")
        st.markdown("### 📖 Reading Resources")
        for reading in subdomain.readings:
            st.markdown(f"- [{reading.title}]({reading.url})")

st.markdown("---")

# Practice Tasks
st.markdown("## Practice Tasks")

for i, task in enumerate(DOMAIN_4_PRACTICE_TASKS, 1):
    st.markdown(f"**{i}. {task.description}**")
    if task.url:
        st.markdown(f"   📖 [Documentation]({task.url})")
    st.checkbox(f"Completed task {i}", key=f"task_4_{i}")

st.markdown("---")

# Completion checkbox
if st.checkbox("✅ Mark this section as complete", value=is_section_complete(5)):
    mark_section_complete(5)
    st.success("Section marked as complete! Great job! 🎉")
    st.balloons()

