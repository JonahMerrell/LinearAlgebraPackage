# Software Manual (gen_sym_matrix.py)

## [Back](softwaremanual.md)

**Routine Name:**           gen_sym_matrix.py

**Author:** Jonah Merrell

**Language:** Python 3.7.0

**Description/Purpose:** This routine will create a n*n symmetric square matrix. In order to make the matrix diagnaly dominant, random entries from 0 to 1 
 are generated everywhere in the matrix. Then, to make the matrix symmetric, n is added to the diagnal entries
 in the matrix.

**Input:** argument1: The width of the matrix

**Output:** This routine returns the n*n symmetric square matrix.

**Usage/Example:**

Below shows an example of generating a matrix using the routine "gen_sym_matrix". Then the matrix is printed 
one row at a time (for readability's sake). 

      A_ = gen_sym_matrix()
      for i in range(len(A_)):
          print(A_[i])


Output from the lines above:

      Please enter the width of the square matrix: 5
     [0.8025696089861225, 0.04089313746525569, 0.15669660790023143, 0.8902235581571983, 0.709520522161153]
     [0.04089313746525569, 0.533613729349306, 0.1503954651296724, 0.8042467620235467, 0.7426564088713985]
     [0.15669660790023143, 0.1503954651296724, 0.943134745475213, 0.3437436901975546, 0.5735670136611515]
     [0.8902235581571983, 0.8042467620235467, 0.3437436901975546, 0.609080003095936, 0.9638436143986736]
     [0.709520522161153, 0.7426564088713985, 0.5735670136611515, 0.9638436143986736, 0.3812056913192303]


In the example above, "5" was chosen to be the size of the matrix to be generated. The above matrix generated is just
 one possible matrix generated, since the content of the matrix is generated randomly.  Calling this function
 again would (likely) produce a matrix with different randomly generated numbers inside.

**Implementation/Code:** The following is the code for gen_sym_matrix()

      import random
      
      def gen_sym_matrix(width=5):
          A = [[0 for i in range(width)] for j in range(width)]
          for i in range(0, width):
              for j in range(i+1, width):
                  value = random.random()
                  A[j][i] = value
                  A[i][j] = value
          for i in range(0, width):
              A[i][i] = random.random()
          return A
