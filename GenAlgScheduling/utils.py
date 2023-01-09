import requests
from datetime import date
import pandas as pd
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
    return prices
