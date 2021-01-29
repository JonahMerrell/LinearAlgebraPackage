# Software Manual (root_solve_newton_hybrid.py)

## [Back](softwaremanual.md)

**Routine Name:**           root_solve_newton_hybrid.py

**Author:** Jonah Merrell

**Language:** Python 3.7.0

**Description/Purpose:** This routine will implement the fixed point iteration.

**Input:** argument1: The function f(x) (which we assume is equal to 0 when x is the root) for newton's iteration.<br>
		   argument2: The function f'(x) (the derivative of f(x))<br>
		   argument3: The left bound for the iteration<br>
		   argument4: The right bound for the iteration<br>
		   argument5: The tolerance used to determine when to stop iterating. (A number like 0.00001)<br>
		   argument6: The maximum iterations allowed while iterating.<br>
		   
**Output:** This routine returns the solution x to the equation f(x)=0, where f(x) is given in the input.

**Usage/Example:**

Below shows an example of solving the equation x * math.cosh(x) + pow(x, 3) - math.pi = 0 using the routine "root_solve_newton_hybrid".
 Then the solution is printed. 

      import math
	  def function(x):
          return x * math.cosh(x) + pow(x, 3) - math.pi
      def function_prime(x):
          return math.cosh(x) + x * math.sinh(x) + 3 * pow(x, 2)
      print(root_solve_newton_hybrid(function, function_prime, 0, 2, 0.000001,20))

Output from the lines above:

      1.0963277882923448

In the example above, 1.0963277882923448 is the approximation for the solution to the equation x * math.cosh(x) + pow(x, 3) - math.pi = 0

**Implementation/Code:** The following is the code for root_solve_newton_hybrid()
      
      import sys, os
      sys.path.append(os.path.abspath('../../mylibrary'))
      from _mymodules import root_solve_bisection, root_solve_newton
      import math
      
      
      def root_solve_newton_hybrid(function, function_prime, a, b, tol,maxiter):
          c = root_solve_bisection(function, a, b, tol, 4)
          solution = root_solve_newton(function, function_prime, c, tol, maxiter)
          return solution
