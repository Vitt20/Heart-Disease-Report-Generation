import numpy as np
import joblib
import streamlit as st

# Load the model from disk
model = joblib.load("final_model_KNN.pkl")

st.set_page_config(page_title="Heart Health Prediction App", page_icon="DVC", layout="centered", initial_sidebar_state="expanded")

def preprocess(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal):   
    # Pre-processing user input   
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
        "Upsloping: better heart rate with excercise(uncommon)": 0,
        "Flatsloping: minimal change(typical healthy heart)": 1,
        "Downsloping: signs of unhealthy heart": 2
    }
    slope = slope_dict.get(slope, 0)
    
    user_input = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
    prediction = model.predict(user_input)
    
    return prediction

# Front end elements of the web page 
html_temp = """ 
    <div style ="background-color:silver;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Heart Disease Prediction App 📱 V1.0</h1> 
    </div> 
"""
st.markdown(html_temp, unsafe_allow_html=True) 
st.subheader('Designed by :- Dhiraj Chavan (Assignment)')

# User input
age = st.selectbox("Age", range(1, 121, 1))
sex = st.radio("Select Gender: ", ('male', 'female'))
cp = st.radio('Chest Pain Type', ("Typical angina", "Atypical angina", "Non-anginal pain", "Asymptomatic"))
trestbps = st.selectbox('Resting Blood Sugar', range(1, 500, 1)) 
chol = st.selectbox('Serum Cholestoral in mg/dl', range(1, 1000, 1))
fbs = st.radio("Fasting Blood Sugar higher than 120 mg/dl", ['Yes', 'No'])
restecg = st.radio('Resting Electrocardiographic Results', ("Nothing to note", "ST-T Wave abnormality", "Possible or definite left ventricular hypertrophy"))
thalach = st.selectbox('Maximum Heart Rate Achieved', range(1, 300, 1))
exang = st.radio('Exercise Induced Angina', ["Yes", "No"])
oldpeak = st.number_input('Oldpeak')
slope = st.radio('Heart Rate Slope', ("Upsloping: better heart rate with excercise(uncommon)", "Flatsloping: minimal change(typical healthy heart)", "Downsloping: signs of unhealthy heart"))
ca = st.selectbox('Number of Major Vessels Colored by Flourosopy', range(0, 5, 1))
thal = st.selectbox('Thalium Stress Result', range(0, 4, 1))

# Predict
if st.button("Predict"):
    pred = preprocess(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal)
    
    if pred == 0:
        st.error('Predicted that there are more chances of Heart disease')
    elif pred == 1:
        st.success('Predicted that there are less chances of Heart disease')

st.sidebar.subheader("About App")
st.sidebar.info("R1.0 V1.0 ")
st.sidebar.info("📱 : +919881539987")
