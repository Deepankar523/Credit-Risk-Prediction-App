import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("credit_risk_model.pkl", "rb"))

st.title("💳 AI Credit Risk Prediction System")

st.write("Enter applicant details below:")

# Create input fields (21 features — same order as dataset except 'kredit')

laufkont = st.number_input("Checking Account Status")
laufzeit = st.number_input("Loan Duration (months)")
moral = st.number_input("Credit History")
verw = st.number_input("Purpose")
hoehe = st.number_input("Credit Amount")
sparkont = st.number_input("Savings Account")
beszeit = st.number_input("Employment Duration")
rate = st.number_input("Installment Rate")
famges = st.number_input("Personal Status")
buerge = st.number_input("Guarantor")
wohnzeit = st.number_input("Residence Duration")
verm = st.number_input("Property")
alter = st.number_input("Age")
weitkred = st.number_input("Other Installment Plans")
wohn = st.number_input("Housing")
bishkred = st.number_input("Existing Credits")
beruf = st.number_input("Job")
pers = st.number_input("Number of Dependents")
telef = st.number_input("Telephone")
gastarb = st.number_input("Foreign Worker")

if st.button("Predict Risk"):
    input_data = np.array([[laufkont, laufzeit, moral, verw, hoehe, sparkont,
                            beszeit, rate, famges, buerge, wohnzeit, verm,
                            alter, weitkred, wohn, bishkred, beruf,
                            pers, telef, gastarb]])

    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)

    if prediction[0] == 1:
        st.success(f"Low Risk ✅ (Confidence: {max(probability[0])*100:.2f}%)")
    else:
        st.error(f"High Risk ❌ (Confidence: {max(probability[0])*100:.2f}%)")