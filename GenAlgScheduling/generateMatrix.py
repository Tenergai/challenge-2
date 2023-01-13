import random
import numpy as np
from deviceSpecification import getDevices


devices = getDevices()
emptyMatrix = []


# generates 1 matrix based on HoursOn from every device ([2][7], corresponds to hour 7 of device 2 ), also packs the hours in consecutive hours
def generateMatrix(devices):
    emptyMatrix = []
    for i in range(len(devices)):
        hoursOn = devices[i]["hoursOn"]
        #print(hoursOn)
        consecutiveHours = devices[i]["consecutiveHours"]
        arrayDevice = [1] * hoursOn + [0] * (24 - hoursOn)
        random.shuffle(arrayDevice)
        #print(arrayDevice)
        count = 0
        new_array = []
        for j in range(len(arrayDevice)):
            if len(new_array) < 24:
                if arrayDevice[j] == 1:
                    count += 1
                    if count == consecutiveHours:
                        new_array.append(1)
                        count = 0
                    else:
                        new_array.append(1)
                        for k in range(j + 1, len(arrayDevice)):
                            if arrayDevice[k] == 1:
                                # time.sleep(2.4)
                                new_array.append(1)
                                arrayDevice[k] = 0
                else:
                    new_array.append(0)
        if i ==0:
            emptyMatrix = np.array(new_array)
        else:
            emptyMatrix = np.vstack((emptyMatrix, new_array))
    return emptyMatrix

# generates n matrices
def getNMatrices(n):
    devices = getDevices()
    emptyMatrix = []
    for i in range(n):
        emptyMatrix.append(generateMatrix(devices))
    return emptyMatrix


"""def experimental(device):
    hoursOn = device["hoursOn"]
    print(hoursOn)
    consecutiveHours = device["consecutiveHours"]
    arrayDevice = [1] * hoursOn + [0] * (24 - hoursOn)
    random.shuffle(arrayDevice)
    print(arrayDevice)
    count = 0
    new_array = []

    for j in range(len(arrayDevice)):
        if len(new_array)<24:
            if arrayDevice[j] == 1:
                count += 1
                if count == consecutiveHours:
                    new_array.append(1)
                    count = 0
                else:
                    new_array.append(1)
                    for k in range(j + 1, len(arrayDevice)):
                        if arrayDevice[k] == 1:
                            #time.sleep(2.4)
                            new_array.append(1)
                            arrayDevice[k] = 0
            else:
                new_array.append(0)
    return new_array
"""

m = generateMatrix(devices)
if __name__ == "__main__":
    print(m)
#print(devices[9])
#m = experimental(devices[9])
#print(m, len(m))
