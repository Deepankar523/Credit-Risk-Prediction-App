import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("credit_risk_model.pkl", "rb"))

st.set_page_config(page_title="Credit Risk Prediction", layout="centered")

st.title("💳 AI Credit Risk Prediction System")
st.markdown("### Enter Applicant Details")

# Sliders for key features
laufkont = st.slider("Checking Account Status", 0, 4, 1)
laufzeit = st.slider("Loan Duration (months)", 4, 72, 12)
hoehe = st.slider("Credit Amount", 250, 20000, 5000)
alter = st.slider("Age", 18, 75, 30)
sparkont = st.slider("Savings Account Status", 0, 4, 1)
beszeit = st.slider("Employment Duration", 0, 4, 1)
rate = st.slider("Installment Rate (%)", 1, 4, 2)
bishkred = st.slider("Existing Credits", 1, 4, 1)

# Create dummy values for remaining features (kept constant)
dummy_values = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

if st.button("Predict Risk"):

    input_data = np.array([[laufkont, laufzeit, 1, 1, hoehe,
                            sparkont, beszeit, rate, 1, 1,
                            1, 1, alter, 1, 1,
                            bishkred, 1, 1, 1, 1]])

    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)

    if prediction[0] == 1:
        st.success(f"Low Risk ✅")
        st.info(f"Confidence: {max(probability[0])*100:.2f}%")
    else:
        st.error("High Risk ❌")
        st.warning(f"Confidence: {max(probability[0])*100:.2f}%")
