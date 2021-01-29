# Software Manual (root_solve_secant_hybrid.py)

## [Back](softwaremanual.md)

**Routine Name:**           root_solve_secant_hybrid.py

**Author:** Jonah Merrell

**Language:** Python 3.7.0

**Description/Purpose:** This routine will implement the fixed point iteration.

**Input:** argument1: The function f(x) (which we assume is equal to 0 when x is the root) for newton's iteration.<br>
		   argument2: The left bound for the iteration<br>
		   argument3: The right bound for the iteration<br>
		   argument4: The tolerance used to determine when to stop iterating. (A number like 0.00001)<br>
		   argument5: The maximum iterations allowed while iterating.<br>
		   
**Output:** This routine returns the solution x to the equation f(x)=0, where f(x) is given in the input.

**Usage/Example:**

Below shows an example of solving the equation x * math.cosh(x) + pow(x, 3) - math.pi = 0 using the routine "root_solve_secant_hybrid".
 Then the solution is printed. 

      import math
	  def function(x):
          return x * math.cosh(x) + pow(x, 3) - math.pi
      print(root_solve_secant_hybrid(function, 0, 2, 0.000001,20))

Output from the lines above:

      1.0963277882922426

In the example above, 1.0963277882922426 is the approximation for the solution to the equation x * math.cosh(x) + pow(x, 3) - math.pi = 0

**Implementation/Code:** The following is the code for root_solve_secant_hybrid()
      
      import sys, os
      sys.path.append(os.path.abspath('../../mylibrary'))
      from _mymodules import root_solve_bisection, root_solve_newton
      
	  def root_solve_secant_hybrid(function, a, b, tol,maxiter):
	      c = root_solve_bisection(function, a, b, tol, 4)
	  
	      #Find another point close to c, appropriate to the scale of a and b
	      if abs(c-a) < abs(c-b) :#If c is closer to a
	          d = c + ((b-a)/10.0)
	      else:
	          d = c - ((b-a) / 10.0)
	      solution = root_solve_secant(function, c, d, tol, maxiter)
	      return solution
