from pathlib import Path

import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "datasets" / "crop_disease.csv"
MODEL_PATH = BASE_DIR / "models" / "disease_model.pkl"


def train_disease_model():
    """Train Random Forest disease prediction model and save it locally."""
    df = pd.read_csv(DATA_PATH)

    features = ["crop", "symptom", "season", "soil_type"]
    target = "disease"

    x = df[features]
    y = df[target]

    preprocessor = ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(handle_unknown="ignore"), features),
        ]
    )

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42,
    )

    pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("model", model),
        ]
    )

    pipeline.fit(x, y)

    MODEL_PATH.parent.mkdir(exist_ok=True)
    joblib.dump(pipeline, MODEL_PATH)

    return pipeline


def load_model():
    """Load saved disease prediction model."""
    if not MODEL_PATH.exists():
        return train_disease_model()

    return joblib.load(MODEL_PATH)


def predict_disease(crop, symptom, season, soil_type):
    """Predict crop disease using local CPU ML model."""
    model = load_model()

    input_df = pd.DataFrame(
        [
            {
                "crop": crop,
                "symptom": symptom,
                "season": season,
                "soil_type": soil_type,
            }
        ]
    )

    prediction = model.predict(input_df)[0]

    confidence = 0.0
    if hasattr(model.named_steps["model"], "predict_proba"):
        probabilities = model.predict_proba(input_df)[0]
        confidence = round(float(max(probabilities)), 2)

    df = pd.read_csv(DATA_PATH)
    row = df[df["disease"] == prediction].iloc[0]

    return {
        "crop": crop,
        "symptom": symptom,
        "season": season,
        "soil_type": soil_type,
        "disease": prediction,
        "severity": row["severity"],
        "recommendation": row["recommendation"],
        "confidence": confidence,
    }


if __name__ == "__main__":
    train_disease_model()

    result = predict_disease(
        crop="Tomato",
        symptom="Yellow Spots",
        season="Kharif",
        soil_type="Red Soil",
    )

    print(result)
    