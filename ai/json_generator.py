from pydantic import BaseModel, Field


class PredictionOutput(BaseModel):
    crop: str
    issue_type: str
    prediction: str
    severity: str
    confidence: float = Field(ge=0.0, le=1.0)
    recommendation: str


def generate_prediction_json(model_result, issue_type="Disease"):
    """Generate JSON from ML model output."""

    output = PredictionOutput(
        crop=model_result["crop"],
        issue_type=issue_type,
        prediction=model_result["disease"],
        severity=model_result["severity"],
        confidence=model_result["confidence"],
        recommendation=model_result["recommendation"],
    )

    try:
        return output.model_dump()
    except AttributeError:
        return output.dict()


if __name__ == "__main__":
    from disease_model import predict_disease

    model_result = predict_disease(
        crop=input("Enter crop: "),
        symptom=input("Enter symptom: "),
        season=input("Enter season: "),
        soil_type=input("Enter soil type: "),
    )

    json_output = generate_prediction_json(model_result)

    print("\nStructured JSON Output:\n")
    print(json_output)