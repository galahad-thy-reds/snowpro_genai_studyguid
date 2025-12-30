"""Domain 1.0: Snowflake for Gen AI Overview section."""

from __future__ import annotations

import streamlit as st

from src.config import SECTIONS
from src.content.domain_1 import DOMAIN_1_PRACTICE_TASKS, DOMAIN_1_SUBDOMAINS
from src.utils import initialize_session_state, is_section_complete, mark_section_complete

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

for subdomain in DOMAIN_1_SUBDOMAINS:
    with st.expander(f"**{subdomain.title}**"):
        st.markdown(f"**Objectives:** {subdomain.objectives}")
        st.markdown("**Reading:**")
        for reading in subdomain.readings:
            st.markdown(f"- [{reading.title}]({reading.url})")

st.markdown("---")

# Practice Tasks
st.markdown("## Practice Tasks")

for i, task in enumerate(DOMAIN_1_PRACTICE_TASKS, 1):
    st.markdown(f"**{i}. {task.description}**")
    if task.url:
        st.markdown(f"   📖 [Documentation]({task.url})")
    st.checkbox(f"Completed task {i}", key=f"task_1_{i}")

st.markdown("---")

# Completion checkbox
if st.checkbox("✅ Mark this section as complete", value=is_section_complete(2)):
    mark_section_complete(2)
    st.success("Section marked as complete! Great job! 🎉")
    st.balloons()

