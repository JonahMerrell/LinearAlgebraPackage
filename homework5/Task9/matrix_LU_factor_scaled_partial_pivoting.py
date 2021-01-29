'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       November 9 2019
written for:        Homework5 Task9
course:             Math 4610

purpose:            This method will return the LU-factorization of a square matrix, using scaled partial pivoting.
                    The matrix "A" contains the elements that form L and U, and the 0s and 1s are implied.
'''

import copy

def matrix_LU_factor_scaled_partial_pivoting(matrix):
    A = copy.deepcopy(matrix)
    n = len(A)
    x =  [0 for i in range(n)]
    s = [0 for i in range(n)] #s stores the scale we will use for each row
    indmap = [i for i in range(n)]

    #First, we compute the scale we will use for each row, and store it in s.
    for i in range(n):
        s[i] = abs(A[i][0])
        for j in range(1,n):
            valchk = abs(A[i][j])
            if valchk > s[i]:
                s[i] = valchk

    for k in range(0,n-1):
        #Next, we find largest the row with the largest k-th entry, and then swap the rows so that largest is in the k-th spot.
        indtmp = indmap[k]
        valmax = abs(A[indmap[k]][k])/s[indmap[k]]#apply scaling here
        for i in range(k+1,n):
            valchk = abs(A[indmap[i]][k])/s[indmap[i]]#apply scaling here
            if (valchk > valmax):
                valmax = valchk
                indtmp = indmap[i]
        indmap[k],indmap[indtmp] = indmap[indtmp],indmap[k]

        #Next, we perform row-operations to make first entry in all rows below become 0. (to acheive upper-trianguler)
        for i in range(k+1,n):
            A[indmap[i]][k] = A[indmap[i]][k]/A[indmap[k]][k]
            for j in range(k+1,n):
                A[indmap[i]][j] = A[indmap[i]][j] - A[indmap[i]][k]*A[indmap[k]][j]

    return A #The matrix "A" contains the elements that form L and U, and the 0s and 1s are implied.

#The code below is used just for testing.
#matrix_example = [[1,1,-1],[1,-2,3],[2,3,1]]
#LU = matrix_LU_factor_scaled_partial_pivoting(matrix_example)
#U = [[(LU[i][j] if (i<=j) else 0.0) for j in range(len(LU))] for i in range(len(LU))]
#L = [[(LU[i][j] if (i>j) else (1.0 if (i == j) else 0.0)) for j in range(len(LU))] for i in range(len(LU))]
#print(U)
#print(L)



