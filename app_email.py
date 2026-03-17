import streamlit as st
import pickle

# Load model
model = pickle.load(open("spam_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

st.title("📧 Spam Email Detector")

user_input = st.text_area("Enter your message")

if st.button("Predict"):
    data = vectorizer.transform([user_input])
    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("🚨 Spam Message")
    else:
        st.success("✅ Not Spam")