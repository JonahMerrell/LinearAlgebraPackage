# Software Manual (vector_SAXPY.py)

## [Back](softwaremanual.md)

**Routine Name:**           vector_SAXPY.py

**Author:** Jonah Merrell

**Language:** Python 3.7.0

**Description/Purpose:** This routine will multiply the first given vector by a scalar, and then add it to a second vector. More precisly speaking, this
 routine will compute scalar*vector1 + vector2.

**Input:** argument1: The scalar to be multiplied with the first vector<br>
           argument2: The first vector to be added<br>
		   argument3: The second vector to be added<br>
		   The 2 vectors given must have equal length.
		   
**Output:** This routine returns a vector that is obtained from the result of adding a scalar multiple of vector1 with vector2 .

**Usage/Example:**

Below shows an example of 2 different vectors with a length of 5 being added together using the routine
 "vector_SAXPY". 

      vector1 = [5,7,9,2,5]
      vector2 = [8,2,3,6,9]
      scalar = 6.0
      print(vector_SAXPY(scalar,vector1,vector2))

Output from the lines above:

      [38.0, 44.0, 57.0, 18.0, 39.0]

The above vector printed is the result of scalar*vector1 + vector2. 

**Implementation/Code:** The following is the code for vector_SAXPY()

      import sys, os
      sys.path.append(os.path.abspath('../../mylibrary'))
      from _mymodules import vector_add,vector_scal_mult
      
      def vector_SAXPY(scalar,vector1,vector2):
          return vector_add(vector_scal_mult(scalar,vector1),vector2)
