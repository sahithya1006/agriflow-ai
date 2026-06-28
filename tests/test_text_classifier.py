from ai.text_classifier import classify_query


def test_classify_fertilizer_query():
    result = classify_query("Which fertilizer should I use for rice?")

    assert result["category"] == "Fertilizer"
    assert "confidence" in result
    assert result["query"] == "Which fertilizer should I use for rice?"


def test_classify_disease_query():
    result = classify_query("My tomato leaves have yellow spots")

    assert result["category"] == "Disease"


def test_classify_pest_query():
    result = classify_query("Cotton plant has white insects")

    assert result["category"] == "Pest"


def test_classify_irrigation_query():
    result = classify_query("When should I water my rice crop?")

    assert result["category"] == "Irrigation"


def test_classify_government_scheme_query():
    result = classify_query("Am I eligible for PM Kisan scheme?")

    assert result["category"] == "Government Scheme"
