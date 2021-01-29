# Software Manual (root_solve_fixed_point.py)

## [Back](softwaremanual.md)

**Routine Name:**           root_solve_fixed_point.py

**Author:** Jonah Merrell

**Language:** Python 3.7.0

**Description/Purpose:** This routine will implement the fixed point iteration.

**Input:** argument1: The function f(x) (which we assume is equal to 0 when x is the root) for the fixed point iteration.<br>
		   argument2: The initial guess x_0 to start of teh iteration<br>
           argument3: The tolerance used to determine when to stop iterating. (A number like 0.00001)<br>
		   argument4: The maximum iterations allowed while iterating.<br>
		   
**Output:** This routine returns the solution x to the equation f(x)=0, where f(x) is given in the input.

**Usage/Example:**

Below shows an example of solving the equation math.cos(x) - x = 0 using the routine "root_solve_fixed_point".
 Then the solution is printed. 

      import math
	  def function(x):
          return math.cos(x) - x
      print(root_solve_fixed_point(function, 0.9, 0.0001, 50))

Output from the lines above:

      0.7391130048798942

In the example above, 0.7391130048798942 is the approximation for the solution to the equation math.cos(x) - x = 0

**Implementation/Code:** The following is the code for root_solve_fixed_point()
      
      def root_solve_fixed_point(function, x_0, tol, maxiter):
      
          error = 10* tol
          x = x_0
          iter = 0
          while (error > tol and iter < maxiter):
              x = x + function(x)
              error = abs(x - x_0)
              x_0 = x
              iter +=1
          return x
