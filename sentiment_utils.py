import joblib
import os
from preprocess import clean_text

# Load the trained model and vectorizer
MODEL_PATH = os.path.join("model", "model.pkl")
VECTORIZER_PATH = os.path.join("model", "vectorizer.pkl")

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

def predict_sentiments(texts):
    """
    Given a list of review texts, predict sentiment for each: Positive, Negative, or Neutral.
    """
    cleaned = [clean_text(str(t)) for t in texts]
    X = vectorizer.transform(cleaned)
    preds = model.predict(X)
    return preds
