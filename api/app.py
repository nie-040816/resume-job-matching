from fastapi import FastAPI
from pydantic import BaseModel
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from models.predict import predict_match

app = FastAPI()

class Request(BaseModel):
    resume: str
    job_description: str

@app.post("/match")
def match(req: Request):
    score = predict_match(req.resume, req.job_description)
    return {"match_score": round(score, 3)}