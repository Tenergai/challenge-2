import streamlit as sl
import plotly.express as px
import requests
import pandas as pd
import numpy as np


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

matriz = [  [0,1,0],
            [0,1,1],
            [0,0,1],
            [0,0,0],
            [1,0,1],
            [1,1,1],
            [1,1,1],
            [1,1,0],
            [1,1,1],
            [1,0,1],
            [1,1,0],
            [1,0,0],
            [1,0,1],
            [1,0,0],
            [0,1,1],
            [0,1,0],
            [1,0,0],
            [1,0,0],
            [0,0,1],
            [1,0,0],
            [1,0,1],
            [0,1,1],
            [1,1,1],
            [0,1,1]]
print(matriz)    


def build_matrix_graph(matrix):
    for i, hour in enumerate(matrix):
        for j,device in enumerate(hour):
            if device == 1:
                matrix[i][j] = device * (j+1)
            else:
                matrix[i][j] = np.nan
    matrix = pd.DataFrame(matrix,columns= ["device1","device2","device3"])
    sl.line_chart(matrix)    

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
def update_graph():
    day = [[0,8,6,1023,109,1,4,81,0,0,0],
    [1,8,5,1023,5,1,6,81,0,0,0],
    [2,7,5,1023,5,4,8,82,0,0,0],
    [3,7,4,1023,41,8,11,83,0,0,0],
    [4,6,4,1023,349,1,11,85,0,0,0],
    [5,6,3,1024,342,0,9,86,0,0,0],
    [6,6,3,1025,51,1,4,86,0,0,0],
    [8,8,5,1026,59,4,8,79,0,0,116],
    [9,9,5,1027,56,14,16,76,0,0,313],
    [10,10,6,1027,71,4,14,72,0,0,534],
    [11,13,5,1027,65,8,20,61,0,0,694],
    [12,14,5,1027,346,25,27,58,0,0,728],
    [13,14,8,1027,323,14,22,68,0,0,932],
    [14,14,7,1027,323,14,24,65,0,0,638],
    [15,14,8,1027,284,29,29,69,0,0,675],
    [16,14,8,1027,338,19,32,69,0,0,564],
    [17,14,9,1027,333,17,20,71,0,0,309],
    [18,12,9,1027,349,9,24,79,0,0,67],
    [19,12,9,1027,155,11,19,83,0,0,11],
    [21,12,10,1028,320,3,14,87,0,0,0],
    [22,12,10,1029,305,1,6,87,0,0,0],
    [23,12,10,1029,342,3,6,87,0,0,0]]
    df = fetch_data(day)
    # Create the figure
    sl.line_chart(df)


sl.write("""
# TenergAI
## Solar Generation Prediction """)
update_graph()

sl.write("""
## Device Scheduling
""")
build_matrix_graph(matriz)
