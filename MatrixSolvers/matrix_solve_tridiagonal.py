'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       November 21 2019
written for:        Homework7 Task8
course:             Math 4610

purpose:            This method will compute the solution of a tridiagonal linear system of equations.
'''

def matrix_solve_tridiagonal(matrix,vector):
    #matrix_storage is a n*3 matrix, where each row represents the 3 non-zero values in the tridiagonal n*n matrix
    tempDiagonal = [matrix[i][1] for i in range(len(matrix))]
    n = len(matrix)
    solution = [0]*len(vector)

    for i in range(1, n):# we start at n-2, because the very last entry in matrix_storage is irrelivant, and not techinuqally in the matrix n*n.
        w = matrix[i][0]/tempDiagonal[i-1]
        tempDiagonal[i] -= w* matrix[i-1][2]
        vector[i] -= w* vector[i-1]
        #matrix_storage[i][0] = 0 #We dont actually have to do this, we just know that they're 0 now.

    #now do back substitution
    solution[n-1] = vector[n-1]/tempDiagonal[i]
    for i in range(n-2, -1, -1):
        solution[i] = (vector[i] - matrix[i][2] *solution[i+1])/tempDiagonal[i]
    return solution


#The code below is used just for testing.
#matrix = [[0,8,10],[5,2,5],[4,2,2],[3,6,0]]
#vector = [12,25,38,27]
#print(matrix_solve_tridiagonal(matrix,vector))
