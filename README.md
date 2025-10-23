# resume-job-matching
# AI Resume-Job Matching System | 简历-岗位智能匹配系统

![Python](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.119-green)
![Streamlit](https://img.shields.io/badge/Streamlit-1.50-red)
![License](https://img.shields.io/badge/license-MIT-green)

## 🚀 在线体验
👉 **Demo**: [(https://resume-job-matching-p6n6knucr95zasnnj4rappe.streamlit.app/)]

## 📌 功能
- 基于 **Sentence-BERT** 语义匹配，**非关键词**
- 支持 **中英文简历/岗位描述**
- **实时打分** + **可解释高亮**
- **Web 界面**上传即可用

## 🛠️ 本地一键运行
```bash
git clone https://github.com/nie-040816/resume-job-matching.git
cd resume-job-matching
pip install -r requirements.txt
python models/train.py          # 训练/加载模型
uvicorn api.app:app --reload    # 后端
streamlit run frontend/app.py   # 前端
## 📁 项目结构
resume-job-matching/
├── models/          # 训练与预测
├── api/             # FastAPI 后端
├── frontend/        # Streamlit 前端
├── model_files/     # 预训练模型
└── requirements.txt
## 📊 性能
- **AUC**: 85 %（自建测试集）
- **推理速度**: < 200 ms/条
📄 许可证
MIT © 2025 nie-040816
