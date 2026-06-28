from ai.json_generator import generate_prediction_json


def test_generate_prediction_json():
    model_result = {
        "crop": "Tomato",
        "disease": "Early Blight",
        "severity": "High",
        "confidence": 0.94,
        "recommendation": "Apply Copper Fungicide",
    }

    result = generate_prediction_json(model_result)

    assert result["crop"] == "Tomato"
    assert result["issue_type"] == "Disease"
    assert result["prediction"] == "Early Blight"
    assert result["confidence"] == 0.94
    