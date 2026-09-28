import joblib

MODEL_PATH = "model/spam_classifier.pkl"

try:
    model = joblib.load(MODEL_PATH)

    print("========================================")
    print("       TASK 3 MODEL INSPECTION")
    print("========================================")

    print("\nModel loaded successfully!")
    print("Model type:", type(model))

    # Pipeline information
    if hasattr(model, "steps"):
        print("\nPipeline steps:")

        for name, step in model.steps:
            print(f"- {name} => {type(step)}")

    # Check classifier
    classifier = model.named_steps["classifier"]

    print("\nClassifier:", type(classifier))

    # Check classes
    if hasattr(classifier, "classes_"):
        print("Classes:", classifier.classes_)

    # Check probability support
    print("\nProbability support:", hasattr(model, "predict_proba"))

    # Test messages
    test_messages = [
        "Congratulations! You won a free prize. Click now!",
        "Hey, are you coming home today?",
        "URGENT! Claim your cash reward immediately."
    ]

    print("\n========================================")
    print("       SAMPLE PREDICTIONS")
    print("========================================")

    for message in test_messages:

        prediction = model.predict([message])[0]

        print("\nMessage:", message)
        print("Prediction:", prediction)

        if hasattr(model, "predict_proba"):
            probabilities = model.predict_proba([message])[0]

            print("Probabilities:")

            for class_name, probability in zip(
                model.classes_,
                probabilities
            ):
                print(f"  {class_name}: {probability:.4f}")

except Exception as e:

    print("\nERROR:")
    print(type(e).__name__, "-", str(e))