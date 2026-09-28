import joblib

from intelligent_analyzer import analyze_message


MODEL_PATH = "model/spam_classifier.pkl"


# Load the existing trained model
model = joblib.load(MODEL_PATH)


print("========================================")
print("   TASK 3 INTELLIGENT FEATURE TEST")
print("========================================")


test_messages = [
    "Congratulations! You won a free prize. Click now!",
    "Hey, are you coming home today?",
    "URGENT! Claim your cash reward immediately."
]


for message in test_messages:

    print("\n----------------------------------------")
    print("Message:")
    print(message)

    try:

        result = analyze_message(model, message)

        print("\nPrediction:", result["prediction"])
        print(
            "Confidence:",
            f"{result['confidence'] * 100:.2f}%"
        )
        print(
            "Spam Probability:",
            f"{result['spam_probability'] * 100:.2f}%"
        )
        print("Risk Level:", result["risk_level"])

        print("\nSuspicious Indicators:")

        if result["indicators"]:

            for indicator in result["indicators"]:

                print(
                    f"- {indicator['category']}: "
                    f"{', '.join(indicator['keywords'])}"
                )

        else:

            print("- None detected")

        print("\nRecommendation:")
        print(result["recommendation"])

    except Exception as e:

        print("\nError:")
        print(type(e).__name__, "-", str(e))


print("\n========================================")
print("          ERROR HANDLING TEST")
print("========================================")


try:

    analyze_message(model, "")

except Exception as e:

    print("\nEmpty message test:")
    print(type(e).__name__, "-", str(e))


try:

    analyze_message(model, "Hi")

except Exception as e:

    print("\nShort message test:")
    print(type(e).__name__, "-", str(e))


print("\n========================================")
print("             TEST COMPLETE")
print("========================================")