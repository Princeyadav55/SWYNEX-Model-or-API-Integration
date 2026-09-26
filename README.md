# SWYNEX - Model Integration: AI SMS Spam Detector

## 📌 Project Overview

This project is developed as part of Task 2 of the SWYNEX Technologies internship.

The objective of this task is to integrate an existing trained machine learning model into a small working prototype.

For this task, the trained AI model developed during Task 1 of the internship has been reused and integrated into a new Streamlit-based prototype.

The prototype allows a user to enter an SMS message and receive an AI-generated classification:

- 🚨 SPAM
- ✅ NOT SPAM

---

## 🔗 Connection with Task 1

The machine learning model used in this Task 2 prototype was developed during Task 1.

The trained model is stored as:

`model/spam_classifier.pkl`

The saved model is a Scikit-learn Pipeline containing:

1. TfidfVectorizer
2. MultinomialNB classifier

Task 2 focuses on integrating this existing trained model into a new prototype rather than training the model again.

### Integration Flow

```text
User SMS
   ↓
Streamlit Interface
   ↓
predictor.py
   ↓
Trained Task 1 Model
   ↓
TF-IDF Vectorization
   ↓
Multinomial Naive Bayes
   ↓
SPAM / NOT SPAM