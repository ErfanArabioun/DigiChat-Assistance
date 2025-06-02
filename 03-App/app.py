import streamlit as st
from transformers import AutoTokenizer, AutoModel
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd


# # For Right to left
# st.markdown(
#     """
#     <style>
#     .reportview-container {
#         direction: rtl;
#         text-align: right;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# Load tokenizer and model
@st.cache_resource
def load_model():
    model_name = "HooshvareLab/bert-fa-base-uncased"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name)
    return tokenizer, model

# Encode question
def encode_questions(questions, tokenizer, model):
    embeddings = []
    for question in questions:
        inputs = tokenizer(question, return_tensors="pt", truncation=True, padding=True, max_length=128)
        outputs = model(**inputs)
        embeddings.append(outputs.last_hidden_state.mean(dim=1).detach().numpy())
    return np.vstack(embeddings)

# Find the best answer
def find_best_answer(user_question, faq_data, faq_embeddings, tokenizer, model):
    user_embedding = encode_questions([user_question], tokenizer, model)[0]
    similarities = cosine_similarity([user_embedding], faq_embeddings)
    best_match_idx = similarities.argmax()
    return faq_data.iloc[best_match_idx]

# Load data and embeddings
@st.cache_data
def load_data():
    faq_data = pd.read_excel("FAQ_Dataset.xlsx")
    faq_embeddings = np.load("faq_embeddings.npy")
    return faq_data, faq_embeddings

# Streamlit App
def main():
    st.title("📚 DigiChat Assistance")
    st.markdown("این ابزار برای یافتن پاسخ‌های متداول طراحی شده است. لطفاً سؤال خود را وارد کنید:")

    # Load resources
    tokenizer, model = load_model()
    faq_data, faq_embeddings = load_data()

    # User input
    user_question = st.text_input("👇🏻 سؤال خود را اینجا وارد کنید:")
    
    if user_question:
        with st.spinner("Analysing..."):
            best_answer_row = find_best_answer(user_question, faq_data, faq_embeddings, tokenizer, model)
            # st.success("✅ پاسخ یافت شد!")
            st.markdown(f"**پاسخ سوال شما:** {best_answer_row['Answer']}")
            if pd.notna(best_answer_row['Related_Links']) and best_answer_row['Related_Links']:
                st.markdown(f"**لطفا برای کسب اطلاعات بیشتر به لینک مراجعه نمایید:**({best_answer_row['Related_Links']})")

if __name__ == "__main__":
    main()
