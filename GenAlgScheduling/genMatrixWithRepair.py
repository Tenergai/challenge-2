import random

import numpy as np
from deviceSpecification import getDevices
from generateMatrix import generateMatrix, getNMatrices
from repairFunction import repairFunction
import time

def validateChild(matrix):
    validation, nec_hours_error, consec_hours_error, poss_hour_error, precd_hours_error = repairFunction(matrix)
    return validation, poss_hour_error





# generates n matrices
def generateAndRepair(n_matrix, max_iter):
    start_time = time.time()
    sum_necessary_hours_error_counter = 0
    sum_consecutive_hours_error_counter = 0
    sum_possible_hours_error_counter = 0
    sum_precedence_hours_error_counter = 0
    devices = getDevices()
    generated_matrix_array = []
    curr_iter = 0

    while len(generated_matrix_array) < n_matrix:
        if curr_iter >= max_iter:
            break
        print("curr_iter: ", curr_iter)
        a_matrix = generateMatrix(devices)
        validation, nec_hours_error, consec_hours_error, poss_hour_error, precd_hours_error = repairFunction(a_matrix)
        sum_necessary_hours_error_counter += nec_hours_error
        sum_consecutive_hours_error_counter += consec_hours_error
        sum_possible_hours_error_counter += poss_hour_error
        sum_precedence_hours_error_counter += precd_hours_error
        if validation:
            generated_matrix_array.append((a_matrix, poss_hour_error))
        curr_iter += 1

    errs = [sum_necessary_hours_error_counter, sum_consecutive_hours_error_counter, sum_possible_hours_error_counter,
            sum_precedence_hours_error_counter]

    end_time = time.time()
    return generated_matrix_array, errs, curr_iter, end_time - start_time


# generates n matrices
def generateAndRepairTime(n_matrix, mins):
    start_time = time.time()
    end_time = start_time + (mins * 60)
    sum_necessary_hours_error_counter = 0
    sum_consecutive_hours_error_counter = 0
    sum_possible_hours_error_counter = 0
    sum_precedence_hours_error_counter = 0
    devices = getDevices()
    generated_matrix_array = []
    curr_iter = 0

    while len(generated_matrix_array) < n_matrix:
        if time.time() >= end_time:
            break
        print("curr_iter: ", curr_iter)
        a_matrix = generateMatrix(devices)
        validation, nec_hours_error, consec_hours_error, poss_hour_error, precd_hours_error = repairFunction(a_matrix)
        sum_necessary_hours_error_counter += nec_hours_error
        sum_consecutive_hours_error_counter += consec_hours_error
        sum_possible_hours_error_counter += poss_hour_error
        sum_precedence_hours_error_counter += precd_hours_error
        if validation:
            generated_matrix_array.append(a_matrix)
        curr_iter += 1

    errs = [sum_necessary_hours_error_counter, sum_consecutive_hours_error_counter, sum_possible_hours_error_counter,
            sum_precedence_hours_error_counter]

    return generated_matrix_array, errs, curr_iter


result, errors, iterations_ran, t = generateAndRepair(6, 10000)
# result, errors, iterations_ran = generateAndRepairTime(4, 10)

print("#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
print(result)
print("Iterations ran:", iterations_ran)
print("Necessary Hours Errors: ", errors[0])
print("Consecutive Hours Errors: ", errors[1])
print("Possible Hours Errors: ", errors[2])
print("Precedence Hours Errors: ", errors[3])
print("Time: ", t, " s ", t / 60, " min")
print("#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
