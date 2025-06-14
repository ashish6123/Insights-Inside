# 🧠 Insights Inside – Product Review Sentiment Analysis Tool

🚀 **[Live Demo App](https://ashish6123-insights-inside-app-ewjx08.streamlit.app/)**

**Insights Inside** is a modern, end-to-end web application designed to analyze and visualize sentiments in product reviews. Built with Streamlit and powered by machine learning, this tool helps you uncover actionable insights from customer feedback at scale from any 
e-commerce platform.

---

## 🚀 Features

- **User-Friendly Interface**  
  Sleek, dark-themed UI with the “Insights Inside” title prominently centered for a professional, clear experience.

- **Flexible Input Options**  
  Analyze a single review or upload bulk review files (`.csv`, `.xlsx`, `.txt`)—ideal for individuals or teams.

- **Automated Text Preprocessing**  
  Uploaded reviews are automatically cleaned and normalized (stopword removal, text normalization) for optimal ML results.

- **Accurate Sentiment Prediction**  
  Uses a pre-trained TF-IDF vectorizer and Logistic Regression model to classify reviews as Positive, Negative, or Neutral.

- **Rich Visual Insights**  
  Interactive visualizations: sentiment distribution pie charts, word clouds for each sentiment, and highlights of top reviews.

- **Easy Output Export**  
  Download sentiment-tagged reviews for offline use and further analysis.

- **Deployment Ready**  
  Easily deployable on Streamlit Cloud with minimal setup.

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit (Python)
- **NLP & ML:** scikit-learn (Logistic Regression, TF-IDF), pandas, numpy
- **Visualization:** matplotlib, wordcloud
- **Utilities:** Modular scripts for preprocessing (`preprocess.py`), sentiment prediction (`sentiment_utils.py`), and EDA/model-building notebooks.

---

## 📁 Project Structure

```
Insights_Inside/
├── app.py
├── sentiment_utils.py
├── preprocess.py
├── model/
│   ├── model.pkl
│   └── vectorizer.pkl
├── dataset/
│   └── sample_input.csv
├── outputs/
├── requirements.txt
├── notebooks/
│   └── model_building.ipynb
├── README.md
└── report.pdf (optional)
```

---

## ⚡ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/Insights_Inside.git
cd Insights_Inside
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Launch the App

```bash
streamlit run app.py
```

### 4. Usage

- **Single Review**: Enter a review directly in the input box.
- **Bulk Reviews**: Upload a `.csv`, `.xlsx`, or `.txt` file containing reviews.
- View interactive charts and download sentiment-tagged results.

---

## 📈 Example Input & Output

- **Sample Input File:** `dataset/sample_input.csv`
- **Output:** Downloadable file with sentiment predictions; interactive charts and word clouds in-app.

---

## 🌐 Deployment

Try it live: 👉 [Insights Inside on Streamlit Cloud](https://ashish6123-insights-inside-app-ewjx08.streamlit.app/)
Deploy easily on [Streamlit Cloud](https://streamlit.io/cloud).  
See the official [Streamlit deployment docs](https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app) for instructions.

---

## 🎯 Purpose & Impact

Insights Inside empowers product managers, data analysts, and e-commerce businesses to transform raw customer feedback into actionable insights. By automating sentiment analysis and visualization, it enables data-driven decision-making to improve products and services.

---

## 👨‍💻 Developed & Maintained by

**Ashish Ranjan**

---

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---
