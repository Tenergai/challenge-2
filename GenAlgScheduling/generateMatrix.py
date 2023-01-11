import random

import numpy as np
from deviceSpecification import getDevices

# print(precedences)



devices = getDevices()
emptyMatrix = []

#generates 1 matrix based on HoursOn from every device ([2][7], corresponds to hour 7 of device 2 )
def generateMatrix(devices):
    emptyMatrix = []
    for i in range(len(devices)):
        hoursOn = devices[i]["hoursOn"]
        arrayDevice = [1] * hoursOn + [0] * (24-hoursOn)
        random.shuffle(arrayDevice)
        if i ==0:
            emptyMatrix = np.array(arrayDevice)
        else:
            emptyMatrix = np.vstack((emptyMatrix, arrayDevice))
    return emptyMatrix

#generates n matrices
def getNMatrices(n):
    devices = getDevices()
    emptyMatrix = []
    for i in range(n):
        emptyMatrix.append(generateMatrix(devices))
    return emptyMatrix


m = getNMatrices(2)
#print(m[0] ,'\n\n\n' ,m[1])