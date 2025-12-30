# SnowPro GenAI Study Guide

An interactive Streamlit application to help you prepare for the **SnowPro Specialty: Gen AI Certification**.

## 🎯 Overview

This study guide is based on the official SnowPro GenAI Study Plan V2 and provides:
- **7 Interactive Sections** covering all exam domains
- **Progress Tracking** to monitor your study journey
- **Practice Tasks** with links to official documentation
- **Capstone Project** for hands-on experience
- **Exam Prep** with key concepts and scenarios

## 📚 Course Structure

| Domain | Weight | Time |
|--------|--------|------|
| Domain 1.0: Snowflake for Gen AI Overview | 26% | 3.0 h |
| Domain 2.0: Snowflake Gen AI & LLM Functions | 40% | 4.5 h |
| Domain 3.0: Snowflake Gen AI Governance | 22% | 2.0 h |
| Domain 4.0: Snowflake Document AI | 12% | 1.5 h |
| Capstone: Document Processing Framework | — | 2.0 h |
| Final Exam Prep | — | 1.0 h |

**Total Study Time**: ~14 hours

## 🚀 Getting Started

### Prerequisites

- Python 3.10
- `uv` package manager ([Installation Guide](https://github.com/astral-sh/uv))
- Snowflake account (optional, for hands-on practice)

### Installation

1. **Clone or navigate to the project directory**

2. **Install uv** (if not already installed):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

3. **Create virtual environment**:
   ```bash
   uv venv
   ```

4. **Activate virtual environment**:
   ```bash
   # Linux/Mac
   source .venv/bin/activate
   
   # Windows
   .venv\Scripts\activate
   ```

5. **Install dependencies**:
   ```bash
   uv pip install -r requirements.txt
   ```

6. **Configure environment** (optional):
   ```bash
   cp .env.example .env
   # Edit .env with your Snowflake credentials (if needed)
   ```

### Running the Application

```bash
# Using uv (recommended)
uv run streamlit run app.py

# Or with activated virtual environment
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## 📁 Project Structure

```
snowpro_genai_studyguid/
├── app.py                    # Main Streamlit entry point
├── pages/                     # Multi-page app structure (presentation layer)
│   ├── 1_📚_Introduction.py
│   ├── 2_🔍_Domain_1_Overview.py
│   ├── 3_🤖_Domain_2_GenAI_Functions.py
│   ├── 4_🔒_Domain_3_Governance.py
│   ├── 5_📄_Domain_4_Document_AI.py
│   ├── 6_🎯_Capstone.py
│   └── 7_📝_Exam_Prep.py
├── src/
│   ├── config.py            # Configuration and constants
│   ├── content/             # Content modules (data layer)
│   │   ├── __init__.py
│   │   └── domain_1.py      # Domain 1.0 content (subdomains, tasks)
│   ├── data_loader.py       # Load and parse study plan content
│   ├── snowflake_utils.py   # Snowflake connection helpers
│   └── utils.py             # Utility functions
├── docs/                     # Documentation
│   ├── SnowPro_GenAI_Study_Plan_V2.md
│   └── project_summary.md
├── requirements.txt          # Python dependencies
├── .python-version          # Python 3.10
└── README.md                # This file
```

### Architecture

The project follows a **separation of concerns** pattern:

- **`pages/`**: Streamlit page files (presentation layer) - handle UI rendering
- **`src/content/`**: Content modules (data layer) - store structured content using dataclasses
- **`src/`**: Utility modules - shared functionality and configuration

This separation allows:
- Content updates without touching UI code
- Reusable content across different views
- Type-safe content structures
- Easier testing and maintenance

## 🛠️ Development

### Using uv for Development

```bash
# Install new package
uv pip install package-name

# Update requirements.txt
uv pip freeze > requirements.txt

# Sync dependencies (exact versions)
uv pip sync requirements.txt

# Run with uv
uv run streamlit run app.py
```

### Code Style

- Follow PEP 8 conventions
- Use type hints (Python 3.10+)
- Maximum line length: 100 characters
- Google-style docstrings

### Content Architecture

**Content Separation Pattern:**
- Store section content in `src/content/` modules (e.g., `domain_1.py`)
- Use dataclasses from `src/data_loader.py` (`Subdomain`, `Reading`, `PracticeTask`)
- Page files import and render content, keeping presentation logic separate
- Example: `pages/2_🔍_Domain_1_Overview.py` imports from `src.content.domain_1`

**Adding New Content:**
1. Create content file in `src/content/` (e.g., `domain_2.py`)
2. Define content using dataclasses (`Subdomain`, `PracticeTask`, etc.)
3. Export constants (e.g., `DOMAIN_2_SUBDOMAINS`, `DOMAIN_2_PRACTICE_TASKS`)
4. Import in page file and render

## 📖 Study Guide Features

- **Interactive Navigation**: Sidebar navigation with progress tracking
- **Section Completion**: Mark sections as complete to track progress
- **Documentation Links**: Direct links to official Snowflake documentation
- **Practice Tasks**: Hands-on exercises for each domain
- **Capstone Project**: Complete Document Processing Framework implementation
- **Exam Prep**: Key concepts, scenarios, and exam day tips

## 🔗 Resources

- [Snowflake Cortex Documentation](https://docs.snowflake.com/en/user-guide/snowflake-cortex)
- [SnowPro Certification Portal](https://www.snowflake.com/certifications/)
- [Study Plan Source](docs/SnowPro_GenAI_Study_Plan_V2.md)

## 📝 Notes

- This study guide is based on the official SnowPro GenAI Study Plan V2 (Dec 26, 2025)
- Always refer to the latest Snowflake documentation for the most current information
- Prefer "Exam-Safe" (GA/Stable) features over preview features
- Hands-on practice is essential for exam success

## 🤝 Contributing

This is a personal study guide project. Feel free to fork and customize for your own use.

## 📄 License

This project is for educational purposes only. All Snowflake documentation and resources are property of Snowflake Inc.

---

**Good luck with your certification!** ❄️🎓

