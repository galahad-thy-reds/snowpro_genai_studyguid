"""Main entry point for SnowPro GenAI Study Guide Streamlit app."""

from __future__ import annotations

import streamlit as st

from src.config import APP_ICON, APP_TITLE, SECTIONS
from src.utils import calculate_progress, initialize_session_state

# Page configuration
st.set_page_config(
    page_title=APP_TITLE,
    page_icon=APP_ICON,
    layout="wide",
    initial_sidebar_state="expanded",
)

# Initialize session state
initialize_session_state()

# Sidebar navigation and progress
with st.sidebar:
    st.title(f"{APP_ICON} {APP_TITLE}")
    st.markdown("---")
    
    # Progress indicator
    progress = calculate_progress()
    st.metric("Overall Progress", f"{progress:.1f}%")
    st.progress(progress / 100)
    
    st.markdown("### Navigation")
    
    # Navigation links
    for section in SECTIONS:
        icon = section["icon"]
        title = section["title"]
        time = section["time"]
        weight = section["weight"]
        
        # Format display text
        if weight:
            display_text = f"{icon} {title} ({time}, {weight}%)"
        else:
            display_text = f"{icon} {title} ({time})"
        
        st.markdown(f"- {display_text}")
    
    st.markdown("---")
    st.markdown("### About")
    st.markdown(
        "This study guide helps you prepare for the **SnowPro Specialty: Gen AI Certification**."
    )
    st.markdown(
        "Follow the sections in order, complete practice tasks, and track your progress."
    )

# Main content
st.title(f"{APP_ICON} Welcome to {APP_TITLE}")
st.markdown("---")

st.markdown("""
### 🎯 Getting Started

This interactive study guide is designed to help you master the SnowPro Specialty: Gen AI Certification.

**Course Structure:**
- **Total Study Time**: ~14 hours
- **7 Main Sections**: From introduction to exam prep
- **4 Core Domains**: Covering all exam topics

**How to Use:**
1. Navigate through sections using the sidebar
2. Complete each section's objectives and practice tasks
3. Track your progress as you go
4. Review the capstone project for hands-on experience

**Prerequisites:**
- SnowPro Associate: Platform or SnowPro Core Certification
- Basic Python and SQL knowledge
- Access to Snowflake account (for hands-on practice)

Start by clicking on **📚 Introduction** in the sidebar!
""")

# Display course overview
st.markdown("### 📊 Course Overview")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### Domain Weights")
    for section in SECTIONS[1:5]:  # Domains 1-4
        if section["weight"]:
            st.metric(
                section["title"],
                f"{section['weight']}%",
                delta=f"{section['time']} study time"
            )

with col2:
    st.markdown("#### Study Sections")
    for section in SECTIONS:
        icon = section["icon"]
        title = section["title"]
        time = section["time"]
        st.markdown(f"- **{icon} {title}** - {time}")

st.markdown("---")
st.markdown(
    "*Last updated: Based on SnowPro GenAI Study Plan V2 (Dec 26, 2025)*"
)

