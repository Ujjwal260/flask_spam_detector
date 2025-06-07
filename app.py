from flask import Flask, request, jsonify, render_template
import pickle
from transform import transform_text
import traceback

app = Flask(__name__)

# Load model and vectorizer
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        email_text = data.get('email', '')

        # Vectorize and predict
        transformed = vectorizer.transform([email_text])
        prediction = model.predict(transformed)[0]

        return jsonify({'prediction': prediction})
    except Exception as e:
        # Log the error for debugging
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
