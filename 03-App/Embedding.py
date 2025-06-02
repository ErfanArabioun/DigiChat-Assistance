import numpy as np
import pandas as pd
from transformers import AutoTokenizer, AutoModel
from sklearn.metrics.pairwise import cosine_similarity


faq_data = pd.read_excel("FAQ_Dataset.xlsx")
questions = faq_data['Question'].tolist()

model_name = "HooshvareLab/bert-fa-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

def encode_questions(questions):
    embeddings = []
    for question in questions:
        inputs = tokenizer(question, return_tensors="pt", truncation=True, padding=True, max_length=128)
        outputs = model(**inputs)
        embeddings.append(outputs.last_hidden_state.mean(dim=1).detach().numpy())
    return np.vstack(embeddings)

faq_embeddings = encode_questions(questions)
np.save("faq_embeddings.npy", faq_embeddings)  

def find_best_answer(user_question, questions, embeddings):
    user_embedding = encode_questions([user_question])[0]
    similarities = cosine_similarity([user_embedding], embeddings)
    best_match_idx = similarities.argmax()
    return questions[best_match_idx]

# user_question =  "کیف پول چگونه فعال می شود"
# best_answer = find_best_answer(user_question, faq_data['Answer'].tolist(), faq_embeddings)
# print("Best Answer:", best_answer)