# Software Manual (matrix_solve_LU_scaled_partial_pivoting.py)

## [Back](softwaremanual.md)

**Routine Name:**           matrix_solve_LU_scaled_partial_pivoting.py

**Author:** Jonah Merrell

**Language:** Python 3.7.0

**Description/Purpose:** This routine will compute the solution of a square linear system of equations. (The system is of the form Ax = b)
The solution is calculated by performing LU factorization with scaled partial pivoting (changing the system of equations to LUx = B), followed with forward substitution and back substitution.

**Input:** argument1: The matrix "A" in the system of linear equations Ax = b<br>
		   argument2: The vector "b" in the system of linear equations Ax = b

**Output:** This routine returns the solution vector "x" to the system of linear equations.

**Usage/Example:**

Below shows an example of solving a system of linear equations of the form "Ax = b" using the routine "matrix_solve_LU_scaled_partial_pivoting".
 Then the solution vector is printed. 

      matrix_example = [[1,1,-1],[1,-2,3],[2,3,1]]
      vector_example = [4,-6,7]
      print(matrix_solve_LU_scaled_partial_pivoting(matrix_example,vector_example))

Output from the lines above:

      [1.0, 2.0, -1.0]

In the example above, the matrix representing "A" in the system "Ax = b" had a width of "3". The output vector "x"
 is the solution vector to the system, so that Ax = b.

**Implementation/Code:** The following is the code for matrix_solve_LU_scaled_partial_pivoting()
      
      import sys, os
      sys.path.append(os.path.abspath('../../mylibrary'))
      from _mymodules import matrix_solve_upper_tri, matrix_solve_lower_tri,matrix_LU_factor_scaled_partial_pivoting
      
      def matrix_solve_LU_scaled_partial_pivoting(matrix,vector):
          n=len(matrix)
          LU = matrix_LU_factor_scaled_partial_pivoting(matrix)
          U = [[(LU[i][j] if (i<=j) else 0.0) for j in range(n)] for i in range(n)]
          L = [[(LU[i][j] if (i>j) else (1.0 if (i == j) else 0.0)) for j in range(n)] for i in range(n)]
      
          solution_y = matrix_solve_lower_tri(L,vector)
          solution_x = matrix_solve_upper_tri(U,solution_y)
          return solution_x
