import numpy as np

from deviceSpecification import getDevices, getPrecedences

# test_matrix = np.random.randint(2, size=(10, 24))

test = [
    [0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1],
    [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1],
    [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
    [0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0],
    [0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


def check_value_in_range(arr, start_index, end_index, value):
    for i in range(start_index, end_index + 1):
        if arr[i] == value:
            return True
    return False


def check_elements(arr1, arr2):
    return all(val in arr2 for val in arr1)


def repairFunction(m):
    necessary_hours_error_counter = 0
    consecutive_hours_error_counter = 0
    possible_hours_error_counter = 0
    precedence_hours_error_counter = 0
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
        # print("##########")
        print("Checking Device: ", i, " - ", current_device["name"])
        hours_on = sum(row)
        # print("Necessary Hours: ", current_device["hoursOn"], "Actual Hours Turned On: ", hours_on)
        if current_device["hoursOn"] != hours_on:
            necessary_hours_error_counter += 1
            # print("Invalid Matrix - Necessary Hours")
            return False, necessary_hours_error_counter, consecutive_hours_error_counter, possible_hours_error_counter, precedence_hours_error_counter
        else:
            print("Valid Matrix - Necessary Hours")
        # print("##########")
        # print("Consecutives: ")
        # print(row)
        # check consecutive hours
        consecutives_max = 0;
        consecutives_min = 99;
        consecutives_counter = 0;
        for y in range(len(row)):
            if row[y] == 1:
                consecutives_counter += 1;
                if y == len(row) - 1:
                    # print("Last iteration")
                    # consecutives_total.append(consecutives_counter)
                    if consecutives_counter > consecutives_max:
                        consecutives_max = consecutives_counter
                    if consecutives_counter < consecutives_min and consecutives_counter != 0:
                        consecutives_min = consecutives_counter
                    consecutives_counter = 0
            elif row[y] == 0:
                # consecutives_total.append(consecutives_counter)
                if consecutives_counter > consecutives_max:
                    consecutives_max = consecutives_counter
                if consecutives_counter < consecutives_min and consecutives_counter != 0:
                    consecutives_min = consecutives_counter
                consecutives_counter = 0
        if current_device["consecutiveHours"] != consecutives_max or current_device[
            "consecutiveHours"] != consecutives_min:
            consecutive_hours_error_counter += 1
            # print("Invalid consecutive: ", "Consecutive Hours: ", current_device["consecutiveHours"], "Max: ",consecutives_max, "Min: ", consecutives_min)
            return False, necessary_hours_error_counter, consecutive_hours_error_counter, possible_hours_error_counter, precedence_hours_error_counter
        else:
            print("Valid consecutive: ", "Consecutive Hours: ", current_device["consecutiveHours"], "Max: ",
                  consecutives_max, "Min: ", consecutives_min)
        # if row[y] == row[y + 1] and row[y] == 1:
        #   consecutives.append(y)
        #  print("Consecutive 1's found")
        # elif row[y] == row[y - 1] and row[y] == 1:
        #   consecutives.append(y)

        # print(consecutives)
        # print("##########")
        # check possible hours
        hours_device_was_on = np.where(row == 1)
        # print("Possible Hours: ", current_device["possibleHours"], "Hours it was on: ", hours_device_was_on[0])

        if not check_elements(hours_device_was_on[0], current_device["possibleHours"]):
            # print("Invalid Matrix - Possible Hours")
            possible_hours_error_counter += 1
            return False, necessary_hours_error_counter, consecutive_hours_error_counter, possible_hours_error_counter, precedence_hours_error_counter
        else:
            print("Valid Matrix - Possible Hours")
        # print("##########")
        # check precedences
        # print("Current Device: ", i, current_device["name"])
        preceded_by = list(np.where(precedences[i] == 1))[0]
        # print("Preceded by: ")
        if len(preceded_by) > 0:
            # print(preceded_by)
            for o, p in enumerate(preceded_by):  # ver cada precedencia
                preceded_by_matrix = matrixToFix[p]
                # print(row)
                asdads = row
                # print(preceded_by_matrix)
                min_index_for_search = 0
                following_val = 0
                for index, val in enumerate(row):  # ver cada hora de começo
                    if index == len(row) - 1:
                        print("Last iteration")
                    # print(index,v)
                    previous_val = row[index - 1]
                    if index != len(row) - 1:
                        following_val = row[index + 1]
                    if val == 1 and previous_val == 0:  # if começou
                        if check_value_in_range(preceded_by_matrix, min_index_for_search, index - 1, 1):
                            print("Valid")
                        else:
                            # print("Invalid Matrix - Invalid Precedence")
                            precedence_hours_error_counter += 1
                            return False, necessary_hours_error_counter, consecutive_hours_error_counter, possible_hours_error_counter, precedence_hours_error_counter

                    elif val == 1 and previous_val == 1 and following_val == 0 and index != len(
                            row) - 1:  # termino do trabalho, avoid last iteration
                        min_index_for_search = index
        else:
            print("None")

    # if 0 - 1, then preceding device hr before must be 1

    # for column in matrix.T:
    # print(column)

    return True, necessary_hours_error_counter, consecutive_hours_error_counter, possible_hours_error_counter, precedence_hours_error_counter


repairFunction(test)
