from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle
from flask import Flask, request, jsonify

# initialize flask app
application = Flask(__name__)
loaded_model = None
vectorizer = None

### model loading ###
def load_model():
    global loaded_model, vectorizer

    with open('basic_classifier.pkl', 'rb') as fid:
        loaded_model = pickle.load(fid)

    with open('count_vectorizer.pkl', 'rb') as vd:
        vectorizer = pickle.load(vd)

load_model()

### home route
@application.route('/')
def index():
    return "Fake News Detection API is running..."

### prediction route
@application.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # check if input is valid
    if not data or 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400

    # get text
    text = data['text']

    # make prediction
    prediction = loaded_model.predict(vectorizer.transform([text]))[0]

    # return 1 if FAKE, 0 if REAL
    result = 1 if prediction == 'FAKE' else 0

    return jsonify({'prediction': result, 'label': prediction})

### start application
if __name__ == '__main__':
    application.run()
