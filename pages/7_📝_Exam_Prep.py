"""Final Exam Prep section."""

from __future__ import annotations

import streamlit as st

from src.config import SECTIONS
from src.utils import calculate_progress, initialize_session_state, mark_section_complete, is_section_complete

# Page configuration
st.set_page_config(
    page_title="Final Exam Prep - SnowPro GenAI Study Guide",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Initialize session state
initialize_session_state()

# Header
section_info = SECTIONS[6]
st.title(f"{section_info['icon']} {section_info['title']}")
st.caption(f"Estimated time: {section_info['time']}")

st.markdown("---")

# Progress Summary
progress = calculate_progress()
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Overall Progress", f"{progress:.1f}%")
with col2:
    completed = len(st.session_state.get("completed_sections", set()))
    st.metric("Sections Completed", f"{completed}/7")
with col3:
    st.metric("Ready for Exam", "✅" if progress >= 80 else "⏳")

st.markdown("---")

# Review Key Concepts
st.markdown("## Review Key Concepts")

concepts = {
    "AISQL Catalog": "Task functions, statuses, and model selection",
    "Analyst/Search/Agents": "When to use each Cortex component",
    "Document AI Deprecations": "Older PREDICT paths deprecated, use AISQL",
    "Usage Views": "CORTEX_AISQL_USAGE_HISTORY for monitoring",
    "Cost Levers": "Compute, serverless, cloud services costs",
    "RBAC Patterns": "CORTEX_USER, COPILOT_USER, model-level RBAC",
    "Guardrails": "Safety filtering in Complete options",
    "Pipelines": "Integrating AISQL into ELT workflows",
    "Document Flows": "Parse → Extract → Validate → Load",
}

for concept, description in concepts.items():
    with st.expander(f"**{concept}**"):
        st.markdown(description)

st.markdown("---")

# Practice Scenarios
st.markdown("## Practice Scenarios")

scenarios = [
    {
        "title": "RBAC Configuration",
        "question": "How would you configure model-level RBAC to restrict access to specific LLM models?",
        "key_points": [
            "Use GRANT/REVOKE on model objects",
            "Create custom roles with specific model access",
            "Revoke PUBLIC access to Cortex features",
            "Grant CORTEX_USER role to authorized users",
        ],
    },
    {
        "title": "Guardrails Implementation",
        "question": "How do you enable guardrails to reduce unsafe output from AI_COMPLETE?",
        "key_points": [
            "Use guardrails parameter in CompleteOptions",
            "Configure filtering for content safety",
            "Test with various prompts to validate",
            "Monitor guardrail effectiveness",
        ],
    },
    {
        "title": "Pipeline Integration",
        "question": "How would you add AISQL functions to an existing ELT pipeline?",
        "key_points": [
            "Use AI_COUNT_TOKENS for budget estimation",
            "Chunk large text with SPLIT_TEXT_RECURSIVE_CHARACTER",
            "Consider token limits and costs",
            "Handle errors gracefully with TRY_COMPLETE",
        ],
    },
    {
        "title": "Document Processing Flow",
        "question": "Design a document processing pipeline from stage to curated table.",
        "key_points": [
            "Create stage with SNOWFLAKE_SSE encryption",
            "Parse with AI_PARSE_DOCUMENT (LAYOUT mode)",
            "Extract with AI_EXTRACT using prompts",
            "Validate and load into curated tables",
            "Use streams & tasks for automation",
        ],
    },
]

for i, scenario in enumerate(scenarios, 1):
    with st.expander(f"**Scenario {i}: {scenario['title']}**"):
        st.markdown(f"**Question:** {scenario['question']}")
        st.markdown("**Key Points:**")
        for point in scenario['key_points']:
            st.markdown(f"- {point}")

st.markdown("---")

# Exam Day Tips
st.markdown("## Exam Day Tips")

tips = [
    "**Timeboxing**: Allocate time per domain based on weights (40% for Domain 2.0)",
    "**GA vs Preview**: Verify GA status in questions - prefer exam-safe features",
    "**Structured Outputs**: Use structured outputs for deterministic grading",
    "**Read Carefully**: Scenario-based questions require understanding context",
    "**Process of Elimination**: Eliminate clearly wrong answers first",
    "**Practice First**: Hands-on experience is crucial for success",
]

st.markdown("### Time Management")
st.markdown("""
- **Domain 1.0 (26%)**: ~15-20 minutes
- **Domain 2.0 (40%)**: ~25-30 minutes (largest weight)
- **Domain 3.0 (22%)**: ~12-15 minutes
- **Domain 4.0 (12%)**: ~8-10 minutes
- **Review**: ~10-15 minutes
""")

st.markdown("### Key Reminders")
for tip in tips:
    st.markdown(f"- {tip}")

st.markdown("---")

# Exam-Safe vs Latest Features
st.markdown("## Exam-Safe vs Latest Features")

st.info("""
**Important**: The exam focuses on GA (Generally Available) features. 
Be aware of preview features but prioritize stable, exam-safe implementations.
""")

comparison_data = {
    "Topic": [
        "General LLM completions",
        "Task functions",
        "Document parsing",
        "Usage tracking",
        "Model access",
    ],
    "Exam-Safe (GA)": [
        "AI_COMPLETE",
        "AISQL catalog",
        "AI_PARSE_DOCUMENT",
        "CORTEX_AISQL_USAGE_HISTORY",
        "Opt-out & DB roles",
    ],
    "Latest/Preview": [
        "SNOWFLAKE.CORTEX.COMPLETE (older name)",
        "New operators may be Preview",
        "Older PREDICT paths (deprecated)",
        "Older CORTEX_FUNCTIONS_* views",
        "Model-level RBAC (newer)",
    ],
}

st.dataframe(comparison_data, use_container_width=True)

st.markdown("---")

# Final Checklist
st.markdown("## Final Checklist")

checklist_items = [
    "Reviewed all 4 domains thoroughly",
    "Completed practice tasks for each domain",
    "Understood RBAC and access control patterns",
    "Familiar with AISQL functions and usage",
    "Practiced document processing workflows",
    "Reviewed cost monitoring and governance",
    "Understood exam format and time allocation",
    "Completed capstone project",
]

for item in checklist_items:
    st.checkbox(item, key=f"checklist_{item}")

st.markdown("---")

# Completion checkbox
if st.checkbox("✅ Mark this section as complete", value=is_section_complete(7)):
    mark_section_complete(7)
    st.success("All sections complete! You're ready for the exam! 🎉🎊")
    st.balloons()
    
    if progress >= 80:
        st.celebration("🎉", "Congratulations! You've completed the study guide!")

