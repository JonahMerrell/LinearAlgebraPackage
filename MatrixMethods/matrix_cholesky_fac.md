# Software Manual (matrix_cholesky_fac.py)

## [Back](softwaremanual.md)

**Routine Name:**           matrix_cholesky_fac.py

**Author:** Jonah Merrell

**Language:** Python 3.7.0

**Description/Purpose:** This routine will perform the Cholesky factorization method for square matrices

**Input:** argument1: The matrix to perform cholesky factorization on.<br>

**Output:** This routine returns a matrix resulting from performing cholesky factorization on the input matrix given.

**Usage/Example:**

Below shows an example of performing cholesky factorization on a positive definate symetrical matrix using "matrix_cholesky_fac" (one row is printed at a time, for
 readabilities sake).

      A_ = matrix_cholesky_fac([[3,-1,0],[-1,2,-1],[0,-1,2]])
      for i in range(len(A_)):
          print(A_[i])

Output from the lines above:

      [[1.7320508075688772, 0, 0], 
	  [-0.5773502691896258, 1.2909944487358056, 0], 
	  [0.0, -0.7745966692414834, 1.1832159566199232]]

The above matrix printed is the cholesky-factorized result of the original matrix.

**Implementation/Code:** The following is the code for matrix_cholesky_fac()

      import sys, os
      sys.path.append(os.path.abspath('../../mylibrary'))
      from _mymodules import matrix_check_sym
      
      def matrix_cholesky_fac(matrix):
          if (not matrix_check_sym(matrix)):
              return False
          width = len(matrix)
          L_matrix = [[0 for i in range(width)] for j in range(width)]
          for k in range(0, width):
              for i in range(0, k):
                  temp_sum = matrix[k][i]
                  for j in range(0, i):
                      temp_sum -= L_matrix[i][j] * L_matrix[k][j]
                  L_matrix[k][i] = temp_sum/L_matrix[i][i]
      
              temp_sum = matrix[k][k]
              for j in range(0,k):
                  temp_sum -= pow(L_matrix[k][j],2)
              L_matrix[k][k] = pow(temp_sum,0.5)
      
          return L_matrix
