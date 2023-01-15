import streamlit as sl
import plotly.express as px
import requests
import pandas as pd
import numpy as np
import sys
sys.path.append('.')
from GenAlgScheduling.ga import ga

def fetch_rf():
    response = requests.get('http://127.0.0.1:5002/train_rf')
    # Process the data
    data = response.json()
    return data['score']

def fetch_dt():
    response = requests.get('http://127.0.0.1:5002/train_dt')
    # Process the data
    data = response.json()
    return data['score']
def fetch_svm():
    response = requests.get('http://127.0.0.1:5002/train_svm')
    # Process the data
    data = response.json()
    return data['score']

best_individual, device_names, matriz, day = ga()

def build_matrix_graph(matrix):    
    matrix = matrix.tolist()
    matrix = extend_one_hour(matrix)
    matrix = np.transpose(matrix)
    matrix = matrix.tolist()
    matrix = set_null_values_nan(matrix)
    matrix = pd.DataFrame(matrix, columns=device_names)
    #print(matrix)
    sl.line_chart(matrix)    

def extend_one_hour(matrix):
    for device in range(len(matrix)):
        matrix[device].append(0)
    for device in range(len(matrix)):
        for hour in range(len(matrix[device])):
            if hour < 24:
                if matrix[device][hour] == 1 and matrix[device][hour+1] == 0:
                    matrix[device][hour+1] = -1

    for device in range(len(matrix)):
        for hour in range(len(matrix[device])):
            if matrix[device][hour] == -1:
                matrix[device][hour] = 1
    return matrix

def set_null_values_nan(matrix):
    for i, hour in enumerate(matrix):
        for j,device in enumerate(hour):
            if device == 1:
                matrix[i][j] = device * (j+1)
                
            else:
                matrix[i][j] = np.nan
    return matrix

def update_graph(data):
    #df = fetch_data(day)
    # Create the figure
    sl.line_chart(data)

option = sl.selectbox(
        "What model do you want to use?",
        ("Random Forest", "Decision Trees", "SVR"),
    )

if option == "Random Forest":
    score = fetch_rf()
if option == "Decision Trees":
    score = fetch_dt()
if option == "SVR":
    score = fetch_svm()

sl.write("Score: ",score)

sl.write("""
# TenergAI
## Solar Generation Prediction """)
update_graph(day)

sl.write("""
## Device Scheduling
""")
build_matrix_graph(matriz)
