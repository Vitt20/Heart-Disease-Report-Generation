import numpy as np
import pickle
import streamlit as st

# Load the model from disk using pickle
with open("final_model_KNN.pkl", "rb") as file:
    model = pickle.load(file)

# Set up the Streamlit page configuration
st.set_page_config(page_title="Heart Health Prediction App", page_icon="❤️", layout="centered", initial_sidebar_state="expanded")

def preprocess(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal):
    # Convert user input to numerical values
    sex = 1 if sex == "male" else 0
    
    cp_dict = {
        "Typical angina": 0,
        "Atypical angina": 1,
        "Non-anginal pain": 2,
        "Asymptomatic": 3
    }
    cp = cp_dict.get(cp, 0)
    
    fbs = 1 if fbs == "Yes" else 0
    
    restecg_dict = {
        "Nothing to note": 0,
        "ST-T Wave abnormality": 1,
        "Possible or definite left ventricular hypertrophy": 2
    }
    restecg = restecg_dict.get(restecg, 0)
    
    exang = 1 if exang == "Yes" else 0
    
    slope_dict = {
        "Upsloping: better heart rate with exercise (uncommon)": 0,
        "Flatsloping: minimal change (typical healthy heart)": 1,
        "Downsloping: signs of unhealthy heart": 2
    }
    slope = slope_dict.get(slope, 0)
    
    # Create a 2D array for the model input
    user_input = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
    
    # Predict using the model
    prediction = model.predict(user_input)
    
    return prediction

# Display the front end of the app
st.title("Heart Disease Prediction App 📱 V1.0")
st.subheader('Designed by Dhiraj Chavan (Assignment)')

# Collect user input
age = st.selectbox("Age", range(1, 121))
sex = st.radio("Select Gender", ('male', 'female'))
cp = st.radio('Chest Pain Type', ("Typical angina", "Atypical angina", "Non-anginal pain", "Asymptomatic"))
trestbps = st.selectbox('Resting Blood Pressure', range(1, 501))
chol = st.selectbox('Serum Cholestoral in mg/dl', range(1, 1001))
fbs = st.radio("Fasting Blood Sugar higher than 120 mg/dl", ['Yes', 'No'])
restecg = st.radio('Resting Electrocardiographic Results', ("Nothing to note", "ST-T Wave abnormality", "Possible or definite left ventricular hypertrophy"))
thalach = st.selectbox('Maximum Heart Rate Achieved', range(1, 301))
exang = st.radio('Exercise Induced Angina', ["Yes", "No"])
oldpeak = st.number_input('Oldpeak', format="%.2f")
slope = st.radio('Heart Rate Slope', ("Upsloping: better heart rate with exercise (uncommon)", "Flatsloping: minimal change (typical healthy heart)", "Downsloping: signs of unhealthy heart"))
ca = st.selectbox('Number of Major Vessels Colored by Flourosopy', range(0, 5))
thal = st.selectbox('Thalium Stress Result', range(0, 4))

# Predict button
if st.button("Predict"):
    pred = preprocess(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal)
    
    if pred == 0:
        st.error('Predicted that there are more chances of Heart disease')
    elif pred == 1:
        st.success('Predicted that there are less chances of Heart disease')

# Sidebar information
st.sidebar.subheader("About App")
st.sidebar.info("Version 1.0")
st.sidebar.info("📱 Contact: +919881539987")
