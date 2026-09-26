import joblib

# Load the trained AI pipeline from Task 1
model = joblib.load("model/spam_classifier.pkl")


def predict_message(message):
    """
    Predict whether an SMS is SPAM or NOT SPAM.
    """

    prediction = model.predict([message])[0]

    if prediction == "spam":
      result = "SPAM"
    else:
      result = "NOT SPAM"

    return result


if __name__ == "__main__":
    message = input("Enter an SMS message: ")

    result = predict_message(message)

    print("\nPrediction:", result)