from sentence_transformers import SentenceTransformer
import numpy as np
import os

model_path = os.path.join(os.path.dirname(__file__), 'match_model')
model = SentenceTransformer(model_path)

def predict_match(resume: str, job_desc: str) -> float:
    emb1 = model.encode(resume)
    emb2 = model.encode(job_desc)
    sim = np.dot(emb1, emb2) / (np.linalg.norm(emb1) * np.linalg.norm(emb2))
    return float(sim)