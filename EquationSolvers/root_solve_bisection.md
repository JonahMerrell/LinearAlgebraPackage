# Software Manual (root_solve_bisection.py)

## [Back](softwaremanual.md)

**Routine Name:**           root_solve_bisection.py

**Author:** Jonah Merrell

**Language:** Python 3.7.0

**Description/Purpose:** This routine will implement the bisection method.

**Input:** argument1: The function f(x) (which we assume is equal to 0 when x is the root) for the bisection iteration.<br>
		   argument2: The left bound for the iteration<br>
		   argument3: The right bound for the iteration<br>
           argument4: The tolerance used to determine when to stop iterating. (A number like 0.00001)<br>
		   
**Output:** This routine returns the solution x to the equation f(x)=0, where f(x) is given in the input.

**Usage/Example:**

Below shows an example of solving the equation math.cos(x) - x = 0 using the routine "root_solve_bisection".
 Then the solution is printed. 

      import math
	  def function(x):
          return math.cos(x) - x
      print(root_solve_bisection(function, 0, 1, 0.000001))

Output from the lines above:

      0.7390847206115723

In the example above, 0.7390847206115723 is the approximation for the solution to the equation math.cos(x) - x = 0

**Implementation/Code:** The following is the code for root_solve_bisection()
      
      def root_solve_bisection(function, a, b, tol):
          #Check to see if a or b are already the solution
          if (function(a) == 0) :
              return a
          if (function(b) == 0) :
              return b
          #Calculate the max iterations needed for this method
          maxiter = math.ceil(-math.log2(tol/(b-a)) + 1)
          val = function(a)*function(b)
          if (val >= 0):
              return "a and b are not valid for this iteration technique"
          c = 0
          for i in range(maxiter):
              c = 0.5 * (a + b)
              if (function(c) == 0):
                  return
              if (function(a)*function(c) < 0):
                  b = c
              else:
                  a = c
          return c
