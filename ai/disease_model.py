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


def clean_text(value):
    return str(value).strip().title()


def train_disease_model():
    df = pd.read_csv(DATA_PATH)

    features = ["crop", "symptom", "season", "soil_type"]
    target = "disease"

    x = df[features]
    y = df[target]

    preprocessor = ColumnTransformer(
        [("cat", OneHotEncoder(handle_unknown="ignore"), features)]
    )

    model = RandomForestClassifier(n_estimators=100, random_state=42)

    pipeline = Pipeline(
        [
            ("preprocessor", preprocessor),
            ("model", model),
        ]
    )

    pipeline.fit(x, y)

    MODEL_PATH.parent.mkdir(exist_ok=True)
    joblib.dump(pipeline, MODEL_PATH)

    return pipeline


def load_model():
    if not MODEL_PATH.exists():
        return train_disease_model()

    return joblib.load(MODEL_PATH)


def predict_disease(crop, symptom, season, soil_type):
    model = load_model()

    crop = clean_text(crop)
    symptom = clean_text(symptom)
    season = clean_text(season)
    soil_type = clean_text(soil_type)

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

    disease = model.predict(input_df)[0]
    probabilities = model.predict_proba(input_df)[0]
    confidence = round(float(max(probabilities)), 2)

    df = pd.read_csv(DATA_PATH)

    matching_rows = df[
        (df["disease"].str.title() == str(disease).title())
        & (df["crop"].str.title() == crop)
    ]

    if not matching_rows.empty:
        severity = matching_rows.iloc[0]["severity"]
        recommendation = matching_rows.iloc[0]["recommendation"]
    else:
        severity = "Medium"
        recommendation = "Consult local agriculture officer"

    return {
        "crop": crop,
        "symptom": symptom,
        "season": season,
        "soil_type": soil_type,
        "disease": disease,
        "severity": severity,
        "confidence": confidence,
        "recommendation": recommendation,
    }


if __name__ == "__main__":
    result = predict_disease(
        crop="Potato",
        symptom="Dark Spots",
        season="Rabi",
        soil_type="Loamy Soil",
    )

    print(result)
