from sentence_transformers import SentenceTransformer, InputExample, losses
from torch.utils.data import DataLoader
import json
import os

# 读数据
with open(os.path.join(os.path.dirname(__file__), '..', 'data', 'sample_data.json'), encoding='utf-8') as f:
    data = json.load(f)

train_examples = [
    InputExample(texts=[d['resume'], d['job_description']], label=float(d['label']))
    for d in data
]

# 模型
model = SentenceTransformer('./model_files/all-MiniLM-L6-v2')
train_dataloader = DataLoader(train_examples, shuffle=True, batch_size=2)
train_loss = losses.CosineSimilarityLoss(model)

# 训练
model.fit(train_objectives=[(train_dataloader, train_loss)], epochs=3, warmup_steps=10)

# 保存
save_path = os.path.join(os.path.dirname(__file__), 'match_model')
model.save(save_path)
print("Model saved to models/match_model")