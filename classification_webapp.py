# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 00:00:25 2024

@author: Nidhi
"""

import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('D:/Python pros/diabetes/diabetes_model.sav','rb'))

#creating a function for prediction
def diabetes_prediction(input_data):
    

    #change i/p to numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    #reshape array as we are predicting for one datapoint
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    if(prediction[0]==0):
        return 'The person is not diabetic'
    else:
        return 'The person is diabetic'
    
    
def main():
    
    st.title('Diabetic Diagnosis For Women')
    #getting input from user
    preg= st.text_input('Number of pregnancies')
    glu= st.text_input('Glucose Level')
    bp = st.text_input('Blood Pressure')
    skt=st.text_input(' Skin Thickness')
    insulin=st.text_input('Insulin level')
    BMI=st.text_input('BMI')
    dpf=st.text_input('Diabetes Pedigree Function')
    age=st.text_input('Age')
    
    #prediction
    diagnosis = ''
    
    if st.button('Test Result'):
        diagnosis = diabetes_prediction([preg, glu, bp, skt, insulin, BMI, dpf, age])
        
    st.success(diagnosis)
    
if __name__ == '__main__':
    main()
    
    