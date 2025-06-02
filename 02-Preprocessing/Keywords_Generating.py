from transformers import AutoTokenizer, AutoModel
import torch
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def load_model_and_tokenizer():
    """Load model and tokenizer"""
    model_name = 'HooshvareLab/bert-fa-base-uncased'
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name)
    return model, tokenizer

def get_bert_embeddings(text, model, tokenizer):
    """Get BERT embeddings for input text"""
    inputs = tokenizer(text, return_tensors='pt', padding=True, truncation=True, max_length=128)
    with torch.no_grad():
        outputs = model(**inputs)
    # Using average of token embeddings
    embeddings = outputs.last_hidden_state.mean(dim=1).numpy()
    return embeddings

def extract_keywords(question, model, tokenizer, stop_words):
    """Extract keywords from question"""
    try:
        # Get embedding for entire text
        text_embedding = get_bert_embeddings(question, model, tokenizer)
        
        # Text tokens
        tokens = tokenizer.tokenize(question)
        
        # Remove stop words
        filtered_tokens = [token for token in tokens if token not in stop_words]
        
        if not filtered_tokens:
            return ""
        
        # Calculate embedding for each token
        token_embeddings = []
        for token in filtered_tokens:
            token_embedding = get_bert_embeddings(token, model, tokenizer)
            token_embeddings.append(token_embedding)
        
        token_embeddings = np.array(token_embeddings).squeeze()
        
        # Calculate cosine similarity
        similarities = cosine_similarity(token_embeddings, text_embedding.reshape(1, -1)).flatten()
        
        # Select top 5 keywords
        top_indices = np.argsort(similarities)[::-1][:5]
        keywords = [filtered_tokens[i] for i in top_indices]
        
        return ", ".join(keywords)
    
    except Exception as e:
        print(f"❌ Error in keyword extraction: {str(e)}")
        return ""

def main():
    try:
        # Load data
        print("📚 Loading data...")
        df = pd.read_csv('DIGIKALA_FAQ_ALL.csv')
        
        # Load model and tokenizer
        print("🤖 Loading model...")
        model, tokenizer = load_model_and_tokenizer()
        
        # Load stop words
        print("📝 Loading stop words...")
        with open('Persian_Stop_Words.txt', 'r', encoding='utf-8') as f:
            stop_words = set(f.read().splitlines())
        
        # Extract keywords
        print("🔍 Extracting keywords...")
        df['Keywords'] = df['Question'].apply(
            lambda x: extract_keywords(x, model, tokenizer, stop_words)
        )
        
        # Save results
        print("💾 Saving results...")
        df.to_csv("DIGIKALA_FAQ_KEYWORDS.csv", index=False, encoding='utf-8-sig')
        print("✅ Operation completed successfully!")
        
    except Exception as e:
        print(f"❌ Error in program execution: {str(e)}")

if __name__ == "__main__":
    main()
