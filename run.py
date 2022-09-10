import time
import json
import requests
import io
import streamlit as st

backend = "http://127.0.0.1:8000/predict"
st.title('Iris prediction')

sepal_len = st.text_input('sepal_len')
sepal_width = st.text_input('sepal_width')
petal_len = st.text_input('petal_len')
petal_width = st.text_input('petal_width')

data = {'sepal_length' : sepal_len, 'sepal_width' : sepal_width, 
        'petal_length' : petal_len, 'petal_width' : petal_width}

header = {'Content-Type': 'application/json'}

res = requests.post(backend, headers = header, 
                       json = data)

pred = st.button(label='Predict')
if pred:
    result = res.text
    st.write(f"Prediction result is {result}!!!")