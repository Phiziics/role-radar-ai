# RoleRadar AI

RoleRadar AI is a RAG-powered job intelligence platform for data science job seekers.

The project scrapes job postings, extracts required skills, compares jobs against a resume, ranks role fit, and prepares the foundation for retrieval-augmented generation using Hugging Face embeddings and ChromaDB.

## Current Features

1. Greenhouse job scraper
2. Job posting storage as CSV
3. Resume-to-job skill matching
4. Skill gap detection
5. Modular Python project structure

## Planned Features

1. Hugging Face sentence-transformer embeddings
2. ChromaDB vector search
3. Streamlit dashboard
4. FastAPI backend
5. Resume bullet generation
6. Job market skill analytics

## Tech Stack

Python, pandas, requests, BeautifulSoup, scikit-learn, Hugging Face, ChromaDB, Streamlit, FastAPI

## Project Flow

Internet job boards → scraped jobs CSV → skill extraction → resume matching → RAG retrieval → dashboard

## How to Run

Create a virtual environment:

```bash
python -m venv .venv