# Homework5<br>

## [Back](../)

- [x] [Task 1](#task-1)
- [x] [Task 2](#task-2)
- [x] [Task 3](#task-3)
- [x] [Task 4](#task-4)
- [x] [Task 5](#task-5)
- [x] [Task 6](#task-6)
- [x] [Task 7](#task-7)
- [ ] [Task 8](#task-8)
- [x] [Task 9](#task-9)
- [x] [Task 10](#task-10)

### Task 1
For this task, we were asked to write a method/routine that will compute the solution of a square linear systems of equations where the coefficient matrix is diagonal.

- Code:
  - [matrix_solve_diagonal.py](Task1/matrix_solve_diagonal.py)
- Software Manual entry:
  - [matrix_solve_diagonal](../software_manual/matrix_solve_diagonal.md)

### Task 2
For this task, we were asked to write a method/routine that will compute the solution of an upper triangular system.

- Code:
  - [matrix_solve_upper_tri.py](Task2/matrix_solve_upper_tri.py)
- Software Manual entry:
  - [matrix_solve_upper_tri](../software_manual/matrix_solve_upper_tri.md)

### Task 3
For this task, we were asked to write a method/routine that will compute the solution of a lower triangular system.

- Code:
  - [matrix_solve_lower_tri.py](Task3/matrix_solve_lower_tri.py)
- Software Manual entry:
  - [matrix_solve_lower_tri](../software_manual/matrix_solve_lower_tri.md)

### Task 4
For this task, we were asked to write a routine that will row reduce a square matrix into row echelon form.

- Code:
  - [matrix_ref.py](Task4/matrix_ref.py)
- Software Manual entry:
  - [matrix_ref](../software_manual/matrix_ref.md)

### Task 5
For this task, we were asked to write a code that will solve a square linear system of equations using Gaussian elimination (elementary row operations).

- Code:
  - [matrix_solve.py](Task5/matrix_solve.py)
- Software Manual entry:
  - [matrix_solve](../software_manual/matrix_solve.md)

### Task 6
For this task, we were asked to write a routine that will compute the LU-factorization of a square matrix. 

- Code:
  - [matrix_LU_factor.py](Task6/matrix_LU_factor.py)
- Software Manual entry:
  - [matrix_LU_factor](../software_manual/matrix_LU_factor.md)

### Task 7
For this task, we were asked to create a routine that will solve a linear system of equations using the LU-factorization.

- Code:
  - [matrix_solve_LU.py](Task7/matrix_solve_LU.py)
- Software Manual entry:
  - [matrix_solve_LU](../software_manual/matrix_solve_LU.md)

### Task 8
For this task, we were see if we can speed up the LU-factorization solution method from the previous task using OpenMP

Not complete.

### Task 9
For this task, we were asked to embed scaled partial pivoting in a new version of the LU-factorization linear solution method, using more than one processor. Do this without interchanging rows - use an index vector to improve efficiency.
- Code:
  - [matrix_solve_LU_scaled_partial_pivoting.py](Task9/matrix_solve_LU_scaled_partial_pivoting.py)
  - [matrix_LU_factor_scaled_partial_pivoting.py](Task9/matrix_LU_factor_scaled_partial_pivoting.py)
- Software Manual entry:
  - [matrix_solve_LU_scaled_partial_pivoting](../software_manual/matrix_solve_LU_scaled_partial_pivoting.md)
  
### Task 10
  
For this task, we were asked search the internet for sites that document pivoting strategies in numerical solution of linear equations. <br>

There are multiple ways to implement pivoting when solving systems of linear equations. Methods include no pivoting (when no pivoting is implemented), trivial pivoting (when row “i” is swapped with another arbitrary row when ai,i=0), and partial pivoting (when row “i” is swapped with another row “p” with the largest value for ap,i). There also exists “total pivoting”, which involves swapping rows and columns to achieve an ideal non-zero value for ai,i.

[http://mathfaculty.fullerton.edu/mathews/n2003/PivotingMod.html](http://mathfaculty.fullerton.edu/mathews/n2003/PivotingMod.html)<br>
[http://ijear.org/vol4spl2/7-Ashu-Vij.pdf](http://ijear.org/vol4spl2/7-Ashu-Vij.pdf)<br>
[https://www.math.ust.hk/~mamu/courses/231/Slides/CH06_2A.pdf](https://www.math.ust.hk/~mamu/courses/231/Slides/CH06_2A.pdf)<br>