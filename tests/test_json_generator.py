from pydantic import BaseModel, Field


class PredictionOutput(BaseModel):
    crop: str
    issue_type: str
    prediction: str
    severity: str
    confidence: float = Field(ge=0.0, le=1.0)
    recommendation: str


def generate_prediction_json(
    crop,
    issue_type,
    prediction,
    severity,
    confidence,
    recommendation,
):
    output = PredictionOutput(
        crop=crop,
        issue_type=issue_type,
        prediction=prediction,
        severity=severity,
        confidence=confidence,
        recommendation=recommendation,
    )

    # Compatible with both Pydantic v1 and v2
    try:
        return output.model_dump()
    except AttributeError:
        return output.dict()


if __name__ == "__main__":
    print("Testing JSON Generator...\n")

    result = generate_prediction_json(
        crop="Tomato",
        issue_type="Disease",
        prediction="Early Blight",
        severity="High",
        confidence=0.94,
        recommendation="Apply Copper Fungicide",
    )

    print(result)