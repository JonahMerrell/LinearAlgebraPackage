
import sys, os
sys.path.append(os.path.abspath('../../mylibrary'))
from _mymodules import matrix_find_eigenvalues

def hilbert_matrix_find_eigenvalues_test():

    selection = [4,6,8,10]
    hilbert_matrix = []
    solution = []

    # Create the hilbert matrices and their corresponding Q factorization matrix.
    for n in selection:
        hilbert_matrix.append([[1/(1+i+j) for i in range(n)] for j in range(n)])  # Hilbert Matrix generator
        solution.append(matrix_find_eigenvalues(hilbert_matrix[-1]))

    for i in range(0,len(selection)):  # 4, 6, 8, 10
        print("Eigenvalues for " + str(selection[i]) + "x" + str(selection[i]) + ": " + str(solution[i]))

hilbert_matrix_find_eigenvalues_test()