"""Domain 3.0: Snowflake Gen AI Governance section."""

from __future__ import annotations

import streamlit as st

from src.config import SECTIONS
from src.content.domain_3 import DOMAIN_3_PRACTICE_TASKS, DOMAIN_3_SUBDOMAINS
from src.utils import initialize_session_state, is_section_complete, mark_section_complete

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

# Reference to study plan
with st.expander("📚 **Study Plan References**", expanded=False):
    st.markdown("""
    This section is based on:
    - **[SnowPro GenAI Study Plan V2](docs/SnowPro_GenAI_Study_Plan_V2.md)** - Section 4: Domain 3.0
    - **[Official SnowPro Study Guide PDF](docs/SnowProGenAIStudyGuide.pdf)** - Domain 3.0 (Pages 10-11)
    
    **Exam Coverage**: This domain represents **22%** of the exam. Focus on understanding:
    - Model access controls (allowlists, RBAC, opt-out patterns)
    - Guardrails and safety measures (Cortex Guard)
    - Cost monitoring and optimization (usage views, token management)
    - AI observability tools (metrics, tracing, evaluation)
    """)

st.markdown("---")

# Subdomains
st.markdown("## Subdomains & Objectives")

st.info(
    "💡 **Study Tip**: Governance is critical for production deployments. Focus on "
    "access control patterns, cost monitoring views, and safety measures. "
    "Reference: [Study Plan V2](docs/SnowPro_GenAI_Study_Plan_V2.md) Section 4"
)

for subdomain in DOMAIN_3_SUBDOMAINS:
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

for i, task in enumerate(DOMAIN_3_PRACTICE_TASKS, 1):
    st.markdown(f"**{i}. {task.description}**")
    if task.url:
        st.markdown(f"   📖 [Documentation]({task.url})")
    st.checkbox(f"Completed task {i}", key=f"task_3_{i}")

st.markdown("---")

# Completion checkbox
if st.checkbox("✅ Mark this section as complete", value=is_section_complete(4)):
    mark_section_complete(4)
    st.success("Section marked as complete! Great job! 🎉")
    st.balloons()

