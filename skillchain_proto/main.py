from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, HTMLResponse
from qrcode import make as make_qr
import json
import os

import spacy
import hashlib 
from spacy.matcher import PhraseMatcher

from skillNer.general_params import SKILL_DB
from skillNer.skill_extractor_class import SkillExtractor

app = FastAPI()

nlp = spacy.load("en_core_web_lg")
skill_extractor = SkillExtractor(nlp, SKILL_DB, PhraseMatcher)

CREDENTIALS_DIR = "data"

def load_json(credential_id: str):
    """Loads a mock VC from the JSON file."""
    filepath = os.path.join(CREDENTIALS_DIR, f"{credential_id}.json")
    if not os.path.exists(filepath):
        raise HTTPException(status_code=404, detail="Credential not found")
    with open(filepath, 'r') as f:
        return json.load(f)

@app.get("/skills/{credential_id}")
def get_credential_data(credential_id: str):
    """Serves the JSON payload (the verified skill data)."""
    return load_json(credential_id)

@app.get("/qr/{credential_id}")
async def generate_qr_code(credential_id: str):
    """Generates a QR code image that links to the /verify page."""
    load_json(credential_id)

    verify_url = f"http://127.0.0.1:8000/verify/{credential_id}"
    
    img = make_qr(verify_url)
    qr_filename = f"qr_{credential_id}.png"
    img.save(qr_filename)

    return FileResponse(qr_filename, media_type="image/png")

@app.get("/", response_class=HTMLResponse)
async def home():
    """Simple home page to start the demo."""
    return FileResponse("frontend/index.html")

@app.get("/verify/{credential_id}", response_class=HTMLResponse)
async def verify_page(credential_id: str):
    """Serves the Employer Verification UI (verify.html)."""
    return FileResponse("frontend/verify.html")

@app.get("/dashboard/gap_analysis", response_class=HTMLResponse)
async def gap_dashboard():
    """Serves the AI Gap Detector Dashboard UI."""
    return FileResponse("frontend/gap_dashboard.html")

@app.get("/ai/skillner_analyze")
def skillner_analyze_curriculum():
    """Uses SkillNER to extract skills from arbitrary course and job text and identify gaps."""
    
    courses_data = load_json("courses_arbitrary") 
    jobs_data = load_json("jobs_arbitrary") 

    extracted_course_skills = set()
    for course in courses_data:
        course_text = (
            course['description'] + " " + 
            " ".join(course.get('objectives', [])) + " " + 
            " ".join(course.get('weekly_topics', []))
        )
        
        annotations = skill_extractor.annotate(course_text)
        
        for skill_info in annotations["results"].get('full_matches', []):
            extracted_course_skills.add(skill_info['doc_node_value'].lower())

    job_analysis_data = []
    all_required_job_skills = set()
    
    for job in jobs_data:
        job_text = job['description']
        
        annotations = skill_extractor.annotate(job_text)
        required_skills_in_job = {
            s['doc_node_value'].lower() 
            for s in annotations["results"].get('full_matches', [])
        }
        
        all_required_job_skills.update(required_skills_in_job)
        
        job_analysis_data.append({
            "job_role": job['job_title'],
            "required_skills": required_skills_in_job
        })

    missing_skills_overall = all_required_job_skills - extracted_course_skills

    results = []
    for job_info in job_analysis_data:
        job_missing_skills = list(job_info['required_skills'].intersection(missing_skills_overall))
        
        if job_missing_skills:
            results.append({
                "job_role": job_info['job_role'],
                "CRITICAL_GAPS": job_missing_skills,
            })
            
    return {
        "status": "SkillNER Arbitrary Text Analysis Complete",
        "total_extracted_course_skills": len(extracted_course_skills),
        "gaps_found": results
    }
