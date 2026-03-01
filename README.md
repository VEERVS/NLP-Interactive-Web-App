# 🧠 NLP Interactive Web App

An interactive NLP web application built with Streamlit, supporting tokenization, TF-IDF, word embeddings, POS tagging, and Named Entity Recognition.

---

## 🎓 Learning Context

This project was developed during an NLP Bootcamp organized by the IT Department at KIET.

The core NLP concepts and implementations were demonstrated during the bootcamp sessions.  
I implemented, structured, and deployed these concepts into an interactive Streamlit web application to reinforce my understanding.

This repository represents my hands-on practice and experimentation with foundational NLP techniques.

---

## 🎥 Demo

![Demo](./assets/demo.gif)

---

## 🚀 Features

- 🔹 Tokenization (NLTK / spaCy)
- 🔹 Stopword Removal
- 🔹 Word Frequency Analysis
- 🔹 Word Cloud Generation
- 🔹 TF-IDF Vectorization
- 🔹 Named Entity Recognition (spaCy / NLTK)
- 🔹 Part-of-Speech Tagging

---

## 🛠 Tech Stack

- Python  
- Streamlit  
- NLTK  
- spaCy  
- Scikit-learn  
- Pandas  
- Matplotlib  
- WordCloud

---

## 📁 Project Structure

```
nlp-web-app/
│
├── app.py                # Streamlit main app
├── requirements.txt      # Dependencies
├── assets/
│   └── demo.gif          # Demo recording
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/VEERVS/NLP-Interactive-Web-App.git
cd NLP-Interactive-Web-App
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Download spaCy model:

```bash
python -m spacy download en_core_web_sm
```

Run the app:

```bash
streamlit run app.py
```

---

## 📌 Future Improvements

- Add Transformer-based models (BERT)
- Add text summarization
- Add chatbot functionality
- Improve UI/UX
- Deploy with Docker

---

## ⭐ Support

If you find this project useful, consider giving it a star ⭐
