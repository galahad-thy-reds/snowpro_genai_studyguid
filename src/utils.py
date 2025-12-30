"""Utility functions for the SnowPro GenAI Study Guide app."""

from __future__ import annotations

import streamlit as st

from src.config import SESSION_KEYS


def initialize_session_state() -> None:
    """Initialize session state with default values."""
    if SESSION_KEYS["progress"] not in st.session_state:
        st.session_state[SESSION_KEYS["progress"]] = {}
    
    if SESSION_KEYS["completed_sections"] not in st.session_state:
        st.session_state[SESSION_KEYS["completed_sections"]] = set()
    
    if SESSION_KEYS["study_time"] not in st.session_state:
        st.session_state[SESSION_KEYS["study_time"]] = {}


def calculate_progress() -> float:
    """Calculate overall progress percentage."""
    from src.config import SECTIONS, SESSION_KEYS
    
    completed = st.session_state.get(SESSION_KEYS["completed_sections"], set())
    total_sections = len(SECTIONS)
    
    if total_sections == 0:
        return 0.0
    
    return (len(completed) / total_sections) * 100


def format_time(time_str: str | None) -> str:
    """Format time string for display."""
    if not time_str:
        return "N/A"
    return time_str


def format_weight(weight: int | None) -> str:
    """Format weight percentage for display."""
    if weight is None:
        return "—"
    return f"{weight}%"


def render_external_link(text: str, url: str) -> str:
    """Generate markdown for external link that opens in new tab."""
    return f'<a href="{url}" target="_blank" rel="noopener noreferrer">{text}</a>'


def mark_section_complete(section_id: int) -> None:
    """Mark a section as completed."""
    from src.config import SESSION_KEYS
    
    if SESSION_KEYS["completed_sections"] not in st.session_state:
        st.session_state[SESSION_KEYS["completed_sections"]] = set()
    
    st.session_state[SESSION_KEYS["completed_sections"]].add(section_id)


def is_section_complete(section_id: int) -> bool:
    """Check if a section is completed."""
    from src.config import SESSION_KEYS
    
    completed = st.session_state.get(SESSION_KEYS["completed_sections"], set())
    return section_id in completed

