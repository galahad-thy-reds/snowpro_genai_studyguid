# SNOWPRO® SPECIALTY: GEN AI EXAM STUDY GUIDE

**Last Updated:** August 22, 2025

---

## TABLE OF CONTENTS

1. [SNOWPRO® SPECIALTY: GEN AI STUDY GUIDE OVERVIEW](#overview)
2. [RECOMMENDATIONS FOR USING THIS GUIDE](#recommendations)
3. [SNOWPRO® SPECIALTY: GEN AI EXAM CONTENT AND FORMAT](#exam-content)
4. [CERTIFICATION OVERVIEW](#certification-overview)
5. [SNOWPRO® SPECIALTY: GEN AI PREREQUISITE](#prerequisite)
6. [STEPS TO SUCCESS](#steps-to-success)
7. [EXAM DOMAINS AND WEIGHTINGS](#exam-domains)
8. [Domain 1.0: Snowflake for Gen AI Overview](#domain-10)
9. [Domain 2.0: Snowflake Gen AI & LLM Functions](#domain-20)
10. [Domain 3.0: Snowflake Gen AI Governance](#domain-30)
11. [Domain 4.0: Snowflake Document AI](#domain-40)
12. [SNOWPRO® SPECIALTY: GEN AI SAMPLE QUESTIONS](#sample-questions)
13. [MAINTAINING YOUR CERTIFICATION](#certification-maintenance)

---

## SNOWPRO® SPECIALTY: GEN AI STUDY GUIDE OVERVIEW {#overview}

This is a self-paced guide that outlines the Snowflake domains, objectives, and topics covered on the SnowPro Specialty: Gen AI Certification Exam. Use of this study guide does not guarantee certification success.

**Prerequisite:** Holding either the SnowPro Associate: Platform or the SnowPro Core Certification in good standing are prerequisite options for taking the Specialty: Gen AI Certification Exam.

For an overview and more information on all available SnowPro Certifications, please navigate to the Snowflake certification portal.

---

## RECOMMENDATIONS FOR USING THIS GUIDE {#recommendations}

This guide outlines the Snowflake topics and subtopics covered on the exam. Following the topics are additional resources consisting of links to documentation, blogs, and/or exercises designed to support candidates' understanding of Gen AI on Snowflake.

**Estimated length of study time required:** 10 – 13 hours

Some links may have more value for exam preparation than others, depending on the candidate's level of experience. The same amount of time should not be spent on each link. Some links may appear in more than one content domain.

---

## SNOWPRO® SPECIALTY: GEN AI EXAM CONTENT AND FORMAT {#exam-content}

### CERTIFICATION OVERVIEW {#certification-overview}

The SnowPro Specialty: Gen AI Certification Exam tests specialized knowledge, skills, and best practices used to leverage Gen AI methodologies in Snowflake including key concepts, features, and programming constructs. The exam will assess skills through scenario-based questions, interactive questions, and real-world examples.

**This certification will test the candidate's ability to:**

- Define and implement Snowflake Gen AI principles, capabilities, and best practices related to infrastructure, data governance, and cost governance
- Leverage Snowflake Cortex AI features, Large Language Models (LLMs), and offerings to support customer use cases (for example, Cortex Analyst, Cortex Search, Cortex Fine-tuning, Snowflake Copilot)
- Build open-source models with Snowpark Container Services and Snowflake Model Registry (for example, Hugging Face)
- Use Document AI to train and troubleshoot models specific to authentic use cases

**The candidate is expected to have knowledge of:**

- Snowflake Cortex suite of Gen AI features and their underlying models
- Retrieval Augmented Generation (RAG) applications leveraging LLMs

**Target Audience:**

Candidates with one or more years of Gen AI experience with Snowflake, in an enterprise environment. In addition, successful candidates may have advanced proficiency writing code in Python. Previous data engineering and SQL knowledge is assumed.

**This exam is designed for:**

- AI or ML Engineers
- Data Scientists
- Data Engineers
- Data Application Developers
- Data Analysts with programming experience

---

## SNOWPRO® SPECIALTY: GEN AI PREREQUISITE {#prerequisite}

To be eligible to take this exam, candidates must hold an active **SnowPro Associate: Platform** or **SnowPro Core Certification**.

---

## STEPS TO SUCCESS {#steps-to-success}

1. Review this Gen AI Exam Study Guide
2. Attend Snowflake's Instructor-Led Snowflake Gen AI Training
3. Get hands-on experience with our Snowflake x Gen AI: A Cool Collab and Snowflake X Gen AI: LLM Functions
4. Review and study applicable white papers and documentation
5. Get hands-on practical experience with relevant business requirements using Snowflake
6. Attend free Snowflake Webinars
7. Attend Snowflake Virtual Hands-on Labs to gain practical experience
8. Practice with sample questions here
9. Schedule the exam
10. Take the exam!

---

## EXAM DOMAINS AND WEIGHTINGS {#exam-domains}

The following table contains the domains and weightings covered on the exam. It is not a comprehensive listing of all the content that will be presented on the exam.

| Domain | Domain Weightings |
|--------|-------------------|
| 1.0 Snowflake for Gen AI Overview | 26% |
| 2.0 Snowflake Gen AI & LLM Functions | 40% |
| 3.0 Snowflake Gen AI Governance | 22% |
| 4.0 Snowflake Document AI | 12% |

---

# Domain 1.0: Snowflake for Gen AI Overview (26%) {#domain-10}

## 1.1 Define Snowflake's Gen AI principles, features, and best practices

### Core Components

**Snowflake Cortex:**
- Fully managed AI service providing access to industry-leading LLMs and AI models
- Comprehensive suite of Gen AI capabilities within Snowflake

**Large Language Models (LLMs):**
- Industry-leading models integrated within Snowflake
- Support for models from OpenAI, Anthropic, Meta, Mistral AI, DeepSeek

**Cortex Search:**
- Vector search capabilities for RAG applications
- Enterprise search on unstructured data

**Cortex Analyst:**
- Natural language to SQL (NL2SQL) with high accuracy
- Structured/text-to-SQL use cases

**Cortex Fine-tuning:**
- Customize LLMs for specific use cases
- Training data preparation and model deployment

**Cortex Agents:**
- Orchestrate multistep tasks across structured and unstructured data
- REST API access

**Snowflake Copilot:**
- Text-to-SQL assistant for natural language interactions
- Integrated within Snowflake interfaces

### Security, Privacy, Access, and Control Principles

**Role-Based Access Control (RBAC):**
- Manage user permissions based on roles
- Fine-grained access control for AI features

**Guardrails:**
- Safety measures to ensure responsible AI usage
- Cortex Guard for filtering harmful or unsafe responses

**Required Privileges:**
- Necessary permissions for accessing AI features
- Privilege management for different Cortex components

**Cortex LLM Functions:**
- Secure and controlled use of LLM capabilities
- Function-level access control

**Control Model Access:**
- **CORTEX_MODELS_ALLOWLIST parameter** - Specify permitted models
- Restrict access to specific models
- **CORTEX_MODELS** - View available models

### Interfaces

**Cortex LLM Playground (Public Preview):**
- Interactive environment for experimenting with LLMs
- Testing and evaluation interface

**SQL:**
- Standard SQL interface for AI functions
- Native SQL integration for all Cortex functions

**REST API:**
- Programmatic access via REST endpoints
- API-level access control and authentication

### Bringing Your Own Models into Snowflake

**From Hugging Face:**
- Import models from Hugging Face
- Integration with open-source model ecosystem

**Using Snowflake Model Registry:**
- Register and manage custom models within Snowflake
- Model versioning and metadata management
- Custom model deployment

**Using Snowpark Container Services:**
- Deploy and run containerized AI models securely
- Docker image support
- Compute pool management

---

## 1.2 Outline Gen AI capabilities in Snowflake

### Cortex LLM Functions

**Task-specific functions:**
- **CLASSIFY_TEXT** - Classify text into categories
- **EXTRACT_ANSWER** - Extract answers from context
- **PARSE_DOCUMENT** - Parse and extract structured data from documents
- **SENTIMENT** - Analyze sentiment (positive, negative, neutral)
- **SUMMARIZE** - Generate summaries of text
- **TRANSLATE** - Translate text between languages

**General functions:**
- **COMPLETE** - General-purpose text completion
- **COMPLETE Structured Outputs** - Returns structured JSON responses

### Vector Embedding Functions

- **EMBED_TEXT_768** - Generate 768-dimensional embeddings
- **EMBED_TEXT_1024** - Generate 1024-dimensional embeddings

### Vector Functions

- **VECTOR_INNER_PRODUCT** - Compute inner product for similarity
- **VECTOR_L1_DISTANCE** - Compute Manhattan distance
- **VECTOR_L2_DISTANCE** - Compute Euclidean distance
- **VECTOR_COSINE_SIMILARITY** - Compute cosine similarity (most common for embeddings)

### Fine-tuning Capabilities

- Customize LLMs for specific use cases using training data
- Job creation and monitoring
- Model deployment after fine-tuning

### Cortex Search

**RAG use cases:**
- Retrieval Augmented Generation for enhanced information retrieval
- Contextual search and retrieval

**Unstructured data use cases:**
- Search across documents, images, and other unstructured content
- Multimodal search capabilities

**REST APIs:**
- Programmatic access to search functionality
- Integration capabilities

### Cortex Analyst

**Semantic model generation:**
- Creates models that understand data semantics
- Knowledge representation

**Semantic model storage:**
- **Stored in YAML files in a stage** - Semantic models defined in YAML and stored in stages
- **Stored natively in semantic views (Public Preview)** - Native semantic view support

**Structured/text-to-SQL use cases:**
- Convert natural language to SQL queries
- High-accuracy NL2SQL conversion

**REST APIs:**
- API access for integration
- Programmatic access to Analyst capabilities

### Cortex Agents

- **REST APIs** - API-based agent orchestration
- Multistep task orchestration
- Cross-data source integration

### Cross-Region Inference

- **CORTEX_ENABLED_CROSS_REGION parameter** - Specify cross-region model access
  - Can be set to `'DISABLED'` to disable cross-region inference
  - Can be set to specific region codes (e.g., `'AWS_US'`, `'AWS_EU'`) to enable cross-region inference
- **Considerations:**
  - Latency implications
  - Availability trade-offs
  - Cost factors

---

### Domain 1.0 Study Resources

#### Snowflake Documentation

**[Document AI](https://docs.snowflake.com/en/user-guide/ml-powered/document-ai)**
- Enables extraction of structured data from unstructured documents using AI models
- Zero-shot extraction, schema-aware table extractions, multilingual support (29 languages)

**[Cortex LLM REST API](https://docs.snowflake.com/en/developer-guide/cortex/cortex-llm-rest-api)**
- REST API interface for invoking Cortex LLM functions programmatically
- Authentication methods, request/response formats, error handling

**[Cortex Search](https://docs.snowflake.com/en/user-guide/snowflake-cortex/search)**
- Vector search service for RAG applications and enterprise search
- Vector embeddings, similarity search, RAG pipelines

**[Cortex Analyst](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst)**
- Converts natural language questions to SQL queries with high accuracy
- Semantic model generation, Verified Query Repository (VQR), suggested questions

**[Cortex LLM Playground](https://docs.snowflake.com/en/user-guide/snowflake-cortex/llm-playground)**
- Interactive web interface for testing and experimenting with Cortex LLM functions
- Model selection, parameter tuning, prompt testing

**[Vector data types](https://docs.snowflake.com/en/sql-reference/data-types-semistructured)**
- Native VECTOR data type for storing and querying vector embeddings
- Vector dimensions (up to 16,384), embedding storage

**[VECTOR_INNER_PRODUCT](https://docs.snowflake.com/en/sql-reference/functions/vector_inner_product)**
- Calculates inner product between two vectors for similarity computation

**[VECTOR_L1_DISTANCE](https://docs.snowflake.com/en/sql-reference/functions/vector_l1_distance)**
- Calculates L1 (Manhattan) distance between vectors

**[VECTOR_L2_DISTANCE](https://docs.snowflake.com/en/sql-reference/functions/vector_l2_distance)**
- Calculates L2 (Euclidean) distance between vectors

**[VECTOR_COSINE_SIMILARITY](https://docs.snowflake.com/en/sql-reference/functions/vector_cosine_similarity)**
- Calculates cosine similarity between vectors (normalized dot product)

**[Known limitations to Document AI](https://docs.snowflake.com/en/user-guide/ml-powered/document-ai/limitations)**
- Documents constraints and limitations when using Document AI
- File size limits, supported formats, processing time considerations

**[Snowflake Cortex AISQL (including LLM functions)](https://docs.snowflake.com/en/user-guide/snowflake-cortex/ai-sql)**
- Comprehensive guide to Cortex AI functions including LLM capabilities
- Function categories, usage patterns, performance considerations

**[Anomaly Detection (Snowflake ML Functions)](https://docs.snowflake.com/en/user-guide/ml-functions/anomaly-detection)**
- ML-powered anomaly detection using statistical methods

**[Time-Series Forecasting (Snowflake ML Functions)](https://docs.snowflake.com/en/user-guide/ml-functions/forecasting)**
- Automated time-series forecasting using ML models

**[Using Snowflake Copilot](https://docs.snowflake.com/en/user-guide/snowflake-cortex/copilot)**
- Guide to using Snowflake Copilot for natural language to SQL conversion

**[Bring your own model types via serialized files](https://docs.snowflake.com/en/user-guide/ml-powered/bring-your-own-models)**
- Import custom models via serialized files into Snowflake

**[Snowflake Model Registry user interface](https://docs.snowflake.com/en/user-guide/ml-powered/model-registry-ui)**
- Web UI for managing models in the Model Registry

**[COMPLETE (SNOWFLAKE.CORTEX)](https://docs.snowflake.com/en/sql-reference/functions/complete-snowflake-cortex)**
- General-purpose LLM function for text completion tasks
- Model selection, prompt engineering, structured outputs

**[FINETUNE ('CREATE') (SNOWFLAKE.CORTEX)](https://docs.snowflake.com/en/sql-reference/functions/finetune-snowflake-cortex)**
- Function to create fine-tuning jobs for customizing LLMs

**[Cross-region inference](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cross-region-inference)**
- Configure Cortex functions to use models from different regions

**[Fine-tuning (Snowflake Cortex)](https://docs.snowflake.com/en/user-guide/snowflake-cortex/fine-tuning)**
- Complete guide to fine-tuning LLMs in Snowflake

**[GRANT DATABASE ROLE](https://docs.snowflake.com/en/sql-reference/sql/grant-database-role)**
- SQL command to grant database roles for access control

**[Vector Embeddings](https://docs.snowflake.com/en/user-guide/snowflake-cortex/embeddings)**
- Guide to generating and using vector embeddings

#### Reading Assets

**[Best Practices for Getting Started with Snowflake's Document AI (Article)](https://www.snowflake.com/blog/best-practices-for-getting-started-with-snowflakes-document-ai/)**
- Best practices for Document AI implementation

**[Snowflake AI Trust and Safety FAQs (Article)](https://www.snowflake.com/blog/snowflake-ai-trust-and-safety-faqs/)**
- FAQs about AI trust, safety, and data privacy in Snowflake

**[Snowflake's Data Architecture: Enabling AI Apps, Next-Gen Lakehouse Analytics And More (Article)](https://www.snowflake.com/blog/snowflakes-data-architecture-enabling-ai-apps-next-gen-lakehouse-analytics-and-more/)**
- Overview of Snowflake's data architecture supporting AI applications

---

# Domain 2.0: Snowflake Gen AI & LLM Functions (40%) {#domain-20}

## 2.1 Apply Gen AI and LLM functions in Snowflake

### Snowflake Cortex Functions

#### General Functions

- **COMPLETE** - Generates text completions using selected LLM
- **COMPLETE Structured Outputs** - Returns structured JSON responses with schema validation

#### Task-Specific Functions

- **CLASSIFY_TEXT** - Classifies text into user-defined categories
- **EXTRACT_ANSWER** - Extracts answers from provided context
- **PARSE_DOCUMENT** - Parses and extracts structured data from documents
- **SENTIMENT** - Analyzes sentiment (positive, negative, neutral)
- **SUMMARIZE** - Generates summaries of text
- **TRANSLATE** - Translates text between supported languages

#### Vector Embedding Functions

- **EMBED_TEXT_768** - Generates 768-dimensional embeddings
- **EMBED_TEXT_1024** - Generates 1024-dimensional embeddings

#### Vector Functions

- **VECTOR_INNER_PRODUCT** - Computes inner product for similarity
- **VECTOR_L1_DISTANCE** - Computes Manhattan distance
- **VECTOR_L2_DISTANCE** - Computes Euclidean distance
- **VECTOR_COSINE_SIMILARITY** - Computes cosine similarity (most common for embeddings)

#### Helper Functions

- **COUNT_TOKENS** - Counts tokens in text (important for cost estimation)
- **TRY_COMPLETE** - Error-handling wrapper that returns NULL on failure instead of error
- **SPLIT_TEXT_RECURSIVE_CHARACTER** - Splits text into chunks for processing

### Additional Services

- **Cortex Search** - Vector search for RAG
- **Cortex Analyst** - NL2SQL service
- **Cortex Fine-tuning** - Custom model training
- **Cortex Agents** - Agent orchestration

### Choosing a Model

**Considerations:**
- **Capability** - Task complexity requirements
- **Latency** - Response time requirements
- **Cost** - Token pricing and usage patterns

**Model Selection Guidelines:**
- Large models: Higher capability, higher latency and cost
- Small models: Lower latency and cost, suitable for simpler tasks

---

## 2.2 Perform data analysis given a use case

### Use Fully-Managed LLMs, RAG, and Text-to-SQL Services

#### Unstructured Data

- **CORTEX.PARSE_DOCUMENT** - Extract structured data from documents
- Document processing and extraction

#### Structured Data

**Cortex Analyst:**
- **Cortex Analyst Verified Query Repository (VQR)** - Pre-validated queries for common questions
- **Integration with Cortex Search** - Combine search with analysis
- **Suggested Questions** - AI-generated question suggestions
- **custom_instructions field** - Customize analyst behavior
- **Performance considerations:**
  - Latency optimization
  - Fine-tuning impact
  - Model size selection

---

## 2.3 Build chat interfaces to interact with data in Snowflake

### Set up the Snowflake Environment

- **Required privileges** - USAGE on database/schema, EXECUTE on functions
- Environment configuration

### Invoke Cortex Functions within Application Code

- Integration with Streamlit
- Python and JavaScript implementations
- API integration

### Chat Conversations

- **Multi-turn architecture** - Context preservation across messages
- Conversation management
- **Update parameters** - Dynamic parameter adjustment (temperature, max_tokens, etc.)

---

## 2.4 Use Snowflake Cortex functions in data pipelines

### Snowflake Cortex SQL Interface

**Use Cases:**
- **Extracting data from text using COMPLETE** - Parse unstructured text
- **Transcripts** - Process audio/video transcripts
- **Data enrichment** - Add AI-generated metadata
- **Data augmentation** - Generate synthetic data
- **Data transformations** - AI-powered data cleaning and formatting

---

## 2.5 Run third-party models in Snowflake

### Using Snowpark Container Services

**Environment setup:**
- Prerequisites and configuration

**Docker images:**
- Container image requirements

**Specification files:**
- Service definition YAML

**Infrastructure:**
- **Create compute pool** - Infrastructure provisioning
- **Create image repository** - Docker registry setup

### Using the Snowflake Model Registry

**Model Management:**
- **Logging the model** - Register model with metadata
- **Calling the model** - Inference execution via registry APIs

---

### Domain 2.0 Study Resources

#### Snowflake Documentation

**[Cortex Agents](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents)**
- Guide to creating and managing AI agents that orchestrate multistep tasks

**[AI_PARSE_DOCUMENT (SNOWFLAKE.CORTEX)](https://docs.snowflake.com/en/sql-reference/functions/ai_parse_document)**
- Function to parse documents and extract structured information (replaces SNOWFLAKE.CORTEX.PARSE_DOCUMENT)

**[Cortex Analyst Verified Query Repository](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst/verified-query-repository)**
- Repository of verified SQL queries for common questions

**[Suggested Questions in Cortex Analyst](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst/suggested-questions)**
- Feature that suggests questions based on available data

**[Improve literal search to enhance Cortex Analyst responses](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst/literal-search)**
- Techniques to improve literal search capabilities

**[Cortex Analyst semantic model specification](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst/semantic-model-spec)**
- YAML format specification for semantic models

**[Cortex Search tutorials](https://docs.snowflake.com/en/user-guide/snowflake-cortex/search/tutorials)**
- Step-by-step tutorials for implementing Cortex Search

**[Dynamic tables compared to streams and tasks and to materialized views](https://docs.snowflake.com/en/user-guide/dynamic-tables/about)**
- Comparison of dynamic tables with other Snowflake features

**[AI_COMPLETE Structured Outputs](https://docs.snowflake.com/en/user-guide/snowflake-cortex/structured-outputs)**
- Guide to using COMPLETE function with structured JSON outputs

**[Snowpark Container Services](https://docs.snowflake.com/en/user-guide/snowpark-container-services-overview)**
- Overview of containerized service deployment in Snowflake

**[Working with an image registry and repository](https://docs.snowflake.com/en/user-guide/snowpark-container-services/repositories)**
- Guide to managing Docker images in Snowflake

**[Snowflake Model Registry](https://docs.snowflake.com/en/user-guide/ml-powered/model-registry)**
- Centralized registry for managing ML models

**[Snowflake ML: End-to-End Machine Learning](https://docs.snowflake.com/en/user-guide/ml-powered/introduction)**
- Comprehensive guide to ML capabilities in Snowflake

**[Model Serving in Snowpark Container Services](https://docs.snowflake.com/en/user-guide/snowpark-container-services/model-serving)**
- Guide to serving models via container services

**[Snowpark Container Services Tutorials](https://docs.snowflake.com/en/user-guide/snowpark-container-services/tutorials)**
- Tutorials for container service implementation

**[SENTIMENT (SNOWFLAKE.CORTEX)](https://docs.snowflake.com/en/sql-reference/functions/sentiment-snowflake-cortex)**
- Function for sentiment analysis

**[TRANSLATE (SNOWFLAKE.CORTEX)](https://docs.snowflake.com/en/sql-reference/functions/translate-snowflake-cortex)**
- Function for language translation

**[TRY_COMPLETE (SNOWFLAKE.CORTEX)](https://docs.snowflake.com/en/sql-reference/functions/try_complete-snowflake-cortex)**
- Error-handling version of COMPLETE function

**[CLASSIFY_TEXT (SNOWFLAKE.CORTEX)](https://docs.snowflake.com/en/sql-reference/functions/classify_text-snowflake-cortex)**
- Function for text classification

**[SUMMARIZE (SNOWFLAKE.CORTEX)](https://docs.snowflake.com/en/sql-reference/functions/summarize-snowflake-cortex)**
- Function for text summarization

**[EXTRACT_ANSWER (SNOWFLAKE.CORTEX)](https://docs.snowflake.com/en/sql-reference/functions/extract_answer-snowflake-cortex)**
- Function to extract specific answers from context

**[snowflake.ml.registry.Registry](https://docs.snowflake.com/en/developer-guide/snowpark-ml-python-reference/registry)**
- Python API for Model Registry operations

**[CREATE COMPUTE POOL](https://docs.snowflake.com/en/sql-reference/sql/create-compute-pool)**
- SQL command to create compute pools for container services

#### Quickstarts and Tutorials

**[Fine-Tuning an LLM in Snowpark Container Services with AutoTrain](https://docs.snowflake.com/en/developer-guide/snowpark-container-services/tutorials/autotrain-finetuning)**
- Tutorial for fine-tuning LLMs using AutoTrain in container services

**[Deploy and Fine-tune Open Source Llama 2 in Snowpark Container Services](https://docs.snowflake.com/en/developer-guide/snowpark-container-services/tutorials/llama2-finetuning)**
- Step-by-step guide for deploying and fine-tuning Llama 2

**[Build a basic LLM chat app](https://docs.snowflake.com/en/developer-guide/snowpark-container-services/tutorials/basic-llm-chat-app)**
- Tutorial for building a chat application with LLMs

#### Reading Assets

**[Snowflake Cortex Analyst: Support for Multi-turn Conversation (Article)](https://www.snowflake.com/blog/snowflake-cortex-analyst-support-for-multi-turn-conversation/)**
- Article about multi-turn conversation support in Cortex Analyst

**[AI-Infused Pipelines with Snowflake Cortex (Blog)](https://www.snowflake.com/blog/ai-infused-pipelines-with-snowflake-cortex/)**
- Blog post about integrating AI into data pipelines

**[Snowpark Container Services — A Tech Primer (Blog)](https://www.snowflake.com/blog/snowpark-container-services-a-tech-primer/)**
- Technical overview of Snowpark Container Services

---

# Domain 3.0: Snowflake Gen AI Governance (22%) {#domain-30}

## 3.1 Set up model access controls

### Limits on Which Models Can Be Used

**Restrict access to specific models:**
- **CORTEX_MODELS_ALLOWLIST parameter** - Restrict which models can be used
- Fine-grained model permissions
- Model-level access control

**Affected Interfaces:**
- **Cortex LLM REST API** - API-level access control
- **COMPLETE (SNOWFLAKE.CORTEX)** - Function-level controls
- **TRY_COMPLETE (SNOWFLAKE.CORTEX)** - Alternative function with error handling
- **Cortex LLM Playground (Public Preview)** - UI access restrictions

### Data Safety and Security Considerations

- **Is data leaving/going to LLMs?** - Data residency verification
- Ensure data doesn't leave Snowflake
- Data privacy and compliance

### REST API Authentication Methods

- OAuth authentication
- Key pairs
- Token-based authentication

---

## 3.2 Set guardrails to filter out harmful or unsafe LLM responses

### Cortex Guard

**COMPLETE arguments:**
- Guard parameter in COMPLETE function
- Safety filtering configuration

**Methods to reduce model hallucinations:**
- Prompt engineering
- Temperature control
- Context management

**Methods to reduce bias:**
- Diverse training data considerations
- Output filtering
- Evaluation criteria

**Error conditions:**
- Handling unsafe content detection
- Error response handling

---

## 3.3 Monitor and optimize Snowflake Cortex costs

### Cortex Search Costs

**Different types of costs:**
- **Virtual warehouse costs** - Compute charges
- **EMBED_TEXT costs** - Embedding generation charges
- **Serving costs** - Search query execution charges

### Cortex Analyst Costs

- Query execution costs
- Model inference costs

### Cortex LLM Functions Costs

**Cost Optimization:**
- **Minimize tokens** - Optimize prompts to reduce token usage
- **Token cost implications** - Understanding pricing models
- **Tracking model usage and consumption** - Usage monitoring
- **Usage quotas** - Set spending limits

### Monitoring Tools

- **Snowflake Service Consumption Table** - Overall service usage
- **CORTEX_FUNCTIONS_USAGE_HISTORY view** - Function-level usage tracking
- **CORTEX_FUNCTIONS_QUERY_USAGE_HISTORY view** - Query-level usage details

---

## 3.4 Use Snowflake AI observability tools

### Snowflake AI Observability Features (Public Preview)

**Evaluation metrics:**
- Accuracy measurements
- Relevance scoring
- Latency measurements

**Comparisons:**
- A/B testing between models/configurations
- Performance benchmarking

**Tracing:**
- End-to-end request tracing
- Request flow analysis

**Logging:**
- Detailed execution logs
- Audit trails

**Event tables:**
- Structured event storage for analysis
- Historical event tracking

**Implementation methods:**
- SDK integration
- API usage
- **Trulens SDK** - Third-party observability library integration

---

### Domain 3.0 Study Resources

#### Snowflake Documentation

**[Snowflake Service Consumption Table](https://docs.snowflake.com/en/sql-reference/account-usage/service-consumption)**
- Account-level view of service consumption and costs

**[Snowpark-optimized warehouse](https://docs.snowflake.com/en/user-guide/warehouses-overview#snowpark-optimized-warehouses)**
- Warehouse type optimized for ML/AI workloads

**[Evaluate AI applications](https://docs.snowflake.com/en/user-guide/cortex/ai-observability/evaluation)**
- Guide to evaluating AI application performance

**[AI Observability in Snowflake Cortex](https://docs.snowflake.com/en/user-guide/cortex/ai-observability)**
- Comprehensive observability features for AI applications

**[Cortex Analyst administrator monitoring](https://docs.snowflake.com/en/user-guide/cortex/analyst/admin-monitoring)**
- Monitoring tools for Cortex Analyst administrators

**[Understanding cost for Cortex Search Services](https://docs.snowflake.com/en/user-guide/cortex/search/cost)**
- Detailed cost breakdown for Cortex Search

**[CORTEX_FUNCTIONS_USAGE_HISTORY view](https://docs.snowflake.com/en/sql-reference/account-usage/cortex_functions_usage_history)**
- Historical view of Cortex function usage

**[METERING_DAILY_HISTORY view](https://docs.snowflake.com/en/sql-reference/account-usage/metering_daily_history)**
- Daily aggregated metering data

**[CORTEX_SEARCH_DAILY_USAGE_HISTORY view](https://docs.snowflake.com/en/sql-reference/account-usage/cortex_search_daily_usage_history)**
- Daily Cortex Search usage statistics

**[CORTEX_DOCUMENT_PROCESSING_USAGE_HISTORY view](https://docs.snowflake.com/en/sql-reference/account-usage/cortex_document_processing_usage_history)**
- Historical Document AI processing usage

**[snowflake.cortex.CompleteOptions](https://docs.snowflake.com/en/developer-guide/cortex/cortex-llm-rest-api/complete-options)**
- API reference for COMPLETE function options

---

# Domain 4.0: Snowflake Document AI (12%) {#domain-40}

## 4.1 Set up Document AI

### Virtual Warehouse, Database, and Schema Considerations

- Compute resources for processing
- Organization and access control
- Resource allocation

### Roles and Privileges

- **USAGE** - Access to database/schema
- **OPERATE** - Execute operations
- **CREATE SNOWFLAKE.ML.DOCUMENT_INTELLIGENCE** - Create Document AI models
- **CREATE MODEL** - General model creation privilege

---

## 4.2 Prepare documents for Document AI

### Upload Documents

- Stage documents for processing
- Document organization

### Train the Model

- Create model builds with training data
- Training data preparation

### Requirements

- **Formats** - Supported file types (PDF, images, etc.)
- **Size limits** - Maximum file sizes

### Question Optimization Best Practices

- Craft effective extraction questions
- Question specificity and clarity
- Schema design for extraction

---

## 4.3 Extract values from documents using Document AI

### Conditions

- Specify extraction criteria
- Query conditions

### `<model_build_name>!PREDICT` Query

- Execute predictions using trained model
- Result interpretation

### Automation of Data Pipelines

- Integrate into ETL workflows
- Pipeline automation patterns

---

## 4.4 Troubleshoot Document AI given a use case

### Extracting Query Errors

- Common error scenarios and solutions
- Error diagnosis

### GET_PRESIGNED_URL Function

- Generate URLs for document access
- Secure document retrieval

### Requirements and Privileges

- Permission issues resolution
- Access control troubleshooting

### Cost and Best Practices Considerations

- Optimization strategies
- Cost management
- Performance tuning

---

### Domain 4.0 Study Resources

#### Snowflake Documentation

**[Document AI](https://docs.snowflake.com/user-guide/ml-powered/document-ai)**
- Complete overview of Document AI capabilities

**[Setting up Document AI](https://docs.snowflake.com/en/user-guide/ml-powered/document-ai/setup)**
- Step-by-step setup instructions

**[Troubleshooting Document AI](https://docs.snowflake.com/en/user-guide/ml-powered/document-ai/troubleshooting)**
- Common issues and solutions

**[Cost governance of Document AI](https://docs.snowflake.com/en/user-guide/ml-powered/document-ai/cost-governance)**
- Cost management strategies

**[Create a document processing pipeline](https://docs.snowflake.com/en/user-guide/ml-powered/document-ai/pipeline)**
- Guide to building automated pipelines

**[Prepare your documents for Document AI](https://docs.snowflake.com/en/user-guide/ml-powered/document-ai/prepare)**
- Document preparation guidelines

**[Question optimization for extracting information with Document AI](https://docs.snowflake.com/en/user-guide/ml-powered/document-ai/question-optimization)**
- Best practices for crafting extraction questions

**[Known limitations to Document AI](https://docs.snowflake.com/en/user-guide/ml-powered/document-ai/limitations)**
- Constraints and limitations

**[Extract information with Document AI](https://docs.snowflake.com/en/user-guide/ml-powered/document-ai/extract)**
- Guide to extraction process

**[DOCUMENT_INTELLIGENCE (SNOWFLAKE.ML)](https://docs.snowflake.com/en/sql-reference/sql/create-document-intelligence)**
- SQL reference for Document Intelligence model creation

**[CREATE STAGE](https://docs.snowflake.com/en/sql-reference/sql/create-stage)**
- SQL command for creating stages (document storage)

**[`<model_build_name>!PREDICT`](https://docs.snowflake.com/en/sql-reference/functions/predict-document-intelligence)**
- Function reference for Document AI predictions

---

# SNOWPRO® SPECIALTY: GEN AI SAMPLE QUESTIONS {#sample-questions}

## Question 1: Cost Monitoring

**Question:** A Gen AI Specialist needs to analyze the daily costs incurred for AI services in Snowflake. Which query will retrieve the credit consumption from Snowflake's metadata objects for data usage?

**Options:**
- A. `SELECT * FROM SNOWFLAKE.ACCOUNT_USAGE.QUERY_HISTORY WHERE SERVICE_TYPE='AI_SERVICES';`
- B. `SELECT * FROM SNOWFLAKE.INFORMATION_SCHEMA.METERING_HISTORY WHERE SERVICE_TYPE='AI_SERVICES';`
- C. `SELECT * FROM SNOWFLAKE.ACCOUNT_USAGE.METERING_HISTORY WHERE SERVICE_TYPE='AI_SERVICES';`
- D. `SELECT * FROM SNOWFLAKE.ACCOUNT_USAGE.METERING_DAILY_HISTORY WHERE SERVICE_TYPE='AI_SERVICES';`

**Answer:** D - `SELECT * FROM SNOWFLAKE.ACCOUNT_USAGE.METERING_DAILY_HISTORY WHERE SERVICE_TYPE='AI_SERVICES';`

---

## Question 2: Multi-turn Conversations

**Question:** What is the primary role of memory in a multi-turn chat conversation using a Gen AI model in Snowflake Cortex Analyst?

**Options:**
- A. To securely store user credentials
- B. To increase the speed of response generation
- C. To maintain context throughout multiple requests
- D. To limit the number of tokens processed for each request

**Answer:** C - To maintain context throughout multiple requests

---

## Question 3: Document AI Error

**Question:** A Gen AI Specialist is using Document AI to create a model. When creating a model build with a name unique to the specified schema, this error is returned: "Unable to create a build on the specified database and schema. Please check the documentation to learn more." What would cause this error?

**Options:**
- A. There is a model build with the same name in another schema in the database.
- B. The CREATE SNOWFLAKE.ML.DOCUMENT_INTELLIGENCE privilege has not been granted to the role the Specialist is using.
- C. The USAGE privilege on the database used to create the model build has not been granted to the role the Specialist is using.
- D. The SNOWFLAKE.DOCUMENT_INTELLIGENCE_CREATOR database role has not been granted to the role the Specialist is using.

**Answer:** B - The CREATE SNOWFLAKE.ML.DOCUMENT_INTELLIGENCE privilege has not been granted to the role the Specialist is using.

---

## Question 4: Model Access Control

**Question:** Which parameter can be used by administrators to restrict access to specific LLMs within Snowflake?

**Options:**
- A. NETWORK_POLICY
- B. SAML_IDENTITY_PROVIDER
- C. CORTEX_MODELS_ALLOWLIST
- D. CORTEX_ENABLED_CROSS_REGION

**Answer:** C - CORTEX_MODELS_ALLOWLIST

---

## Question 5: Function Selection

**Question:** Which Snowflake Cortex LLM function should be used to generate an instructional lesson plan based on a prompt?

**Options:**
- A. COMPLETE
- B. EXTRACT ANSWER
- C. SUMMARIZE
- D. TRANSLATE

**Answer:** A - COMPLETE

---

# MAINTAINING YOUR CERTIFICATION {#certification-maintenance}

All Snowflake Certifications expire two (2) years after your certification issue date.

SnowPro Certifications can now be recertified through the **Snowflake Continuing Education (CE) program** which includes these options:

- Completion of eligible Snowflake [Instructor Led (ILT) Training Courses](https://www.snowflake.com/en/training/)
- Earning of an equivalent or higher-level SnowPro Certification

**Note:** You must have a valid Certification to participate in the Continuing Education (CE) program.

---

## DISCLAIMER

The information provided in this guide is provided for your internal purposes only and may not be provided to third parties.

IN ADDITION, THIS STUDY GUIDE IS PROVIDED "AS IS". NEITHER SNOWFLAKE NOR ITS SUPPLIERS MAKES ANY OTHER WARRANTIES, EXPRESS OR IMPLIED, STATUTORY OR OTHERWISE, INCLUDING BUT NOT LIMITED TO WARRANTIES OF MERCHANTABILITY, TITLE, FITNESS FOR A PARTICULAR PURPOSE OR NONINFRINGEMENT.

---

**Last Updated:** August 22, 2025
