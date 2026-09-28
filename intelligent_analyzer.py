"""
Intelligent SMS Analyzer
SWYNEX Internship - Task 3

This module adds an intelligent analysis layer on top of
the existing SMS spam classification model.
"""


# Suspicious patterns commonly associated with spam messages.
SPAM_INDICATORS = {
    "prize/reward": [
        "won",
        "winner",
        "prize",
        "reward",
        "cash",
        "lottery",
        "free"
    ],

    "urgency": [
        "urgent",
        "immediately",
        "act now",
        "hurry",
        "limited time",
        "claim now"
    ],

    "financial request": [
        "bank",
        "account",
        "payment",
        "money",
        "transfer",
        "credit card",
        "debit card"
    ],

    "suspicious link": [
        "click here",
        "click now",
        "http://",
        "https://",
        "www.",
        "link"
    ],

    "offer/promotion": [
        "offer",
        "discount",
        "promotion",
        "exclusive deal"
    ]
}


def analyze_message(model, message):
    """
    Analyze an SMS using the trained ML model and
    additional intelligent rule-based indicators.

    Returns a dictionary containing:
        prediction
        confidence
        risk_level
        indicators
        recommendation
    """

    # -----------------------------
    # Input validation
    # -----------------------------

    if message is None:
        raise ValueError("Message cannot be empty.")

    message = str(message).strip()

    if not message:
        raise ValueError("Please enter an SMS message.")

    if len(message) < 3:
        raise ValueError(
            "Please enter a meaningful SMS message."
        )

    # -----------------------------
    # Model prediction
    # -----------------------------

    prediction = model.predict([message])[0]

    probabilities = model.predict_proba([message])[0]

    classes = model.classes_

    probability_map = dict(
        zip(classes, probabilities)
    )

    confidence = float(max(probabilities))

    # -----------------------------
    # Intelligent indicator analysis
    # -----------------------------

    message_lower = message.lower()

    detected_indicators = []

    for category, keywords in SPAM_INDICATORS.items():

        matched_keywords = []

        for keyword in keywords:

            if keyword in message_lower:
                matched_keywords.append(keyword)

        if matched_keywords:

            detected_indicators.append({
                "category": category,
                "keywords": matched_keywords
            })

    # -----------------------------
    # Risk assessment
    # -----------------------------

    spam_probability = probability_map.get(
        "spam",
        0.0
    )

    if prediction == "spam":

        if spam_probability >= 0.85:
            risk_level = "HIGH"

        elif spam_probability >= 0.60:
            risk_level = "MEDIUM"

        else:
            risk_level = "LOW"

    else:

        if spam_probability >= 0.40:
            risk_level = "MEDIUM"

        else:
            risk_level = "LOW"

    # -----------------------------
    # Recommendation
    # -----------------------------

    if prediction == "spam":

        recommendation = (
            "Avoid clicking links or sharing personal "
            "information. Verify the sender before taking action."
        )

    else:

        recommendation = (
            "The message was classified as non-spam. "
            "Still verify unexpected requests or links."
        )

    # -----------------------------
    # Final result
    # -----------------------------

    return {
        "prediction": prediction,
        "confidence": confidence,
        "spam_probability": spam_probability,
        "risk_level": risk_level,
        "indicators": detected_indicators,
        "recommendation": recommendation
    }