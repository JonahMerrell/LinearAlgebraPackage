# Software Manual (root_solve_newton.py)

## [Back](softwaremanual.md)

**Routine Name:**           root_solve_newton.py

**Author:** Jonah Merrell

**Language:** Python 3.7.0

**Description/Purpose:** This routine will implement the fixed point iteration.

**Input:** argument1: The function f(x) (which we assume is equal to 0 when x is the root) for newton's iteration.<br>
		   argument2: The function f'(x) (the derivative of f(x))<br>
		   argument3: The initial quess to start the method<br>
           argument4: The tolerance used to determine when to stop iterating. (A number like 0.00001)<br>
		   argument5: The maximum iterations allowed while iterating.<br>
		   
**Output:** This routine returns the solution x to the equation f(x)=0, where f(x) is given in the input.

**Usage/Example:**

Below shows an example of solving the equation math.cos(x) - x = 0 using the routine "root_solve_newton".
 Then the solution is printed. 

      import math
	  def function(x):
          return math.cos(x) - x
      def function_prime(x):
          return -math.sin(x) - 1
      print(root_solve_newton(function, function_prime, 1, 0.000001,20))

Output from the lines above:

      0.7390851332151607

In the example above, 0.7390851332151607 is the approximation for the solution to the equation math.cos(x) - x = 0

**Implementation/Code:** The following is the code for root_solve_newton()
      
      def root_solve_newton(f, f_prime, x_0, tol, maxiter,getIterCount=False):
          if (f(x_0) == 0) :
              return x_0
          error = 10*tol
          iter = 0
          while(error > tol and iter < maxiter):
              iter += 1
              x_1 = x_0 - f(x_0)/f_prime(x_0)
              error = abs(x_1 - x_0)
              x_0 = x_1
      
          if getIterCount==False:
              return x_1
          else:
              return (x_1,iter)
