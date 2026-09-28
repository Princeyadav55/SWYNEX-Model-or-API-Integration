import streamlit as st

import joblib

from intelligent_analyzer import analyze_message


# -----------------------------------------
# Load trained model
# -----------------------------------------

MODEL_PATH = "model/spam_classifier.pkl"

model = joblib.load(MODEL_PATH)


# -----------------------------------------
# Page configuration
# -----------------------------------------

st.set_page_config(
    page_title="Smart SMS Risk Analyzer",
    page_icon="🤖",
    layout="centered"
)


# -----------------------------------------
# Title
# -----------------------------------------

st.title("🤖 Smart SMS Risk Analyzer")

st.write(
    "Enter an SMS message below. The AI model will "
    "classify the message and provide an intelligent "
    "risk analysis."
)


st.divider()


# -----------------------------------------
# Input
# -----------------------------------------

message = st.text_area(
    "Enter your SMS message:",
    placeholder=(
        "Example: Congratulations! You have won "
        "a free prize. Click now..."
    ),
    height=150
)


# -----------------------------------------
# Analyze button
# -----------------------------------------

if st.button("🔍 Analyze SMS"):

    try:

        # Analyze the message
        result = analyze_message(
            model,
            message
        )


        st.divider()

        # ---------------------------------
        # Prediction
        # ---------------------------------

        st.subheader("📊 Prediction")


        if result["prediction"] == "spam":

            st.error("🚨 SPAM MESSAGE")

        else:

            st.success("✅ NOT SPAM")


        # ---------------------------------
        # Confidence
        # ---------------------------------

        st.subheader("🎯 Model Confidence")

        st.progress(result["confidence"])

        st.write(
            f"{result['confidence'] * 100:.2f}%"
        )


        # ---------------------------------
        # Spam probability
        # ---------------------------------

        st.subheader("📈 Spam Probability")

        st.write(
            f"{result['spam_probability'] * 100:.2f}%"
        )


        # ---------------------------------
        # Risk level
        # ---------------------------------

        st.subheader("⚠️ Risk Level")

        if result["risk_level"] == "HIGH":

            st.error("🔴 HIGH RISK")

        elif result["risk_level"] == "MEDIUM":

            st.warning("🟠 MEDIUM RISK")

        else:

            st.success("🟢 LOW RISK")


        # ---------------------------------
        # Suspicious indicators
        # ---------------------------------

        st.subheader("🔎 Detected Indicators")


        if result["indicators"]:

            for indicator in result["indicators"]:

                category = indicator["category"]

                keywords = ", ".join(
                    indicator["keywords"]
                )

                st.write(
                    f"• **{category.title()}**: "
                    f"{keywords}"
                )

        else:

            st.write(
                "No suspicious indicators detected."
            )


        # ---------------------------------
        # Recommendation
        # ---------------------------------

        st.subheader("💡 Recommendation")

        st.info(
            result["recommendation"]
        )


    except ValueError as e:

        st.warning(
            f"⚠️ {str(e)}"
        )


    except Exception as e:

        st.error(
            "❌ Something went wrong while "
            "analyzing the message."
        )

        st.caption(
            f"Error type: {type(e).__name__}"
        )


# -----------------------------------------
# Footer
# -----------------------------------------

st.divider()

st.caption(
    "SWYNEX Internship — Task 3: Intelligent Feature"
)