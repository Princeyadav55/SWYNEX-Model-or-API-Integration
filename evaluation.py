import joblib

from intelligent_analyzer import analyze_message


# -----------------------------------------
# Load trained model
# -----------------------------------------

MODEL_PATH = "model/spam_classifier.pkl"

model = joblib.load(MODEL_PATH)


# -----------------------------------------
# Evaluation test cases
# -----------------------------------------

test_cases = [

    {
        "message": "Congratulations! You have won a free prize. Click now!",
        "expected": "spam"
    },

    {
        "message": "URGENT! Claim your cash reward immediately.",
        "expected": "spam"
    },

    {
        "message": "You have won ₹50,000. Click here to claim your reward.",
        "expected": "spam"
    },

    {
        "message": "Exclusive offer! Get a free gift today.",
        "expected": "spam"
    },

    {
        "message": "Hey, are you coming home today?",
        "expected": "ham"
    },

    {
        "message": "Please call me when you reach home.",
        "expected": "ham"
    },

    {
        "message": "Your appointment is scheduled for tomorrow.",
        "expected": "ham"
    },

    {
        "message": "Can you send me the project file?",
        "expected": "ham"
    }
]


# -----------------------------------------
# Run evaluation
# -----------------------------------------

print("========================================")
print("       TASK 3 MODEL EVALUATION")
print("========================================")


correct = 0
total = len(test_cases)


for index, test_case in enumerate(
    test_cases,
    start=1
):

    message = test_case["message"]

    expected = test_case["expected"]


    try:

        result = analyze_message(
            model,
            message
        )

        actual = result["prediction"]

        confidence = result["confidence"]


        if actual == expected:

            status = "PASS"
            correct += 1

        else:

            status = "FAIL"


        print("\n----------------------------------------")

        print(f"Test Case: {index}")

        print("Message:", message)

        print("Expected:", expected)

        print("Actual:", actual)

        print(
            "Confidence:",
            f"{confidence * 100:.2f}%"
        )

        print("Status:", status)


    except Exception as e:

        print("\n----------------------------------------")

        print(f"Test Case: {index}")

        print("Message:", message)

        print("Status: ERROR")

        print(
            "Error:",
            type(e).__name__,
            "-",
            str(e)
        )


# -----------------------------------------
# Final evaluation result
# -----------------------------------------

accuracy = (correct / total) * 100


print("\n========================================")
print("          EVALUATION SUMMARY")
print("========================================")

print("Total Test Cases:", total)

print("Correct Predictions:", correct)

print(
    "Evaluation Accuracy:",
    f"{accuracy:.2f}%"
)

print("========================================")