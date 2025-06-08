from flask import Flask, request, jsonify, render_template
import pickle
from transform import transform_text

app = Flask(__name__)

# Load model and vectorizer
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

# Root route to serve frontend
@app.route('/')
def index():
    return render_template('index.html')

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        message = data.get("email", "")

        if not message:
            return jsonify({"error": "No input provided"}), 400

        vectorized = vectorizer.transform([message])
        prediction = model.predict(vectorized)[0]

        # Convert NumPy type to native Python
        prediction = int(prediction)
        result = "Spam" if prediction == 1 else "Not Spam"

        return jsonify({"prediction": result})

    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
