DigiChat Assistance

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.38.0-red.svg)
![Selenium](https://img.shields.io/badge/Selenium-4.25.0-green.svg)
![Transformers](https://img.shields.io/badge/Transformers-4.44.2-orange.svg)
![PyTorch](https://img.shields.io/badge/PyTorch-2.4.1-blue.svg)

 
Welcome to DigiChat Assistance, an intelligent tool designed to automate answering frequently asked questions (FAQs) from Digikala, Iran's leading e-commerce platform. Powered by web scraping, Persian NLP, and a sleek Streamlit web interface, this project uses BERT-based embeddings to provide accurate and instant responses to customer queries in Persian.
Table of Contents

Features
Project Structure
Prerequisites
Installation
Usage
Technologies Used
Future Improvements
Contributing
Contact
License

Features

Web Scraping: Automatically collects FAQs, answers, and related links from Digikala's website.
Keyword Extraction: Enhances searchability by extracting key terms from questions using a Persian BERT model.
Semantic Search: Uses cosine similarity and BERT embeddings to find the most relevant answer to user queries.
User-Friendly Interface: A Streamlit web app for seamless interaction, allowing users to input questions and receive instant answers.
Persian Language Support: Tailored for Persian text processing with a custom stop words list and a Persian BERT model.

Project Structure
The project is organized into three main components:
DigiChat-Assistance/
├── Crawler/
│   └── Digikala_FAQ_Crawler_FullExtraction.py  # Scrapes FAQs from Digikala
├── Preprocessing/
│   └── Keywords_Generating.py                  # Extracts keywords from questions
├── App/
│   ├── app.py                                 # Streamlit web application
│   └── Embedding.py                           # Generates BERT embeddings
├── Persian_Stop_Words.txt                     # Persian stop words for preprocessing
├── FAQ_Dataset.xlsx                           # Generated FAQ data
├── faq_embeddings.npy                         # Generated BERT embeddings
└── requirements.txt                           # Project dependencies

Prerequisites

Python 3.8+
Google Chrome (for Selenium web scraping)
ChromeDriver compatible with your Chrome version
Internet connection for scraping and model downloads

Installation

Clone the repository:
git clone https://github.com/ErfanArabioun/DigiChat-Assistance.git
cd DigiChat-Assistance


Install dependencies:
pip install -r requirements.txt


Install ChromeDriver:

Download the appropriate ChromeDriver version for your Chrome browser.
Place it in your system PATH or specify its location in Digikala_FAQ_Crawler_FullExtraction.py.



Usage

Collect FAQs:Scrape Digikala's FAQs:
python Crawler/Digikala_FAQ_Crawler_FullExtraction.py

Output: DIGIKALA_FAQ_ALL.csv

Generate Keywords:Extract keywords from questions:
python Preprocessing/Keywords_Generating.py

Output: DIGIKALA_FAQ_KEYWORDS.csv

Create Embeddings:Generate BERT embeddings for FAQs:
python App/Embedding.py

Output: faq_embeddings.npy

Run the Web App:Launch the Streamlit app:
streamlit run App/app.py

Open the provided URL (e.g., http://localhost:8501) in your browser, enter a Persian question, and get the most relevant answer.


Technologies Used

Python 3.8+: Core programming language.
Selenium: For scraping Digikala's FAQ pages.
Transformers (Hugging Face): Persian BERT model (HooshvareLab/bert-fa-base-uncased) for NLP tasks.
PyTorch: Backend for running BERT models.
Streamlit: For building the interactive web application.
Pandas & NumPy: For data manipulation and storage.
Scikit-learn: For cosine similarity calculations.

Future Improvements

Support for multi-lingual FAQ processing.
Enhanced UI with advanced styling and visualizations.
Real-time FAQ updates from Digikala's website.
Optimization of embedding generation for faster response times.

Contributing
We welcome contributions! To contribute:

Fork the repository.
Create a new branch (git checkout -b feature/your-feature).
Make your changes and commit (git commit -m "Add your feature").
Push to the branch (git push origin feature/your-feature).
Open a Pull Request.

For major changes, please open an issue first to discuss your ideas.
Contact
For questions or feedback, reach out via:

Email: arabiounerfan@gmail.com
GitHub Issues: Create an issue in this repository.

License
This project is licensed under the MIT License.

⭐ Star this project on GitHub if you find it useful!
