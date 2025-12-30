"""Load and parse study plan content from markdown file."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import streamlit as st


@dataclass(frozen=True)
class Reading:
    """Represents a reading resource."""
    title: str
    url: str


@dataclass(frozen=True)
class Objective:
    """Represents a learning objective."""
    description: str
    readings: list[Reading]


@dataclass(frozen=True)
class PracticeTask:
    """Represents a practice task."""
    description: str
    url: str | None = None


@dataclass(frozen=True)
class Section:
    """Represents a study section."""
    title: str
    time: str
    weight: int | None
    objectives: list[Objective]
    readings: list[Reading]
    practice_tasks: list[PracticeTask]
    assignments: list[PracticeTask]
    lab_steps: list[str]


@st.cache_data
def load_study_plan(file_path: str = "docs/SnowPro_GenAI_Study_Plan_V2.md") -> str:
    """Load the study plan markdown file."""
    path = Path(file_path)
    
    if not path.exists():
        raise FileNotFoundError(f"Study plan not found at {file_path}")
    
    return path.read_text(encoding="utf-8")


def parse_reading(line: str) -> Reading | None:
    """Parse a reading line from markdown."""
    # Match markdown link format: - [Title](URL) or - URL
    link_pattern = r'\[([^\]]+)\]\(([^\)]+)\)'
    url_pattern = r'https?://[^\s\)]+'
    
    match = re.search(link_pattern, line)
    if match:
        title, url = match.groups()
        return Reading(title=title.strip(), url=url.strip())
    
    # Try to find URL without markdown link
    url_match = re.search(url_pattern, line)
    if url_match:
        url = url_match.group(0)
        # Extract title from line or use URL
        title = line.replace(url, "").strip(" -")
        if not title:
            title = url
        return Reading(title=title, url=url)
    
    return None


def parse_section_content(content: str, section_title: str) -> Section:
    """Parse a section from the study plan markdown."""
    # This is a simplified parser - can be enhanced
    objectives: list[Objective] = []
    readings: list[Reading] = []
    practice_tasks: list[PracticeTask] = []
    assignments: list[PracticeTask] = []
    lab_steps: list[str] = []
    
    lines = content.split("\n")
    current_objective: str | None = None
    current_readings: list[Reading] = []
    
    for line in lines:
        line = line.strip()
        
        if not line:
            continue
        
        # Parse objectives
        if "**Objectives:**" in line or line.startswith("**Objectives:**"):
            if current_objective:
                objectives.append(Objective(
                    description=current_objective,
                    readings=current_readings.copy()
                ))
            current_objective = line.replace("**Objectives:**", "").strip()
            current_readings = []
        
        # Parse readings
        elif line.startswith("-") and ("http" in line or "docs.snowflake.com" in line):
            reading = parse_reading(line)
            if reading:
                readings.append(reading)
                current_readings.append(reading)
        
        # Parse practice tasks
        elif "**Practice Tasks**" in line or "### Practice Tasks" in line:
            # Will be handled in next iteration
            pass
        
        # Parse lab steps
        elif line.startswith(("1.", "2.", "3.", "4.", "5.", "6.", "7.", "8.", "9.")):
            if "Lab Steps" in content or "Lab steps" in content:
                step_text = re.sub(r'^\d+\.\s*', '', line)
                if step_text:
                    lab_steps.append(step_text)
    
    # Add last objective if exists
    if current_objective:
        objectives.append(Objective(
            description=current_objective,
            readings=current_readings.copy()
        ))
    
    # Extract time and weight from section title or content
    time_match = re.search(r'(\d+\.?\d*\s*h|\d+\s*min)', section_title)
    time = time_match.group(1) if time_match else "N/A"
    
    weight_match = re.search(r'(\d+)%', section_title)
    weight = int(weight_match.group(1)) if weight_match else None
    
    return Section(
        title=section_title,
        time=time,
        weight=weight,
        objectives=objectives,
        readings=readings,
        practice_tasks=practice_tasks,
        assignments=assignments,
        lab_steps=lab_steps
    )


def get_section_content(section_id: int) -> Section | None:
    """Get parsed content for a specific section."""
    from src.config import SECTIONS, STUDY_PLAN_PATH
    
    if section_id < 1 or section_id > len(SECTIONS):
        return None
    
    content = load_study_plan(STUDY_PLAN_PATH)
    section_info = SECTIONS[section_id - 1]
    
    # This is a simplified version - full implementation would parse the markdown properly
    return parse_section_content(content, section_info["title"])

