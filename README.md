# 🎓 Student Loan AI System

## Problem
Students take loans without knowing interest rates. Loan officers use emails and spreadsheets with no KYC validation.

## Solution
AI-powered student loan system with:
- Face recognition KYC
- Parent surety verification
- Document OCR
- Loan workflow tracking

## Tech Stack
- Streamlit
- FastAPI
- DeepFace
- OpenCV
- OCR
- SQLite

## How to Run
```bash
pip install -r requirements.txt
uvicorn backend.main:app --reload
streamlit run frontend/app.py
