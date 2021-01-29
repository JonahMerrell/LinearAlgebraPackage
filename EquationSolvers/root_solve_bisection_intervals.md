# Software Manual (root_solve_bisection_intervals.py)

## [Back](softwaremanual.md)

**Routine Name:**           root_solve_bisection_intervals.py

**Author:** Jonah Merrell

**Language:** Python 3.7.0

**Description/Purpose:** This routine will apply the bisection method over multiple sub-intervals in a function to find multiple roots to the function.

**Input:** argument1: The function f(x) (which we assume is equal to 0 when x is the root) for the bisection iteration.<br>
		   argument2: The left bound for the iteration<br>
		   argument3: The right bound for the iteration<br>
           argument4: The number of segments/sub-regions to divide our chosen interval into.
		   argument5: The tolerance used to determine when to stop iterating. (A number like 0.00001)<br>
		   
**Output:** This routine returns a list containing all the found solutions to the equation f(x)=0, where f(x) is given in the input.

**Usage/Example:**

Below shows an example of solving the equation sin(pi*x^2 + 3.7) = 0 using the routine "root_solve_bisection_intervals".
 Then the solution is printed. 

      import math
	  def function(x):
          return math.sin(math.pi* (x ** 2) + 3.7)
      print(root_solve_bisection_intervals(function, 1.1, 68.3, 10000,0.00001))

Output from the lines above:

      [1.3499098437500021, 1.6799576562500051, 1.9550576562500075, 2.19596046875001, 2.412936406250011, ...... many more roots

In the example above, The numbers in the list above are all of the found roots for the function math.sin(math.pi* (x ** 2) + 3.7) in the region 1.1 - 68.3

**Implementation/Code:** The following is the code for root_solve_bisection_intervals()
      
      import sys, os
      sys.path.append(os.path.abspath('../../mylibrary'))
      from _mymodules import root_solve_bisection
      
      def root_solve_bisection_intervals(function, a, b, divisions, tol):
          solutions = []
          step_size = (b-a)/divisions
          i=a
          while i < b:
              solution = root_solve_bisection(function, i, i+step_size, tol)
              if (solution != None):
                  solutions.append(solution)
              i += step_size
          return solutions
