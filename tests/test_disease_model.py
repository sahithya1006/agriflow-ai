from ai.disease_model import predict_disease


def test_predict_disease_returns_result():
    result = predict_disease(
        crop="Tomato",
        symptom="Yellow Spots",
        season="Kharif",
        soil_type="Red Soil",
    )

    assert result["crop"] == "Tomato"
    assert "disease" in result
    assert "recommendation" in result
    assert 0 <= result["confidence"] <= 1
