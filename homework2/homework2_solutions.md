# Homework2<br>

## [Back](../)

- [x] [Task 1](#task-1)
- [x] [Task 2](#task-2)
- [x] [Task 3](#task-3)
- [x] [Task 4](#task-4)
- [x] [Task 5](#task-5)
- [x] [Task 6](#task-6)
- [x] [Task 7](#task-7)
- [x] [Task 8](#task-8)
- [x] [Task 9](#task-9)
- [x] [Task 10](#task-10)

### Task 1
For this task, we were asked to set up a root finding problem for the equation: x cosh(x) + x<sup>3</sup> = pi

__Solution__:

Given x cosh(x) + x<sup>3</sup> = pi <br>
	  x cosh(x) + x<sup>3</sup> - pi = 0 <br>
		Let f(x) = xcosh(x) + x<sup>3</sup> - pi<br>
		Another possible root-finding problem could be: <br>
		Let f(x) = (pi - x<sup>3</sup>) / cosh(x) - x <br>
Thus, the root finding problem is to find x such that f(x) = 0 <br>

### Task 2
For this task, we were asked to set up at least two associated fixed point iteration for the equation: x cosh(x) + x<sup>3</sup> = pi

__Fixed-point Iteration__

x = x + f(x) <br>
x<sub>1</sub> = x<sub>0</sub> + f(x), given an intital guess x<sub>0</sub> <br>
Let g(x<sub>k</sub>) = x<sub>k</sub> + f(x<sub>k</sub>) <br>
x<sub>k + 1</sub> = g(x<sub>k</sub>) <br>

Thus, two fixed point iterations could be: <br>
x<sub>k + 1</sub> = x + xcosh(x) + x<sup>3</sup> - pi <br>
x<sub>k + 1</sub> = (pi - x<sup>3</sup>) / cosh(x) <br>


### Task 3
For this task, we were asked to implement the fixed point iteration.

- Code:
  - [root_solve_fixed_point.py](Task3/root_solve_fixed_point.py)
- Software Manual entry:
  - [root_solve_fixed_point](../software_manual/root_solve_fixed_point.md)
  
### Task 4
For this task, we were asked to implement the bisection iteration.

- Code:
  - [root_solve_bisection.py](Task4/root_solve_bisection.py)
- Software Manual entry:
  - [root_solve_bisection](../software_manual/root_solve_bisection.md)
  
### Task 5
For this task, we were asked to start our software manual for our machine precision methods.

- Link to my Software Manual: [https://jonahmerrell.github.io/math4610/software_manual/softwaremanual](https://jonahmerrell.github.io/math4610/software_manual/softwaremanual)
  
### Task 6
For this task, we were asked to start our software manual for our absolute and relative error methods.

- Link to my Software Manual: [https://jonahmerrell.github.io/math4610/software_manual/softwaremanual](https://jonahmerrell.github.io/math4610/software_manual/softwaremanual)

### Task 7
For this task, we were asked to start our software manual for our fixed point iteration root-finding method.

- Link to my Software Manual: [https://jonahmerrell.github.io/math4610/software_manual/softwaremanual](https://jonahmerrell.github.io/math4610/software_manual/softwaremanual)

### Task 8
For this task, we were asked to start our software manual for our bisection root-finding method.

- Link to my Software Manual: [https://jonahmerrell.github.io/math4610/software_manual/softwaremanual](https://jonahmerrell.github.io/math4610/software_manual/softwaremanual)

### Task 9
For this task, we were asked to compare the results of the functional iteration and Bisection iteration on the problem x cosh(x) + x<sup>3</sup> = pi <br>

I created a program that performs root_solve_bisection and root_solve_fixed_point on the same equation: x cosh(x) + x<sup>3</sup> = pi <br>

      Attempting to solve equation with root_solve_fixed_point:
      An OverflowError occured
      
      Attempting to solve equation with root_solve_bisection:
      1.096343994140625

The root_solve_fixed_point iteration produced an overflow error and was unable to find the root of the equation. However, the bisection iteration was able to quickly find the root, and is as accurate as the method call specified. After further investigation with the root_solve_fixed_point method, I was able to prevent an OverflowError from occuring (by multiplying the equation by 1/1000), but the method still did not converge to the actual root. 

- Code:
  - [compare_functional_iteration_with_bisection.py](Task9/compare_functional_iteration_with_bisection.py)

### Task 10
For this task, we were asked to search the internet for sites that discuss functional iteration for root finding.

Functional iterations are able to find a root of an equation by setting up a function that, when iterated, will converge to the solution (root) of the equation. To generate this root-finding function (normaly called g(x)), we simply need to modify an equation f(x) = 0 into the form g(x)= x. Functional iterations will only converge if abs(g'(x)) < 1.

[https://bookdown.org/rdpeng/advstatcomp/functional-iteration.html](https://bookdown.org/rdpeng/advstatcomp/functional-iteration.html) <br>
[http://home.iitk.ac.in/~psraj/mth101/lecture_notes/lecture8.pdf](http://home.iitk.ac.in/~psraj/mth101/lecture_notes/lecture8.pdf) <br>
[https://mat.iitm.ac.in/home/sryedida/public_html/caimna/transcendental/iteration%20methods/fixed-point/iteration.html](https://mat.iitm.ac.in/home/sryedida/public_html/caimna/transcendental/iteration%20methods/fixed-point/iteration.html) <br>
[https://www3.nd.edu/~zxu2/acms40390F12/Lec-2.2.pdf](https://www3.nd.edu/~zxu2/acms40390F12/Lec-2.2.pdf) <br>






