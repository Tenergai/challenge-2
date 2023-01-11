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
        print("##########")
        print("Checking Device: ", i, " - ", current_device["name"])
        hours_on = sum(row)
        print("Necessary Hours: ", current_device["hoursOn"], "Actual Hours Turned On: ", hours_on)
        if current_device["hoursOn"] != hours_on:
            print("Invalid Matrix - Necessary Hours")
            # break
        else:
            print("Valid Matrix - Necessary Hours")
        print("##########")
        print("Consecutives: ")
        print(row)
        # check consecutive hours
        consecutives_max = 0;
        consecutives_min = 99;
        consecutives_counter = 0;
        for y in range(len(row)):
            if row[y] == 1:
                consecutives_counter += 1;
                if y == len(row) - 1:
                    print("Last iteration")
                    # consecutives_total.append(consecutives_counter)
                    if consecutives_counter > consecutives_max:
                        consecutives_max = consecutives_counter
                    elif consecutives_counter < consecutives_min and consecutives_counter != 0:
                        consecutives_min = consecutives_counter
                    consecutives_counter = 0
            elif row[y] == 0:
                # consecutives_total.append(consecutives_counter)
                if consecutives_counter > consecutives_max:
                    consecutives_max = consecutives_counter
                elif consecutives_counter < consecutives_min and consecutives_counter != 0:
                    consecutives_min = consecutives_counter
                consecutives_counter = 0
        #ajeitar isto
        if current_device["consecutiveHours"] != consecutives_max and current_device[
            "consecutiveHours"] != consecutives_min:
            print("Invalid consecutive: ", "Consecutive Hours: ", current_device["consecutiveHours"], "Max: ",
                  consecutives_max, "Min: ", consecutives_min)
        else:
            print("Valid consecutive: ", "Consecutive Hours: ", current_device["consecutiveHours"], "Max: ",
                  consecutives_max, "Min: ", consecutives_min)
        # if row[y] == row[y + 1] and row[y] == 1:
        #   consecutives.append(y)
        #  print("Consecutive 1's found")
        # elif row[y] == row[y - 1] and row[y] == 1:
        #   consecutives.append(y)

        # print(consecutives)
        print("##########")
        # check possible hours
        hours_device_was_on = np.where(row == 1)
        print("Possible Hours: ", current_device["possibleHours"], "Hours it was on: ", hours_device_was_on[0])

        if not check_elements(hours_device_was_on[0], current_device["possibleHours"]):
            print("Invalid Matrix - Possible Hours")
        else:
            print("Valid Matrix - Possible Hours")
        print("##########")
        # check precedences
        # print("Current Device: ", i, current_device["name"])
        preceded_by = list(np.where(precedences[i] == 1))
        print(preceded_by[0])

    # if 0 - 1, then preceding device hr before must be 1

    # for column in matrix.T:
    # print(column)

    return 0


repairFunction(test)
