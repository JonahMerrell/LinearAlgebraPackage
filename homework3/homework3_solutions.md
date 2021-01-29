# Homework3<br>

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
For this task, we were asked to implement the newton iteration.

- Code:
  - [root_solve_newton.py](Task1/root_solve_newton.py)
- Software Manual entry:
  - [root_solve_newton](../software_manual/root_solve_newton.md)

### Task 2
For this task, we were asked to implement the secant iteration.

- Code:
  - [root_solve_secant.py](Task2/root_solve_secant.py)
- Software Manual entry:
  - [root_solve_secant](../software_manual/root_solve_secant.md)

### Task 3
For this task, we were asked to compare the 4 methods for root finding (functional iteration, bisection, Newton's method, and the secant method) <br>

I created a program that performs the 4 methods on the same equation: x cosh(x) + x<sup>3</sup> - pi = 0<br>

      The true root to the equation x * cosh(x)+ x^3 - pi is 1.0963278
      Using the fixed point iteration, the solution was N/A, which took N/A iterations.
      Using the bisection iteration, the solution was 1.0963282585144043, which took 22 iterations.
      Using the newton iteration, the solution was 1.0963277882922402, which took 4 iterations.
      Using the secant iteration, the solution was 1.096327788292231, which took 5 iterations.
	  
- Code:
  - [compare_root_methods_test.py](Task3/compare_root_methods_test.py)

  
### Task 4
For this task, we were asked to implement a hybrid method that uses the bisection iteration and newton's iteration.

- Code:
  - [root_solve_newton_hybrid.py](Task4/root_solve_newton_hybrid.py)
- Software Manual entry:
  - [root_solve_newton_hybrid](../software_manual/root_solve_newton_hybrid.md)

  
### Task 5
For this task, we were asked to implement a hybrid method that uses the bisection iteration and the secant iteration.

- Code:
  - [root_solve_secant_hybrid.py](Task5/root_solve_secant_hybrid.py)
- Software Manual entry:
  - [root_solve_secant_hybrid](../software_manual/root_solve_secant_hybrid.md)

### Task 6
For this task, we were asked to add the routines created thus far to your shared library.

The routines were added to my shared library.

[Shared Library](https://github.com/JonahMerrell/math4610/tree/master/mylibrary)

### Task 7
For this task, we were asked to develop code that will break an interval of a function into subintervals and apply the Bisection method to each subinterval.

- Code:
  - [root_solve_bisection_intervals.py](Task7/root_solve_bisection_intervals.py)
- Software Manual entry:
  - [root_solve_bisection_intervals](../software_manual/root_solve_bisection_intervals.md)

### Task 8
For this task, we were asked to repeat task 7 for Newton's method

- Code:
  - [root_solve_newton_intervals.py](Task8/root_solve_newton_intervals.py)
- Software Manual entry:
  - [root_solve_newton_intervals](../software_manual/root_solve_newton_intervals.md)

### Task 9
For this task, we were asked to repeat task 7 for the Secant method

- Code:
  - [root_solve_secant_intervals.py](Task9/root_solve_secant_intervals.py)
- Software Manual entry:
  - [root_solve_secant_intervals](../software_manual/root_solve_secant_intervals.md)


### Task 10
For this task, we were asked to search the internet for sites that identify real problems where some root finding problem is used to compute approximate solutions.

Root-finding numerical methods such as newtons method are used for solving systems of differential equations. This consequently means that root finding methods are used in many applications where systems of differential equaitons are used. Examples include modeling heat transfer in a material, modeling predator verses prey population relationships in an ecosystem, or modeling fluid flow.

[http://www.personal.psu.edu/sxt104/class/Math251/Notes-Predator-Prey.pdf](http://www.personal.psu.edu/sxt104/class/Math251/Notes-Predator-Prey.pdf)
[http://adsabs.harvard.edu/abs/1994IJNMF..19...41L](http://adsabs.harvard.edu/abs/1994IJNMF..19...41L)
[https://www.tandfonline.com/doi/abs/10.1080/10407790802182687?journalCode=unhb20](https://www.tandfonline.com/doi/abs/10.1080/10407790802182687?journalCode=unhb20)
 