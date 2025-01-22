import streamlit as st
import numpy as np
import pickle

# Load the pre-trained model
model_file = "clf_model.pkl"  # Replace with your model file path
with open('clf_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

# Streamlit App Title
st.title("Student Mental Health Prediction")

# Collect user input
st.header("Enter Student Details")
Gender = st.radio("Gender", options=["Female", "Male"], index=0)
Gender = 0 if Gender == "Female" else 1

Age = st.number_input("Age", min_value=10.0, max_value=100.0, step=1.0)
Academic_Pressure = st.slider("Academic Pressure (1-10)", min_value=1.0, max_value=10.0, step=0.1)
CGPA = st.slider("CGPA (0-10)", min_value=0.0, max_value=10.0, step=0.01)
Study_Satisfaction = st.slider("Study Satisfaction (1-10)", min_value=1.0, max_value=10.0, step=0.1)

Sleep_Duration = st.selectbox("Sleep Duration", options=["5-6 hours", "7-8 hours", "Less than 5 hours"])
Sleep_Duration = {"5-6 hours": 0, "7-8 hours": 1, "Less than 5 hours": 2}[Sleep_Duration]

Dietary_Habits = st.selectbox("Dietary Habits", options=["Healthy", "Moderate", "Unhealthy"])
Dietary_Habits = {"Healthy": 0, "Moderate": 1, "Unhealthy": 2}[Dietary_Habits]

Degree = st.selectbox(
    "Degree",
    options=["B.Pharm", "BA", "BCA", "BSc", "Class 12", "M.Tech", "MD", "MSc"]
)
Degree = {"B.Pharm": 0, "BA": 1, "BCA": 2, "BSc": 3, "Class 12": 4, "M.Tech": 5, "MD": 6, "MSc": 7}[Degree]

Suicidal_Thoughts = st.radio("Have you ever had suicidal thoughts?", options=["No", "Yes"])
Suicidal_Thoughts = 0 if Suicidal_Thoughts == "No" else 1

Work_Study_Hours = st.number_input("Work/Study Hours", min_value=0.0, max_value=24.0, step=0.5)
Financial_Stress = st.slider("Financial Stress (1-10)", min_value=1.0, max_value=10.0, step=0.1)

Family_History_Mental_Illness = st.radio("Family History of Mental Illness", options=["No", "Yes"])
Family_History_Mental_Illness = 0 if Family_History_Mental_Illness == "No" else 1

# Prepare the input data for prediction
input_data = np.array([[
    Gender,
    Age,
    Academic_Pressure,
    CGPA,
    Study_Satisfaction,
    Sleep_Duration,
    Dietary_Habits,
    Degree,
    Suicidal_Thoughts,
    Work_Study_Hours,
    Financial_Stress,
    Family_History_Mental_Illness
]])

# Prediction Button
if st.button("Predict"):
    # Make a prediction
    prediction = clf_model.predict(input_data)
    prediction_prob = clf_model.predict_proba(input_data)

    # Display Results
    st.subheader("Prediction Result")
    if prediction[0] == 1:
        st.error("The model predicts: The Student's Mental Health is NOT good.")
    else:
        st.success("The model predicts: The Student's Mental Health is GOOD.")

    st.subheader("Prediction Probabilities")
    st.write(f"Probability of Good Mental Health: {prediction_prob[0][0]:.2f}")
    st.write(f"Probability of Poor Mental Health: {prediction_prob[0][1]:.2f}")
