# DigiChat Assistance

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.38.0-red.svg)
![Selenium](https://img.shields.io/badge/Selenium-4.25.0-green.svg)
![Transformers](https://img.shields.io/badge/Transformers-4.44.2-orange.svg)
![PyTorch](https://img.shields.io/badge/PyTorch-2.4.1-blue.svg)

> **DigiChat Assistance** is an intelligent Persian-language FAQ assistant for [Digikala](https://www.digikala.com/), Iran’s largest e-commerce platform. It automates question answering using BERT-based semantic search, a user-friendly Streamlit interface, and web scraping techniques.

---

## 🧠 Features

* **Web Scraping**: Automatically gathers FAQs, answers, and links from Digikala.
* **Keyword Extraction**: Extracts keywords using Persian BERT for enhanced semantic understanding.
* **Semantic Search**: Uses BERT embeddings and cosine similarity to deliver the most relevant answers.
* **Persian NLP**: Tailored for Persian with custom preprocessing and stop words.
* **Streamlit Interface**: Lightweight and intuitive interface for real-time Q\&A.

---

## 📁 Project Structure

```
DigiChat-Assistance/
├── App/
│   ├── app.py                      # Streamlit web app
│   └── Embedding.py                # BERT embedding generator
├── Crawler/
│   └── Digikala_FAQ_Crawler_FullExtraction.py
├── Preprocessing/
│   └── Keywords_Generating.py      # Extracts keywords from FAQs
├── Persian_Stop_Words.txt          # Persian stopwords for preprocessing
├── FAQ_Dataset.xlsx                # Collected FAQs
├── faq_embeddings.npy              # BERT-based semantic vectors
├── requirements.txt                # Dependencies
```

---

## ✅ Prerequisites

* Python >= 3.8
* Google Chrome + matching [ChromeDriver](https://sites.google.com/chromium.org/driver/)
* Internet connection (for scraping and model downloads)

---

## ⚙️ Installation

```bash
git clone https://github.com/ErfanArabioun/DigiChat-Assistance.git
cd DigiChat-Assistance
pip install -r requirements.txt
```

> ⚠️ Make sure ChromeDriver is installed and available in your system's PATH or update the path in `Digikala_FAQ_Crawler_FullExtraction.py`.

---

## 🚀 Usage

1. **Scrape FAQs**:

   ```bash
   python Crawler/Digikala_FAQ_Crawler_FullExtraction.py
   ```

2. **Generate Keywords**:

   ```bash
   python Preprocessing/Keywords_Generating.py
   ```

3. **Create Embeddings**:

   ```bash
   python App/Embedding.py
   ```

4. **Run the App**:

   ```bash
   streamlit run App/app.py
   ```

   Open the provided URL (e.g., `http://localhost:8501`) and ask your question in Persian!

---

## 🛠️ Technologies Used

* **Python 3.8+** – Base programming language
* **Selenium** – Web scraping automation
* **Transformers (Hugging Face)** – Persian BERT: `HooshvareLab/bert-fa-base-uncased`
* **PyTorch** – Deep learning framework
* **Streamlit** – Web UI
* **Pandas & NumPy** – Data manipulation
* **Scikit-learn** – Cosine similarity for semantic search

---

## 🌱 Future Roadmap

* 🌤 Multilingual support
* 🎨 Improved UI/UX with styling and animations
* 🔄 Live scraping with periodic FAQ updates
* ⚡ Faster embedding generation via optimization

---

## 🤝 Contributing

Contributions are welcome! Here's how to contribute:

```bash
# Fork and clone the repo
git checkout -b feature/your-feature-name
# Make your changes and commit
git commit -m "Add your feature"
git push origin feature/your-feature-name
# Open a Pull Request
```

> For large features, please open an issue first to discuss your proposal.

---

## 📬 Contact

* 📧 Email: [arabiounerfan@gmail.com](mailto:arabiounerfan@gmail.com)
* 🐛 Issues: [Submit here](https://github.com/ErfanArabioun/DigiChat-Assistance/issues)

---

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

⭐️ *If you find this project useful, give it a star to support the work!*
