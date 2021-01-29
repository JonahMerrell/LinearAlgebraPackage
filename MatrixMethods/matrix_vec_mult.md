# Software Manual (matrix_vec_mult.py)

## [Back](softwaremanual.md)

**Routine Name:**           matrix_vec_mult.py

**Author:** Jonah Merrell

**Language:** Python 3.7.0

**Description/Purpose:** This routine will multipy a matrix by a vector. 

**Input:** argument1: The matrix to be multiplied <br>
		   argument2: The vector to be multiplied with the matrix <br>
		   
**Output:** This routine returns a vector that is obtained from the result of multiplying the given matric by the given vector.

**Usage/Example:**

Below shows an example of a 2x3 matrix being multiplied by a 3x1 vector using the routine
 "matrix_vec_mult". 

      matrix1 = [[2,1,4],[0,1,1]]
      vector2 = [[6],[1],[-2]]
      print(matrix_vec_mult(matrix1,vector2))

Output from the lines above:

      [[5], [-1]]

The above vector printed is the result of the computation Ax, where A is the given matrix and x is the given vector.

**Implementation/Code:** The following is the code for matrix_vec_mult()


      def matrix_vec_mult(matrix1,vector2):
          iter_count = len(matrix1[0]) # = len(vector2)
          height = len(matrix1)
          final_matrix = [[0] for j in range(height)]
      
      
          for j in range(height):
              sum = 0
              for k in range(iter_count):
                  sum += matrix1[j][k]*vector2[k][0]
              final_matrix[j][0] = sum
      
          return final_matrix


