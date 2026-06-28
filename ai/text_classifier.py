from pathlib import Path

import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline


BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "text_classifier.pkl"


TRAINING_DATA = [
    ("My tomato leaves have yellow spots", "Disease"),
    ("Rice leaves have brown patches", "Disease"),
    ("Cotton plant has white insects", "Pest"),
    ("Small insects are eating my crop", "Pest"),
    ("Which fertilizer should I use for tomato", "Fertilizer"),
    ("My crop growth is slow which fertilizer is needed", "Fertilizer"),
    ("When should I water my rice crop", "Irrigation"),
    ("How much water is needed for cotton", "Irrigation"),
    ("Am I eligible for PM Kisan scheme", "Government Scheme"),
    ("Tell me about crop insurance subsidy", "Government Scheme"),
]


def train_text_classifier():
    """Train TF-IDF + Logistic Regression classifier and save it locally."""
    texts = [item[0] for item in TRAINING_DATA]
    labels = [item[1] for item in TRAINING_DATA]

    model = Pipeline(
        steps=[
            ("tfidf", TfidfVectorizer()),
            ("classifier", LogisticRegression(max_iter=1000)),
        ]
    )

    model.fit(texts, labels)

    MODEL_PATH.parent.mkdir(exist_ok=True)
    joblib.dump(model, MODEL_PATH)

    return model


def load_model():
    """Load saved classifier. Train if model does not exist."""
    if not MODEL_PATH.exists():
        return train_text_classifier()

    return joblib.load(MODEL_PATH)


def classify_query(text):
    """Classify farmer question into category."""
    model = load_model()

    prediction = model.predict([text])[0]

    confidence = 0.0
    if hasattr(model.named_steps["classifier"], "predict_proba"):
        probabilities = model.predict_proba([text])[0]
        confidence = round(float(max(probabilities)), 2)

    return {
        "query": text,
        "category": prediction,
        "confidence": confidence,
    }


if __name__ == "__main__":
    train_text_classifier()

    result = classify_query("Which fertilizer should I use for rice?")
    print(result)
