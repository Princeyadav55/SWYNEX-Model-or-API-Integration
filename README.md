# 🤖 SWYNEX Intelligent SMS Risk Analyzer

## 📌 Project Overview

This project is developed as part of the SWYNEX Technologies
Internship - Task 3: Intelligent Feature.

The project extends the SMS Spam Classification prototype
developed in the previous task.

The application uses a trained Machine Learning model to
classify SMS messages as:

- Spam
- Ham (Not Spam)

In addition to classification, the Task 3 version provides
an intelligent analysis layer that identifies suspicious
message indicators, estimates risk level, displays model
confidence, and provides a safety recommendation.

---

## 🎯 Task Objective

The objective of Task 3 is to enhance an existing Machine
Learning prototype by adding an intelligent feature along
with error handling, evaluation examples, and failure-case
documentation.

---

## ✨ Features

### 1. SMS Classification

The application classifies an SMS message as:

- SPAM
- NOT SPAM

The classification is performed using the trained
Machine Learning pipeline from the previous task.

### 2. Model Confidence

The application displays the probability produced by the
trained classifier.

This helps the user understand how strongly the model
supports its prediction.

### 3. Intelligent Risk Analysis

The application performs additional analysis of the SMS
content.

It checks for indicators such as:

- Prize or reward language
- Urgency
- Financial requests
- Suspicious links
- Promotional language

### 4. Risk Level

The application assigns a simple risk level:

- HIGH
- MEDIUM
- LOW

The risk level is based on the model's spam probability.

### 5. Safety Recommendation

The application provides a recommendation based on the
classification result.

For example, suspicious messages may receive a warning
to avoid clicking links or sharing personal information.

### 6. Input Validation

The application handles invalid input such as:

- Empty messages
- Very short messages

### 7. Error Handling

Unexpected errors during analysis are handled gracefully
so that the application does not terminate unexpectedly.

### 8. Evaluation

The project includes an evaluation script with multiple
spam and non-spam examples.

### 9. Failure Case Documentation

The project documents model limitations and examples where
the classifier produces an incorrect prediction.

---

## 🧠 Machine Learning Model

The project reuses the trained Machine Learning pipeline
developed in the previous internship task.

The pipeline contains:

```text
SMS Text
   ↓
TF-IDF Vectorizer
   ↓
Multinomial Naive Bayes
   ↓
Spam / Ham Prediction