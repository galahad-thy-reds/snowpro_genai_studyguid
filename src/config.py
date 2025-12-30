"""Configuration and constants for the SnowPro GenAI Study Guide app."""

from __future__ import annotations

# Study plan sections configuration
SECTIONS = [
    {
        "id": 1,
        "title": "Introduction",
        "icon": "📚",
        "time": "30 min",
        "weight": None,
    },
    {
        "id": 2,
        "title": "Domain 1.0: Snowflake for Gen AI Overview",
        "icon": "🔍",
        "time": "3.0 h",
        "weight": 26,
    },
    {
        "id": 3,
        "title": "Domain 2.0: Snowflake Gen AI & LLM Functions",
        "icon": "🤖",
        "time": "4.5 h",
        "weight": 40,
    },
    {
        "id": 4,
        "title": "Domain 3.0: Snowflake Gen AI Governance",
        "icon": "🔒",
        "time": "2.0 h",
        "weight": 22,
    },
    {
        "id": 5,
        "title": "Domain 4.0: Snowflake Document AI",
        "icon": "📄",
        "time": "1.5 h",
        "weight": 12,
    },
    {
        "id": 6,
        "title": "Capstone: Document Processing Framework",
        "icon": "🎯",
        "time": "2.0 h",
        "weight": None,
    },
    {
        "id": 7,
        "title": "Final Exam Prep",
        "icon": "📝",
        "time": "1.0 h",
        "weight": None,
    },
]

# Study plan document path
STUDY_PLAN_PATH = "docs/SnowPro_GenAI_Study_Plan_V2.md"

# App configuration
APP_TITLE = "SnowPro GenAI Study Guide"
APP_ICON = "❄️"

# Session state keys
SESSION_KEYS = {
    "progress": "user_progress",
    "current_section": "current_section",
    "completed_sections": "completed_sections",
    "study_time": "study_time_tracking",
}

