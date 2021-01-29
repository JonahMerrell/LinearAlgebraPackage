# Software Manual (gen_diagdom_matrix.py)

## [Back](softwaremanual.md)

**Routine Name:**           gen_diagdom_matrix.py

**Author:** Jonah Merrell

**Language:** Python 3.7.0

**Description/Purpose:** This routine will create a n*n diagnaly dominant square matrix. In order to make the matrix diagnaly dominant, random entries from 0 to 1 
 are generated everywhere in the matrix. Then, to make the matrix diagnally dominant, n is added to the diagnal entries
 in the matrix.

**Input:** argument1: The width of the matrix

**Output:** This routine returns the n*n diagnaly dominant square matrix.

**Usage/Example:**

Below shows an example of generating a matrix using the routine "gen_diagdom_matrix". Then the matrix is printed 
one row at a time (for readability's sake). 

      A_ = gen_diagdom_matrix()
      for i in range(len(A_)):
          print(A_[i])


Output from the lines above:

      Please enter the width of the square matrix: 5
     [5.328408621056993, 0.2177860478666146, 0.7759292529588636, 0.8584555106264391, 0.382275188133827]
     [0.5897965257560369, 5.048258830102817, 0.915157116609189, 0.8447713348440226, 0.6280832220280417]
     [0.20100448849447294, 0.5919927553465042, 5.178006349098188, 0.8541966617288655, 0.5787885578263041]
     [0.9102166340054162, 0.6850111967034856, 0.6808265230692657, 5.131705208782439, 0.6198436691478952]
     [0.3092794678133748, 0.5982743788065175, 0.8561656477762984, 0.36027718661187846, 5.580470294722382]


In the example above, "5" was chosen to be the width of the sqaure matrix.
 The above matrix generated is just one possible matrix generated, since the content of the matrix is generated randomly.
 Calling this function again would (likely) produce a matrix with different randomly generated numbers inside. You
  can observe that the entries on the diagnal of the matrix are larger (relativly speaking), because the matrix is
  diagnoly dominant.

**Implementation/Code:** The following is the code for gen_diagdom_matrix()

      import random
      
      def gen_diagdom_matrix(width=5):
          A = [[0 for i in range(width)] for j in range(width)]
          for i in range(0, width):
              for j in range(0, width):
                  value = random.random()
                  A[j][i] = value
      
          for i in range(0, width):
              A[i][i] += width
          return A
