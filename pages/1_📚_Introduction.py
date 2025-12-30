"""Introduction section of the SnowPro GenAI Study Guide."""

from __future__ import annotations

import streamlit as st

from src.config import SECTIONS
from src.utils import initialize_session_state, mark_section_complete, is_section_complete

# Page configuration
st.set_page_config(
    page_title="Introduction - SnowPro GenAI Study Guide",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Initialize session state
initialize_session_state()

# Header
section_info = SECTIONS[0]
st.title(f"{section_info['icon']} {section_info['title']}")
st.caption(f"Estimated time: {section_info['time']}")

st.markdown("---")

# Main content
st.markdown("""
## What is Snowflake GenAI?

Snowflake Cortex AI brings Large Language Models (LLMs) and multimodal features 
natively within Snowflake. This enables you to:

- **AISQL Functions**: Use LLM functions directly in SQL queries
- **Cortex Analyst**: Natural language to SQL conversion
- **Cortex Search**: Vector search for RAG applications
- **Cortex Agents**: Agent orchestration and automation
- **Snowflake Copilot**: AI-powered assistance in Snowsight

### Key Capabilities

**AISQL (including LLM functions)**
- General text generation with `AI_COMPLETE`
- Task-specific functions (sentiment, translation, summarization)
- Document parsing and extraction
- Vector embeddings and similarity search

**Cortex Analyst**
- Semantic model generation
- Text-to-SQL with high accuracy
- Verified Query Repository (VQR)

**Cortex Search**
- Retrieval Augmented Generation (RAG)
- Multimodal search capabilities
- Enterprise search across documents

**Cortex Agents**
- Multi-step task automation
- Thread-based conversations
- Tool integration

**Snowflake Copilot**
- Inline AI assistance
- Panel-based interactions
- RBAC-respecting suggestions
""")

with st.expander("📖 Official Documentation Links"):
    st.markdown("""
    - [Snowflake Cortex AISQL](https://docs.snowflake.com/en/user-guide/snowflake-cortex/aisql)
    - [Cortex Analyst](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst)
    - [Cortex Search Overview](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-search/cortex-search-overview)
    - [Cortex Agents](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents)
    - [Snowflake Copilot](https://docs.snowflake.com/en/user-guide/snowflake-copilot)
    """)

st.markdown("---")

st.markdown("""
## Why This Certification Matters

The SnowPro Specialty: Gen AI Certification validates your ability to:

- **Implement Gen AI principles** in Snowflake environments
- **Leverage Cortex AI features** for real-world use cases
- **Build RAG applications** using LLMs
- **Govern AI workloads** with proper access controls and cost management
- **Process documents** using Document AI capabilities

This certification is essential for:
- AI/ML Engineers working with Snowflake
- Data Scientists building Gen AI applications
- Data Engineers implementing AI pipelines
- Data Application Developers creating AI-powered solutions
""")

st.markdown("---")

st.markdown("""
## Exam Format & Prerequisites

### Prerequisites
- **Active SnowPro Associate: Platform** OR **SnowPro Core Certification**

### Exam Structure
- **4 Core Domains** with different weights:
  - Domain 1.0: Snowflake for Gen AI Overview (26%)
  - Domain 2.0: Snowflake Gen AI & LLM Functions (40%)
  - Domain 3.0: Snowflake Gen AI Governance (22%)
  - Domain 4.0: Snowflake Document AI (12%)

### Success Tips
- **Practice-first approach**: Hands-on experience is crucial
- **Stay current**: Review official docs and release notes
- **Focus on GA features**: Prefer exam-safe (GA/Stable) over preview features
- **Time management**: Allocate study time based on domain weights
""")

st.markdown("---")

st.markdown("""
## Setting Up Your Environment

Before you begin, ensure you have:

1. **Snowflake Account Access**
   - Create roles and warehouses
   - Set up stages for document processing
   - Understand REST authentication (PAT/JWT/OAuth)

2. **Required Privileges**
   - `SNOWFLAKE.CORTEX_USER` role for AISQL functions
   - `SNOWFLAKE.COPILOT_USER` role for Copilot features
   - Warehouse usage privileges

3. **Hands-on Practice**
   - Access to Snowsight
   - AI & ML Studio → Cortex Playground
""")

with st.expander("📖 Setup Documentation"):
    st.markdown("""
    - [Programmatic Access Tokens](https://docs.snowflake.com/en/user-guide/programmatic-access-tokens)
    - [REST API Authentication](https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/authentication)
    - [Cortex Playground](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-playground)
    """)

st.markdown("---")

# Hands-on section
st.markdown("### 🛠️ Hands-on Exercise")

st.markdown("""
**Task**: Sign in to Snowsight and explore the Cortex Playground

1. Navigate to **AI & ML Studio** in Snowsight
2. Open **Cortex Playground**
3. Try different models and settings
4. Experiment with prompts and parameters

This will give you hands-on experience with Snowflake's Gen AI capabilities.
""")

st.markdown("---")

# Completion checkbox
if st.checkbox("✅ Mark this section as complete", value=is_section_complete(1)):
    mark_section_complete(1)
    st.success("Section marked as complete! Great job! 🎉")
    st.balloons()

