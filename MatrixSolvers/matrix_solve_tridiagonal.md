# Software Manual (matrix_solve_tridiagonal.py)

## [Back](softwaremanual.md)

**Routine Name:**           matrix_solve_tridiagonal.py

**Author:** Jonah Merrell

**Language:** Python 3.7.0

**Description/Purpose:** This routine will compute the solution of a tri-diagonal linear system of equations.
The solution is calculated by (elementary row operations), followed by backsubstitution to find the solution.

**Input:** argument1: The matrix "A" in the system of linear equations Ax = b. A is in a 3*n form, since A is a tridiagonal system.<br>
		   argument2: The vector "b" in the system of linear equations Ax = b

**Output:** This routine returns the solution vector "x" to the system of linear equations.

**Usage/Example:**

Below shows an example of solving a tri-diagonal system of linear equations of the form "Ax = b" using the routine "matrix_solve_tridiagonal".
 Then the solution vector is printed. 

      matrix = [[0,8,10],[5,2,5],[4,2,2],[3,6,0]]
      vector = [12,25,38,27]
      print(matrix_solve_tridiagonal(matrix,vector))

Output from the lines above:

      [-5.072164948453607, 5.257731958762886, 7.969072164948453, 0.5154639175257733]

In the example above, the matrix representing "A" in the system "Ax = b" had a width of "4". The output vector "x"
 is the solution vector to the system, so that Ax = b.

**Implementation/Code:** The following is the code for matrix_solve_tridiagonal()
      
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
