DigiChat Assistance
 
Welcome to DigiChat Assistance, an innovative project designed to provide automated, intelligent answers to frequently asked questions (FAQs) from Digikala, Iran's leading e-commerce platform. Powered by web scraping, natural language processing (NLP), and a user-friendly Streamlit web application, this project leverages BERT-based embeddings to deliver accurate and relevant responses to customer queries in Persian.
🚀 Project Overview
DigiChat Assistance automates the process of answering customer questions by:

Crawling FAQs: Scraping Digikala's FAQ pages to collect questions, answers, and related links.
Keyword Extraction: Generating meaningful keywords from questions to enhance searchability.
Interactive Web App: Providing a Streamlit-based interface where users can input questions and receive instant answers based on semantic similarity.

This project is perfect for anyone interested in NLP, web scraping, or building user-friendly applications for customer support automation.
📂 Project Structure
The project is organized into three main components:

Crawler:

Digikala_FAQ_Crawler_FullExtraction.py: Scrapes FAQs from Digikala's website using Selenium, storing questions, answers, categories, and links in a CSV file.


Preprocessing:

Keywords_Generating.py: Extracts keywords from FAQ questions using a BERT-based model (HooshvareLab/bert-fa-base-uncased) and Persian stop words for improved search functionality.


App:

Embedding.py: Generates BERT embeddings for FAQ questions, saved as a NumPy array for efficient retrieval.
app.py: A Streamlit web application that allows users to input questions in Persian and receive the most relevant FAQ answer based on cosine similarity.



Additional files:

Persian_Stop_Words.txt: A comprehensive list of Persian stop words used for keyword extraction.
FAQ_Dataset.xlsx (generated): Stores the scraped FAQ data.
faq_embeddings.npy (generated): Stores precomputed BERT embeddings for FAQs.

🛠️ Getting Started
Prerequisites

Python 3.8 or higher
Google Chrome (for Selenium web scraping)
Dependencies listed in requirements.txt

Installation

Clone the repository:
git clone https://github.com/ErfanArabioun/DigiChat-Assistance.git
cd DigiChat-Assistance


Install dependencies:
pip install -r requirements.txt


Download and install the ChromeDriver compatible with your Chrome version for the crawler.


Usage

Collect FAQs:Run the crawler to scrape Digikala's FAQs:
python Crawler/Digikala_FAQ_Crawler_FullExtraction.py

This generates DIGIKALA_FAQ_ALL.csv.

Generate Keywords:Extract keywords from questions:
python Preprocessing/Keywords_Generating.py

This generates DIGIKALA_FAQ_KEYWORDS.csv.

Create Embeddings:Generate BERT embeddings for FAQs:
python App/Embedding.py

This generates faq_embeddings.npy.

Run the Web App:Launch the Streamlit app:
streamlit run App/app.py

Open the provided URL in your browser, enter a question in Persian, and get the most relevant answer!


📊 Example Output
User Input: "چگونه کیف پول دیجی‌کالا را فعال کنم؟"Output: The app returns the most relevant FAQ answer, such as:"برای فعال‌سازی کیف پول دیجی‌کالا، ابتدا وارد حساب کاربری خود شوید و از منوی حساب کاربری، گزینه کیف پول را انتخاب کنید..."(along with any related links, if available).
🛠️ Technologies Used

Python: Core programming language.
Selenium: For web scraping Digikala's FAQ pages.
Transformers (Hugging Face): For BERT-based NLP (HooshvareLab/bert-fa-base-uncased).
Streamlit: For building the interactive web application.
Pandas & NumPy: For data handling and processing.
Scikit-learn: For cosine similarity calculations.
Torch: For running BERT models.

📈 Future Improvements

Add support for multi-lingual FAQs.
Enhance the UI with advanced styling and visualizations.
Optimize embedding generation for faster response times.
Integrate real-time FAQ updates from Digikala's website.

🤝 Contributing
Contributions are welcome! Please fork the repository, create a new branch, and submit a pull request with your improvements. For major changes, open an issue first to discuss your ideas.
📜 License
This project is licensed under the MIT License.
🙌 Acknowledgments

Digikala for providing the FAQ data source.
HooshvareLab for the Persian BERT model.
Streamlit for the awesome web app framework.


⭐ If you find this project helpful, give it a star on GitHub!For questions or feedback, contact arabiounerfan@gmail.com or open an issue.
