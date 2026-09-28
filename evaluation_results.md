# Evaluation Results

## Evaluation Overview

The Smart SMS Risk Analyzer was tested using a set of
representative spam and non-spam SMS messages.

The evaluation checks whether the trained machine learning
model correctly classifies the selected test examples.

---

## Test Results

| Test Case | Message | Expected | Actual | Result |
|---|---|---|---|---|
| 1 | Congratulations! You have won a free prize. Click now! | spam | spam | PASS |
| 2 | URGENT! Claim your cash reward immediately. | spam | spam | PASS |
| 3 | You have won ₹50,000. Click here to claim your reward. | spam | spam | PASS |
| 4 | Exclusive offer! Get a free gift today. | spam | spam | PASS |
| 5 | Hey, are you coming home today? | ham | ham | PASS |
| 6 | Please call me when you reach home. | ham | ham | PASS |
| 7 | Your appointment is scheduled for tomorrow. | ham | ham | PASS |
| 8 | Can you send me the project file? | ham | ham | PASS |

---

## Summary

**Total Test Cases:** 8

**Correct Predictions:** 7

**Evaluation Accuracy:** 87.50%

---

## Interpretation

The model correctly classified 7 out of the 8 selected
evaluation examples.

One example was incorrectly classified. This demonstrates
that machine learning predictions are not guaranteed to be
correct for every message.

The evaluation result is based on the selected test cases
and should not be considered a complete benchmark of the
model's performance on all real-world SMS messages.

---

## What Was Evaluated

The evaluation covered:

- Spam SMS classification
- Non-spam SMS classification
- Model prediction
- Prediction confidence
- Intelligent analysis
- Error handling
- Different types of message patterns

---

## Conclusion

The evaluation demonstrates that the Task 3 prototype can
perform SMS classification and provide additional intelligent
analysis while handling invalid input gracefully.