def matrix_check_sym(matrix):
    for i in range(0, len(matrix)):
        for j in range(0, i):
            if (matrix[i][j] != matrix[j][i]):
                return False
    return True

#The code below is used just for testing.
#print(matrix_check_sym([[6,15,35],[15,55,225],[35,225,979]]))


