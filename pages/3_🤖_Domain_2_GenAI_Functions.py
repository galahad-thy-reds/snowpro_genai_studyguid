"""Domain 2.0: Snowflake Gen AI & LLM Functions section."""

from __future__ import annotations

import streamlit as st

from src.config import SECTIONS
from src.content.domain_2 import (
    DOMAIN_2_ASSIGNMENTS,
    DOMAIN_2_PRACTICE_TASKS,
    DOMAIN_2_SUBDOMAINS,
)
from src.utils import initialize_session_state, is_section_complete, mark_section_complete

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

# Reference to study plan
with st.expander("📚 **Study Plan References**", expanded=False):
    st.markdown("""
    This section is based on:
    - **[SnowPro GenAI Study Plan V2](docs/SnowPro_GenAI_Study_Plan_V2.md)** - Section 3: Domain 2.0
    - **[Official SnowPro Study Guide PDF](docs/SnowProGenAIStudyGuide.pdf)** - Domain 2.0 (Pages 8-9)
    
    **Exam Coverage**: This domain represents **40%** of the exam (largest weight). Focus on understanding:
    - AI_COMPLETE vs task-specific functions (when to use each)
    - Document processing pipelines (AI_PARSE_DOCUMENT + AI_EXTRACT)
    - Chat interface implementation (multi-turn, state persistence)
    - Pipeline integration (token budgets, chunking)
    - Third-party model deployment (SPCS, Model Registry)
    """)

st.markdown("---")

# Subdomains
st.markdown("## Subdomains & Objectives")

st.info(
    "💡 **Study Tip**: This is the **largest domain (40%)**. Focus on practical implementation: "
    "function selection, pipeline integration, and chat interfaces. "
    "Reference: [Study Plan V2](docs/SnowPro_GenAI_Study_Plan_V2.md) Section 3"
)

for subdomain in DOMAIN_2_SUBDOMAINS:
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

for i, task in enumerate(DOMAIN_2_PRACTICE_TASKS, 1):
    st.markdown(f"**{i}. {task.description}**")
    if task.url:
        st.markdown(f"   📖 [Documentation]({task.url})")
    st.checkbox(f"Completed task {i}", key=f"task_2_{i}")

st.markdown("---")

# Assignments
st.markdown("## Assignments")

assignment_titles = [
    "Mini RAG chatbot",
    "Semantic Q&A app",
]

for i, (assignment, title) in enumerate(zip(DOMAIN_2_ASSIGNMENTS, assignment_titles), 1):
    with st.expander(f"**Assignment {i}: {title}**"):
        st.markdown(assignment.description)
        if assignment.url:
            st.markdown(f"📖 [Documentation]({assignment.url})")
        st.checkbox(f"Completed assignment {i}", key=f"assignment_{i}")

st.markdown("---")

# Completion checkbox
if st.checkbox("✅ Mark this section as complete", value=is_section_complete(3)):
    mark_section_complete(3)
    st.success("Section marked as complete! Great job! 🎉")
    st.balloons()

