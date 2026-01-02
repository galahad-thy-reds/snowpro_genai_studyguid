"""Content for Domain 4.0: Snowflake Document AI."""

from __future__ import annotations

from src.data_loader import PracticeTask, Reading, Subdomain

# Domain 4.0 Subdomains
DOMAIN_4_SUBDOMAINS = [
    Subdomain(
        title="1. Setup & Privileges",
        objectives="Create warehouse/schema/stage; grant roles (creator & usage); configure encryption.",
        readings=[
            Reading(
                "Setting up Document AI",
                "https://docs.snowflake.com/en/user-guide/snowflake-cortex/document-ai/setting-up",
            ),
        ],
        key_points=[
            "**Virtual warehouse, database, and schema considerations** - Compute resources for processing, organization and access control, resource allocation",
            "**Roles and privileges** - Required permissions for Document AI operations",
            "**USAGE** - Access to database/schema",
            "**OPERATE** - Execute operations",
            "**CREATE SNOWFLAKE.ML.DOCUMENT_INTELLIGENCE** - Create Document AI models (required privilege)",
            "**CREATE MODEL** - General model creation privilege",
            "**Configure encryption** - Use SNOWFLAKE_SSE for internal stages (required for Document AI)",
            "**Stage setup** - Create internal stages with proper encryption for document storage",
        ],
        exam_focus="Required privileges: USAGE, OPERATE, CREATE SNOWFLAKE.ML.DOCUMENT_INTELLIGENCE, CREATE MODEL. Use SNOWFLAKE_SSE encryption for internal stages. Configure warehouse/schema/stage properly.",
    ),
    Subdomain(
        title="2. Prepare Documents",
        objectives="Meet format/size/page limits; use SNOWFLAKE_SSE for internal stages.",
        readings=[
            Reading(
                "Working with Document AI (overview & requirements)",
                "https://docs.snowflake.com/en/user-guide/snowflake-cortex/document-ai/overview",
            ),
        ],
        key_points=[
            "**Upload documents** - Stage documents for processing, document organization",
            "**Train the model** - Create model builds with training data, training data preparation",
            "**Requirements** - Format and size constraints",
            "**Formats** - Supported file types (PDF, DOCX, images, etc.)",
            "**Size limits** - Maximum file sizes (check current documentation for limits)",
            "**Page limits** - Maximum pages per document (check current documentation)",
            "**Use SNOWFLAKE_SSE for internal stages** - Required encryption for Document AI stages",
            "**Question optimization best practices** - Craft effective extraction questions, question specificity and clarity, schema design for extraction",
            "**Internal stages** - Documents must be in internal stages with SNOWFLAKE_SSE encryption",
        ],
        exam_focus="Format/size/page limits must be met. SNOWFLAKE_SSE encryption required for internal stages. Question optimization best practices for effective extraction. Understand supported formats and constraints.",
    ),
    Subdomain(
        title="3. Extract Values",
        objectives="Use AI_EXTRACT prompts to capture entities/tables; combine with AI_PARSE_DOCUMENT layout mode.",
        readings=[
            Reading(
                "Parsing documents (guide)",
                "https://docs.snowflake.com/en/user-guide/snowflake-cortex/parse-document",
            ),
            Reading(
                "Document Processing Playground",
                "https://docs.snowflake.com/en/user-guide/snowflake-cortex/document-processing-playground",
            ),
            Reading(
                "AI_EXTRACT",
                "https://docs.snowflake.com/en/sql-reference/functions/ai_extract",
            ),
            Reading(
                "AI_PARSE_DOCUMENT",
                "https://docs.snowflake.com/en/sql-reference/functions/ai_parse_document",
            ),
        ],
        key_points=[
            "**Use AI_EXTRACT prompts** - Capture entities/tables from documents using prompt-based extraction",
            "**Combine with AI_PARSE_DOCUMENT layout mode** - Parse document structure first, then extract values",
            "**AI_PARSE_DOCUMENT** - Parse documents to extract layout (markdown output), supports LAYOUT/OCR/TEXT modes",
            "**AI_EXTRACT** - Extract structured data using prompts, capture entities and tables",
            "**Document Processing Playground** - Interactive tool for testing parsing and extraction (recommended workflow)",
            "**Conditions** - Specify extraction criteria, query conditions for filtering",
            "**Automation of data pipelines** - Integrate into ETL workflows, pipeline automation patterns",
            "**Workflow**: Parse document (AI_PARSE_DOCUMENT) → Extract values (AI_EXTRACT prompts) → Process results",
            "**Important**: Older `<model_build_name>!PREDICT` paths are deprecated - Use AISQL functions (AI_EXTRACT, AI_PARSE_DOCUMENT) instead",
        ],
        exam_focus="AI_EXTRACT for entity extraction with prompts. AI_PARSE_DOCUMENT for layout parsing. Combine both for document processing. Document Processing Playground for testing. Prefer AISQL functions over deprecated PREDICT paths.",
    ),
    Subdomain(
        title="4. Troubleshooting, Cost & Limitations",
        objectives="Solve presigned URL expiry, stage encryption mismatch, and doc limits; manage costs.",
        readings=[
            Reading(
                "Troubleshooting Document AI",
                "https://docs.snowflake.com/en/user-guide/snowflake-cortex/document-ai/troubleshooting",
            ),
            Reading(
                "Cost governance of Document AI",
                "https://docs.snowflake.com/en/user-guide/snowflake-cortex/document-ai/cost-governance",
            ),
            Reading(
                "Known limitations to Document AI",
                "https://docs.snowflake.com/en/user-guide/snowflake-cortex/document-ai/known-limitations",
            ),
        ],
        key_points=[
            "**Extracting query errors** - Common error scenarios and solutions, error diagnosis",
            "**GET_PRESIGNED_URL function** - Generate URLs for document access, secure document retrieval",
            "**Presigned URL expiry** - URLs expire after 24 hours, regenerate as needed for batch processing",
            "**Stage encryption mismatch** - Ensure SNOWFLAKE_SSE encryption matches Document AI requirements",
            "**Document limits** - Size limits, page limits, format constraints",
            "**Requirements and privileges** - Permission issues resolution, verify all required privileges",
            "**Cost and best practices considerations** - Monitor Document AI costs, optimize processing",
            "**CORTEX_DOCUMENT_PROCESSING_USAGE_HISTORY view** - Monitor Document AI usage and costs",
            "**Known limitations** - Review documentation for current limitations and constraints",
            "**Troubleshooting steps** - Verify stage encryption, check privileges, validate document formats, handle URL expiry",
        ],
        exam_focus="Presigned URL expiry (24 hours). Stage encryption mismatch (use SNOWFLAKE_SSE). GET_PRESIGNED_URL function. Document limits and format constraints. Cost monitoring via usage views. Troubleshooting privilege and format issues.",
    ),
]

# Domain 4.0 Practice Tasks
DOMAIN_4_PRACTICE_TASKS = [
    PracticeTask(
        description="Create stage with SNOWFLAKE_SSE and upload PDFs",
        url="https://docs.snowflake.com/en/user-guide/snowflake-cortex/document-ai/setting-up",
    ),
    PracticeTask(
        description="Parse & extract invoice fields in Playground",
        url="https://docs.snowflake.com/en/user-guide/snowflake-cortex/document-processing-playground",
    ),
    PracticeTask(
        description="Generate presigned URL for batch processing",
        url="https://docs.snowflake.com/en/user-guide/snowflake-cortex/document-ai/troubleshooting",
    ),
]

