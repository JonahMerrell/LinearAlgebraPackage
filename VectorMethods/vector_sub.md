# Software Manual (vector_sub.py)

## [Back](softwaremanual.md)

**Routine Name:**           vector_sub.py

**Author:** Jonah Merrell

**Language:** Python 3.7.0

**Description/Purpose:** This routine will subtract to vectors. More precisly speaking, this
 routine will subtract from the first given vector the values of the second given vector to produce a third vector, which
 we consider to be the "difference" of the 2 original vectors.

**Input:** argument1: The first vector<br>
		   argument2: The second vector to be subtracted from the first vector<br>
		   The 2 vectors given must have equal length.
		   
**Output:** This routine returns a vector that is obtained from the result of subtracting the
 corresponding componenents of the first vector from the second vector. 

**Usage/Example:**

Below shows an example of 2 different vectors with a length of 5 being subtracted using the routine
 "vector_sub". 

      vector1 = [5,7,9,2,5]
      vector2 = [8,2,3,6,9]
      print(vector_sub(vector1,vector2))

Output from the lines above:

      [-3, 5, 6, -4, -4]

The above vector printed is the difference of the previous 2 vectors provided. For example, consider the first
 element in the 2 vectors given as input, "5" and "8". Since 5 - 8 = -3, this explains why the first element
 in the new vector produced by "vector_sub" is "-3". This is how the other 4 elements in the new vector
 were produced.

**Implementation/Code:** The following is the code for vector_sub()


      def vector_sub(vector1,vector2):
          vector_sum = [0]* len(vector1)
          for i in range(len(vector_sum)):
              vector_sum[i] = vector1[i] - vector2[i]
      
          return vector_sum
