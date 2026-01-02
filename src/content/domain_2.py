"""Content for Domain 2.0: Snowflake Gen AI & LLM Functions."""

from __future__ import annotations

from src.data_loader import PracticeTask, Reading, Subdomain

# Domain 2.0 Subdomains
DOMAIN_2_SUBDOMAINS = [
    Subdomain(
        title="1. Apply GenAI & LLM Functions in Snowflake",
        objectives="Use AI_COMPLETE for general generation; prefer task functions for repetitive tasks.",
        readings=[
            Reading(
                "AI_COMPLETE",
                "https://docs.snowflake.com/en/sql-reference/functions/ai_complete-single-string",
            ),
            Reading(
                "AISQL overview",
                "https://docs.snowflake.com/en/user-guide/snowflake-cortex/aisql",
            ),
            Reading(
                "CLASSIFY_TEXT",
                "https://docs.snowflake.com/en/sql-reference/functions/classify_text-snowflake-cortex",
            ),
            Reading(
                "EXTRACT_ANSWER",
                "https://docs.snowflake.com/en/sql-reference/functions/extract_answer-snowflake-cortex",
            ),
            Reading(
                "SENTIMENT",
                "https://docs.snowflake.com/en/sql-reference/functions/sentiment-snowflake-cortex",
            ),
            Reading(
                "SUMMARIZE",
                "https://docs.snowflake.com/en/sql-reference/functions/summarize-snowflake-cortex",
            ),
            Reading(
                "TRANSLATE",
                "https://docs.snowflake.com/en/sql-reference/functions/translate-snowflake-cortex",
            ),
            Reading(
                "AI_EMBED (EMBED_TEXT_768/1024)",
                "https://docs.snowflake.com/en/sql-reference/functions/ai_embed",
            ),
            Reading(
                "Vector functions",
                "https://docs.snowflake.com/en/sql-reference/functions-vector",
            ),
            Reading(
                "VECTOR_COSINE_SIMILARITY",
                "https://docs.snowflake.com/en/sql-reference/functions/vector_cosine_similarity",
            ),
            Reading(
                "VECTOR_L2_DISTANCE",
                "https://docs.snowflake.com/en/sql-reference/functions/vector_l2_distance",
            ),
            Reading(
                "VECTOR_INNER_PRODUCT",
                "https://docs.snowflake.com/en/sql-reference/functions/vector_inner_product",
            ),
            Reading(
                "VECTOR_L1_DISTANCE",
                "https://docs.snowflake.com/en/sql-reference/functions/vector_l1_distance",
            ),
            Reading(
                "AI_COUNT_TOKENS (COUNT_TOKENS)",
                "https://docs.snowflake.com/en/sql-reference/functions/ai_count_tokens",
            ),
            Reading(
                "TRY_COMPLETE",
                "https://docs.snowflake.com/en/sql-reference/functions/try_complete-snowflake-cortex",
            ),
        ],
        key_points=[
            "**Snowflake Cortex**",
            "  - **General functions**: [AI_COMPLETE](https://docs.snowflake.com/en/sql-reference/functions/ai_complete-single-string), COMPLETE Structured Outputs (response_format parameter)",
            "  - **Task-specific functions**: [CLASSIFY_TEXT](https://docs.snowflake.com/en/sql-reference/functions/classify_text-snowflake-cortex), [EXTRACT_ANSWER](https://docs.snowflake.com/en/sql-reference/functions/extract_answer-snowflake-cortex), [PARSE_DOCUMENT](https://docs.snowflake.com/en/sql-reference/functions/ai_parse_document), [SENTIMENT](https://docs.snowflake.com/en/sql-reference/functions/sentiment-snowflake-cortex), [SUMMARIZE](https://docs.snowflake.com/en/sql-reference/functions/summarize-snowflake-cortex), [TRANSLATE](https://docs.snowflake.com/en/sql-reference/functions/translate-snowflake-cortex), EMBED_TEXT_768, EMBED_TEXT_1024",
            "**Cortex Search** - Vector search for RAG applications",
            "**Cortex Analyst** - NL2SQL service for structured data",
            "**Cortex Fine-tuning** - Custom model training",
            "**Cortex Agents (Public Preview)** - Agent orchestration",
            "**Vector functions**: [VECTOR_INNER_PRODUCT](https://docs.snowflake.com/en/sql-reference/functions/vector_inner_product), [VECTOR_L1_DISTANCE](https://docs.snowflake.com/en/sql-reference/functions/vector_l1_distance), [VECTOR_L2_DISTANCE](https://docs.snowflake.com/en/sql-reference/functions/vector_l2_distance), [VECTOR_COSINE_SIMILARITY](https://docs.snowflake.com/en/sql-reference/functions/vector_cosine_similarity) (most common)",
            "**Helper functions**: [AI_COUNT_TOKENS](https://docs.snowflake.com/en/sql-reference/functions/ai_count_tokens) (COUNT_TOKENS), [TRY_COMPLETE](https://docs.snowflake.com/en/sql-reference/functions/try_complete-snowflake-cortex), SPLIT_TEXT_RECURSIVE_CHARACTER",
            "**Choosing a model**: Considerations (e.g., capability, latency, and cost)",
        ],
        exam_focus="AI_COMPLETE for general tasks, task functions for specific tasks. Know vector functions (COSINE_SIMILARITY most common). Use AI_COUNT_TOKENS for cost estimation.",
    ),
    Subdomain(
        title="2. Perform Data Analysis (structured & unstructured)",
        objectives="Combine AI_PARSE_DOCUMENT + AI_EXTRACT for document pipelines; integrate Analyst REST for text-to-SQL.",
        readings=[
            Reading(
                "AI_PARSE_DOCUMENT",
                "https://docs.snowflake.com/en/sql-reference/functions/ai_parse_document",
            ),
            Reading(
                "AI_EXTRACT",
                "https://docs.snowflake.com/en/sql-reference/functions/ai_extract",
            ),
            Reading(
                "Parsing documents (guide)",
                "https://docs.snowflake.com/en/user-guide/snowflake-cortex/parse-document",
            ),
            Reading(
                "Cortex Analyst REST API",
                "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst/rest-api",
            ),
            Reading(
                "Verified Query Repository (VQR)",
                "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst/verified-query-repository",
            ),
        ],
        key_points=[
            "**Unstructured Data**: [AI_PARSE_DOCUMENT](https://docs.snowflake.com/en/sql-reference/functions/ai_parse_document) (LAYOUT/OCR/TEXT modes) + [AI_EXTRACT](https://docs.snowflake.com/en/sql-reference/functions/ai_extract) - Pipeline for document processing",
            "**Structured Data**: Cortex Analyst REST API - NL2SQL for querying structured data",
            "**Verified Query Repository (VQR)**: Pre-validated queries - Improves accuracy and performance",
            "**Cortex Search Integration**: Combine with Analyst for enhanced RAG capabilities",
            "**Suggested Questions**: AI-generated question suggestions - Helps users discover insights",
            "**custom_instructions**: Customize Analyst behavior - Tailor responses to specific needs",
            "**Performance**: Consider latency, fine-tuning impact, model size - Optimize for use case",
        ],
        exam_focus="AI_PARSE_DOCUMENT + AI_EXTRACT for documents. Cortex Analyst REST for NL2SQL. Know VQR and custom_instructions. Understand performance considerations.",
    ),
    Subdomain(
        title="3. Build Chat Interfaces",
        objectives="Implement multi-turn flows (Analyst REST, Agents threads); persist conversation state.",
        readings=[
            Reading(
                "Analyst REST API",
                "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst/rest-api",
            ),
            Reading(
                "Agents Run API",
                "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-run",
            ),
        ],
        key_points=[
            "**Multi-turn Architecture**: Preserve context across messages - Essential for conversational interfaces",
            "**Analyst REST API**: Supports conversation threads - Maintain state between requests",
            "**Agents Threads**: Agent orchestration with conversation management - Complex multi-step workflows",
            "**State Persistence**: Store conversation history - Required for context-aware responses",
            "**Update Parameters**: Adjust temperature, max_tokens dynamically - Fine-tune during conversation",
            "**Integration**: Streamlit, Python, JavaScript - Know how to integrate in applications",
            "**Required Privileges**: USAGE on database/schema, EXECUTE on functions - Set up properly",
        ],
        exam_focus="Multi-turn flows require state persistence. Analyst REST and Agents support threads. Know how to update parameters dynamically. Understand required privileges.",
    ),
    Subdomain(
        title="4. Use Cortex in Data Pipelines",
        objectives="Add AISQL to ELT; consider token budgets; chunking large text.",
        readings=[
            Reading(
                "AI_COUNT_TOKENS",
                "https://docs.snowflake.com/en/sql-reference/functions/ai_count_tokens",
            ),
            Reading(
                "SPLIT_TEXT_RECURSIVE_CHARACTER",
                "https://docs.snowflake.com/en/sql-reference/functions/split_text_recursive_character-snowflake-cortex",
            ),
        ],
        key_points=[
            "**ELT Integration**: Add AISQL functions to existing pipelines - Transform data with AI",
            "**Token Budgets**: Use [AI_COUNT_TOKENS](https://docs.snowflake.com/en/sql-reference/functions/ai_count_tokens) before processing - Estimate costs and stay within limits",
            "**Chunking**: SPLIT_TEXT_RECURSIVE_CHARACTER for large text - Break into manageable pieces",
            "**Use Cases**: Extract data from text, process transcripts, enrich data, augment datasets, transform data",
            "**SQL Interface**: Use Cortex functions directly in SQL - Native integration with Snowflake",
            "**Cost Management**: Monitor token usage - Critical for production pipelines",
            "**Error Handling**: Use [TRY_COMPLETE](https://docs.snowflake.com/en/sql-reference/functions/try_complete-snowflake-cortex) for graceful failures - Prevent pipeline breaks",
        ],
        exam_focus="AI_COUNT_TOKENS for budget estimation. SPLIT_TEXT_RECURSIVE_CHARACTER for chunking. Know use cases: extraction, enrichment, augmentation, transformation.",
    ),
    Subdomain(
        title="5. Run Third-party Models in Snowflake",
        objectives="Deploy models via SPCS; create compute pools; serve inference.",
        readings=[
            Reading(
                "SPCS overview",
                "https://docs.snowflake.com/en/developer-guide/snowpark-container-services/overview",
            ),
            Reading(
                "Model Registry UI",
                "https://docs.snowflake.com/en/developer-guide/snowflake-ml/model-registry/snowsight-ui",
            ),
        ],
        key_points=[
            "**SPCS (Snowpark Container Services)**: Deploy containerized models - Docker-based deployment",
            "**Compute Pools**: CPU or GPU pools - Provision infrastructure for model serving",
            "**Image Repository**: Docker registry in Snowflake - Store container images",
            "**Specification Files**: YAML service definitions - Configure model services",
            "**Model Registry**: Log and manage models - Centralized model management",
            "**Workflow**: Create compute pool → Create image repo → Deploy service → Serve inference",
            "**Use Cases**: Custom models, fine-tuned models, models not in Cortex catalog",
        ],
        exam_focus="SPCS = containerized deployment. Know compute pools (CPU/GPU), image repositories, specification files. Model Registry for logging. Understand deployment workflow.",
    ),
]

# Domain 2.0 Practice Tasks
DOMAIN_2_PRACTICE_TASKS = [
    PracticeTask(
        description="Structured outputs with response_format + show_details on AI_COMPLETE",
        url="https://docs.snowflake.com/en/sql-reference/functions/ai_complete-single-string",
    ),
    PracticeTask(
        description="Classification & sentiment using AISQL functions",
        url="https://docs.snowflake.com/en/user-guide/snowflake-cortex/aisql",
    ),
    PracticeTask(
        description="Embeddings & similarity with AI_EMBED, VECTOR type & vector functions",
        url="https://docs.snowflake.com/en/sql-reference/functions/ai_embed",
    ),
    PracticeTask(
        description="Document parsing (LAYOUT + OCR) & extraction",
        url="https://docs.snowflake.com/en/sql-reference/functions/ai_parse_document",
    ),
    PracticeTask(
        description="SPCS service (create compute pool; simple service)",
        url="https://docs.snowflake.com/en/developer-guide/snowpark-container-services/overview",
    ),
]

# Domain 2.0 Assignments
DOMAIN_2_ASSIGNMENTS = [
    PracticeTask(
        description="Build a RAG chatbot with Cortex Search + AI_COMPLETE",
        url="https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-search/cortex-search-overview",
    ),
    PracticeTask(
        description="Create a semantic Q&A app using Cortex Analyst + Verified Query Repository",
        url="https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst/verified-query-repository",
    ),
]

