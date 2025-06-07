from flask import Flask, request, jsonify, render_template
import pickle
from transform import transform_text

app = Flask(__name__)

# Load model and vectorizer
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    sms = request.json['message']
    transformed = transform_text(sms)
    vectorized = vectorizer.transform([transformed])
    prediction = model.predict(vectorized)[0]
    return jsonify({'result': 'Spam' if prediction == 1 else 'Not Spam'})

if __name__ == '__main__':
    app.run(debug=True)