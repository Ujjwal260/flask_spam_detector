# 📧 SMS/Email Spam Detection using Machine Learning

## 📌 Objective
This project aims to build and deploy a Machine Learning model that can classify text messages (SMS or Email) as **spam** or **ham (not spam)** using natural language processing and classification algorithms.

## 🧰 Tools & Technologies Used
- Python
- pandas, numpy
- scikit-learn
- Flask (for web deployment)
- HTML/CSS (for UI)
- pickle (for model persistence)

## 🔍 Key Steps & Workflow

### 1. Data Preprocessing
- Converted all text to lowercase
- Tokenization
- Removed stopwords, punctuation, and special characters
- Applied stemming for normalization

### 2. Feature Engineering
- Used **Bag of Words (CountVectorizer)** and **TF-IDF Vectorization**
- Evaluated different configurations for `max_features`

### 3. Model Training & Evaluation
- Trained classification models to identify spam messages
- Evaluated models using accuracy, precision, recall, and confusion matrix

### 4. Web Deployment
- Built a **Flask-based web app** with:
  - `app.py` as backend logic
  - HTML templates in `/templates`
  - CSS styling in `/static`
- Deployed using **Gunicorn** via `Procfile` for cloud hosting (e.g., Render or Heroku)
- Serialized model and vectorizer using `pickle` (`model.pkl`, `vectorizer.pkl`)

## 📁 Project Structure
<img width="620" height="288" alt="image" src="https://github.com/user-attachments/assets/074e2612-d9c4-48b9-ac9d-d4ec91919a4e" />


## 🚀 How to Run
1. Clone this repo  
2. Install requirements: `pip install -r requirements.txt`  
3. Run: `python app.py`  
4. Access the web app at `localhost:5000`

## 💡 Outcome
- Successfully deployed a spam detection model with a user-friendly web interface
- Accurate detection of spam vs ham using lightweight NLP techniques
