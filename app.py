import string
import nltk
from nltk.stem.porter import PorterStemmer
import streamlit as st
import pickle

# NLTK setup
nltk.download('punk_tab')
nltk.download('stopwords')
from nltk.corpus import stopwords

ps = PorterStemmer()

# Load trained model and vectorizer
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

# Preprocessing function
def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

# Streamlit UI
st.set_page_config(page_title="Spam Detector", page_icon="📩")

st.title("📩 SMS/Email Spam Classifier")
st.markdown("Check if your message is **Spam** or **Not Spam** using this ML-powered web app!")

st.write("---")

input_sms = st.text_area("✉️ Enter the message below:")

if st.button("🔍 Predict"):
    # Preprocess
    transformed_sms = transform_text(input_sms)

    # Vectorize
    vector_input = vectorizer.transform([transformed_sms])

    # Predict
    result = model.predict(vector_input)[0]

    # Display result
    st.write("---")
    if result == 1:
        st.error("🚨 This message is **SPAM**!")
    else:
        st.success("✅ This message is **NOT SPAM**.")