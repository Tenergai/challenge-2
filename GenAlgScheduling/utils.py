import requests
from datetime import date
import pandas as pd
import numpy as np
def matrixToArray(matrix):
    # Initialize empty array
    array = []

    # Iterate over rows of matrix
    for row in matrix:
        # Iterate over elements in row
        for element in row:
            # Append element to array
            array.append(element)
    return array

def arrayToMatrix(array):
    matrix=[]
    max_index=[24,48,72,96,120,144,168,192,216]
    i=0
    for e in max_index:
        j=e-1
        m=array[i:j]
        matrix.append(m)
        i=e
    return matrix

# 1st argument --> numbers ranging from 0 to 9,
# 2nd argument, row = 2, col = 3
# array = np.random.randint(2, size=(10, 24))
# print(array)

def getPricesForToday():
    today=date.today()
    day=today.day
    month=today.month
    year=str(today.year)
    if month <10:
        month='0'+str(today.month)
    else:
        month=str(today.month)
    if day <10:
        day='0'+str(today.day)
    else:
        day=str(today.day)
    data=day+'_'+month+'_'+year
    url='https://www.omie.es/sites/default/files/dados/AGNO_'+year+'/MES_'+month+'/TXT/INT_MAJ_CONSUM_EV_H_HIST_'+data+'_'+data+'.TXT'
    req= requests.get(url)
    prices=req.text

    list_prices=prices.split(';\r\n')
    columns=list_prices[1]
    columns=columns.replace('\r\n','')
    columns=columns.split(';')
    list_prices=list_prices[2:]
    list_aux=[]
    for l in list_prices:
        list_aux.append(l.split(';'))
    list_prices=list_aux
    df_prices=pd.DataFrame(list_prices, columns=columns)
    df_prices.set_index('Fecha', inplace=True)
    prices_day=df_prices.loc[day+'/'+month+'/'+year]
    prices = prices_day['Precio MIBEL (EUR/MWh)']
    prices=prices.values
    for h in range(24):
        p=prices[h]
        prices[h]=float(p.replace(',','.'))
    return prices

def getDailyGeneration():
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
    data = {"day":day}
    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://127.0.0.1:5002/predict', json=data, headers=headers)
    # Process the data
    data = response.json()
    df = pd.DataFrame(data)
    return df
