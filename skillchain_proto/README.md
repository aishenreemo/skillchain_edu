# SkillChain EDU Prototype

SkillChain is a demonstration project that combines modern verifiable credentials with advanced Natural Language Processing (NLP) using SkillNER to perform real-time curriculum analysis.The application serves two primary functions:
- Verification: Provides a simple API and UI for checking verifiable skill credentials.
- Gap Analysis: Compares skills extracted from arbitrary course descriptions against skills extracted from arbitrary job descriptions to identify critical skill gaps.

## Features
- Credential Verification (/skills/{id}): Securely serves JSON-based verifiable skill credentials.QR Code Generation (/qr/{id}): Generates QR codes that link directly to the verification page.
- Skill Gap Analysis (/ai/skillner_analyze): Leverages SkillNER, a specialized NLP library, to extract and compare skills from unstructured text data.
- Minimal Setup: Uses FastAPI for a lightweight, modern web backend.

## Prerequisites
To run this project locally, you need:
- Python 3.8+pip (Python package installer)
## Setup 
Follow these steps to get the SkillChain server running on your local machine.
1. Install Dependencies
Install the required Python packages, including FastAPI, Uvicorn, SkillNER, and SpaCy.
```
pip install fastapi uvicorn "uvicorn[standard]" qrcode
pip install skillner
python -m spacy download en_core_web_lg

```
(Note: en_core_web_lg is required by SkillNER and is initialized in main.py).

2. Run the Application
Start the FastAPI server using Uvicorn with auto-reload enabled:
```
python -m uvicorn main:app --reload
```
The server will run at `http://127.0.0.1:8000`.

## 📍 Key Endpoints
| Method | Endpoint | Description |
| ------ | -------- | ----------- |
| GET | / | Serves the main Student Dashboard UI (frontend/index.html). |
| GET | /verify/{id} | Serves the Verification UI for employers to check a credential. |
| GET | /skills/{id} | API endpoint that returns the verifiable credential JSON data. |
| GET | /qr/{id} | Generates a QR code image linking to the verification page. |
| GET | /dashboard/gap_analysis | AI Endpoint: Runs the SkillNER extraction and gap analysis against the data files. |
