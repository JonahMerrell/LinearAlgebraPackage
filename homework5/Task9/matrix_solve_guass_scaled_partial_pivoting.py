'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       November 9 2019
written for:        Homework5 Task9
course:             Math 4610

purpose:            This method will solve a system of linear equations by performing guass elimination, followed with back substitution.
                    scaled partial pivoting is also implmemented to speed up the algorithm.
'''

#import sys, os
#sys.path.append(os.path.abspath('../../mylibrary'))
#from _mymodules import matrix_solve_upper_tri, matrix_solve_lower_tri,matrix_LU_factor
import copy

def matrix_solve_guass_scaled_partial_pivoting(matrix,vector):
    A = copy.deepcopy(matrix)
    b = copy.deepcopy(vector)
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
            factor = A[indmap[i]][k]/A[indmap[k]][k]
            #A[indmap[i]][k] = 0 #techniqually, we dont need to do this, if we just remember that its upper-traingular
            for j in range(k+1,n):
                A[indmap[i]][j] = A[indmap[i]][j] - factor*A[indmap[k]][j]
            b[indmap[i]] = b[indmap[i]]-factor*b[indmap[k]]
    #Now we perform back substitution to solve for x
    x[n-1] = b[indmap[n-1]]/A[indmap[n-1]][n-1]
    for i in range(n-2,-1,-1):
        sum = b[indmap[i]]
        for j in range(i+1,n):
            sum -= A[indmap[i]][j]*x[j]
        x[i] = sum/A[indmap[i]][i]

    return x





#The code below is used just for testing.
matrix_example = [[1,1,-1],[1,-2,3],[2,3,1]]
vector_example = [4,-6,7]
print(matrix_solve_guass_scaled_partial_pivoting(matrix_example,vector_example))


