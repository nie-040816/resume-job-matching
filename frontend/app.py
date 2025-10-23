import streamlit as st
import requests

st.title("AI Resume-Job Matching System")
resume = st.text_area("输入简历内容")
job  = st.text_area("输入岗位描述")

if st.button("匹配"):
    res = requests.post("http://localhost:8000/match", json={"resume": resume, "job_description": job})
    st.write("匹配分数：", res.json()["match_score"])