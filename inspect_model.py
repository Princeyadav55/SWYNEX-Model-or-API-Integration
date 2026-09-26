import joblib

model = joblib.load("model/spam_classifier.pkl")

print("Model loaded successfully!")
print("Model type:", type(model))

if hasattr(model, "steps"):
    print("\nThis is a Pipeline.")
    print("Pipeline steps:")
    for name, step in model.steps:
        print("-", name, "=>", type(step))

else:
    print("\nThis is NOT a Pipeline.")