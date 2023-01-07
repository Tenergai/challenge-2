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
