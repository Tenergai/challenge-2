import streamlit as sl
import plotly.express as px
import requests
import pandas as pd
import numpy as np
import sys
sys.path.append('.')
from GenAlgScheduling.ga import ga

# Function to fetch the data from the API
def fetch_data(data):
    # Make the request to the API
    data = {"day":data}
    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://127.0.0.1:5002/predict', json=data, headers=headers)
    # Process the data
    data = response.json()
    df = pd.DataFrame(data)
    return df

best_individual, device_names, matriz, day = ga()

def build_matrix_graph(matrix):
    matrix = np.transpose(matrix)
    matrix = matrix.tolist()
    for i, hour in enumerate(matrix):
        for j,device in enumerate(hour):
            if device == 1:
                matrix[i][j] = device * (j+1)
            else:
                matrix[i][j] = np.nan
    matrix = pd.DataFrame(matrix, columns=device_names)
    sl.line_chart(matrix)    

def update_graph(day):
    #df = fetch_data(day)
    # Create the figure
    sl.line_chart(day)


sl.write("""
# TenergAI
## Solar Generation Prediction """)
""" 8,191,
9,266,
10, 2952,
11, 4559,
12, 5296,
13, 2581,
14, 4181,
15, 2110,
16, 822,
17, 1152,
18, 418,
19, 73, """
update_graph(day)

sl.write("""
## Device Scheduling
""")
build_matrix_graph(matriz)
