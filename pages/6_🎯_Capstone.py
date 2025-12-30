"""Capstone: Document Processing Framework (DPF) Study Case section."""

from __future__ import annotations

import streamlit as st

from src.config import SECTIONS
from src.utils import initialize_session_state, mark_section_complete, is_section_complete

# Page configuration
st.set_page_config(
    page_title="Capstone: Document Processing Framework",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Initialize session state
initialize_session_state()

# Header
section_info = SECTIONS[5]
st.title(f"{section_info['icon']} {section_info['title']}")
st.caption(f"Estimated time: {section_info['time']}")

st.markdown("---")

# Scenario
st.markdown("## Scenario")

st.markdown("""
Design a **Document Processing Framework (DPF)** that:
- Ingests documents from a stage
- Parses layout and extracts entities
- Validates and alarms on issues
- Loads outputs into curated tables
- Includes **streams & tasks** for automation
- Uses **AISQL functions** for processing
- Tracks **usage/cost** via Account Usage views
- Implements **AI Observability** for quality validation
""")

st.markdown("---")

# Objectives
st.markdown("## Objectives")

objectives = [
    "Build a repeatable pipeline using **AI_PARSE_DOCUMENT** + **AI_EXTRACT**",
    "Automate ingestion/validation via **streams & tasks**",
    "Track AISQL usage/costs and evaluate extraction quality with **Observability**",
]

for i, objective in enumerate(objectives, 1):
    st.markdown(f"{i}. {objective}")

st.markdown("---")

# Reading Resources
st.markdown("## Reading Resources")

readings = [
    ("AI_PARSE_DOCUMENT", "https://docs.snowflake.com/en/sql-reference/functions/ai_parse_document"),
    ("Parsing documents", "https://docs.snowflake.com/en/user-guide/snowflake-cortex/parse-document"),
    ("AISQL usage history", "https://docs.snowflake.com/en/sql-reference/account-usage/cortex_aisql_usage_history"),
    ("AI Observability overview", "https://docs.snowflake.com/en/user-guide/snowflake-cortex/ai-observability"),
]

for title, url in readings:
    st.markdown(f"- [{title}]({url})")

st.markdown("---")

# Lab Steps
st.markdown("## Lab Steps")

lab_steps = [
    "Create `doc_stage` (internal, SNOWFLAKE_SSE) and upload sample docs",
    "Parse to LAYOUT (markdown) and persist to a staging table",
    "Extract fields via AI_EXTRACT prompts (e.g., vendor_name, invoice_number, total_amount) and validate with rules/thresholds",
    "Build **stream + task** automation to process new stage files nightly",
    "Query `CORTEX_AISQL_USAGE_HISTORY` for daily token credits; export summaries",
    "Add **Observability runs** (context relevance, groundedness) to validate response quality",
]

for i, step in enumerate(lab_steps, 1):
    st.markdown(f"### Step {i}")
    st.markdown(step)
    st.checkbox(f"Completed step {i}", key=f"capstone_step_{i}")

st.markdown("---")

# Deliverables
st.markdown("## Deliverables")

deliverables = [
    "SQL scripts (stage creation, parse/extract, streams/tasks)",
    "A usage/cost report and evaluation dashboard snapshots",
]

st.markdown("**Expected Deliverables:**")
for deliverable in deliverables:
    st.markdown(f"- {deliverable}")

st.markdown("---")

# Implementation Guide
st.markdown("## Implementation Guide")

with st.expander("**Step-by-Step Implementation**"):
    st.markdown("""
    ### 1. Stage Setup
    ```sql
    CREATE STAGE doc_stage
    ENCRYPTION = (TYPE = 'SNOWFLAKE_SSE');
    ```
    
    ### 2. Parse Documents
    ```sql
    CREATE TABLE parsed_docs AS
    SELECT 
        RELATIVE_PATH,
        AI_PARSE_DOCUMENT('@doc_stage', RELATIVE_PATH, 'LAYOUT') AS parsed_content
    FROM DIRECTORY(@doc_stage);
    ```
    
    ### 3. Extract Entities
    ```sql
    CREATE TABLE extracted_data AS
    SELECT 
        RELATIVE_PATH,
        AI_EXTRACT(
            parsed_content,
            'Extract vendor_name, invoice_number, total_amount as JSON'
        ) AS extracted_fields
    FROM parsed_docs;
    ```
    
    ### 4. Create Stream & Task
    ```sql
    CREATE STREAM doc_stream ON STAGE doc_stage;
    
    CREATE TASK process_docs
    WAREHOUSE = COMPUTE_WH
    SCHEDULE = 'USING CRON 0 2 * * * UTC'
    AS
    -- Process new files from stream
    SELECT * FROM doc_stream;
    ```
    
    ### 5. Monitor Usage
    ```sql
    SELECT 
        DATE_TRUNC('day', START_TIME) AS usage_date,
        SUM(INPUT_TOKENS) AS total_input_tokens,
        SUM(OUTPUT_TOKENS) AS total_output_tokens,
        SUM(CREDITS_USED) AS total_credits
    FROM SNOWFLAKE.ACCOUNT_USAGE.CORTEX_AISQL_USAGE_HISTORY
    WHERE START_TIME >= DATEADD('day', -7, CURRENT_TIMESTAMP())
    GROUP BY usage_date
    ORDER BY usage_date DESC;
    ```
    """)

st.markdown("---")

# Completion checkbox
if st.checkbox("✅ Mark this section as complete", value=is_section_complete(6)):
    mark_section_complete(6)
    st.success("Section marked as complete! Great job! 🎉")
    st.balloons()

