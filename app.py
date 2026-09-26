import streamlit as st
from predictor import predict_message


st.set_page_config(
    page_title="AI SMS Spam Detector",
    page_icon="📩",
    layout="centered"
)


st.title("📩 AI SMS Spam Detector")
st.write(
    "Enter an SMS message below and let the integrated AI model "
    "classify it as Spam or Not Spam."
)

st.divider()

message = st.text_area(
    "Enter your SMS message:",
    placeholder="Example: Congratulations! You have won a free prize...",
    height=150
)

if st.button("🔍 Analyze SMS"):

    if not message.strip():
        st.warning("Please enter an SMS message first.")

    else:
        result = predict_message(message)

        st.subheader("Prediction")

        if result == "SPAM":
            st.error("🚨 SPAM MESSAGE")
            st.write("The AI model classified this message as spam.")

        else:
            st.success("✅ NOT SPAM")
            st.write("The AI model classified this message as not spam.")


st.divider()

st.caption(
    "Prototype built for SWYNEX Internship — Task 2: Model Integration"
)