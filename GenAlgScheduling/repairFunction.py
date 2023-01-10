import numpy as np

from deviceSpecification import getDevices, getPrecedences

# test_matrix = np.random.randint(2, size=(10, 24))

test = [
    [0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1],
    [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    [1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1],
    [0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1],
    [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
    [0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0],
    [0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1]
]


def check_elements(arr1, arr2):
    return all(val in arr2 for val in arr1)


def repairFunction(m):
    matrixToFix = np.array(m)
    # matrix = m
    # print(matrix)
    precedences = np.array(getPrecedences())
    # print(precedences)
    devices = getDevices()
    # print(devices)

    for i, row in enumerate(matrixToFix):
        # check hours on
        current_device = devices[i]
        print("Checking Device: ", i + 1, current_device["name"])
        hours_on = sum(row)
        print("Necessary Hours: ", current_device["hoursOn"], "Actual Hours Turned On: ", hours_on)
        if current_device["hoursOn"] != hours_on:
            print("Invalid Matrix - Necessary Hours")
            # break
        else:
            print("Valid Matrix - Necessary Hours")

        # check possible hours
        hours_device_was_on = np.where(row == 1)
        print("Possible Hours: ", current_device["possibleHours"], "Hours it was on: ", hours_device_was_on[0])

        if not check_elements(hours_device_was_on[0], current_device["possibleHours"]):
            print("Invalid Matrix - Possible Hours")
        else:
            print("Valid Matrix - Possible Hours")

            # check consecutive hours
        # check precedences
        print("Current Device: ", i + 1, current_device["name"])
        print("##################")
        preceded_by = np.where(precedences[i] == 1)
        print(preceded_by[0])
        print("##################")



    # for column in matrix.T:
    # print(column)

    return 0


repairFunction(test)
