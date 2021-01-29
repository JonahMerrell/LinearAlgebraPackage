# Homework6<br>

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
For this task, we were asked to write a code that implements a Cholesky factorization of a real matrix

- Code:
  - [matrix_cholesky_fac.py](Task1/matrix_cholesky_fac.py)
  - [matrix_check_sym.py](Task1/matrix_check_sym.py)
- Software Manual entry:
  - [matrix_cholesky_fac](../software_manual/matrix_cholesky_fac.md)

### Task 2
For this task, we were asked to write a method that implements Jacobi iteration for solving linear systems of equations.

- Code:
  - [matrix_solve_jacobian.py](Task2/matrix_solve_jacobian.py)
- Software Manual entry:
  - [matrix_solve_jacobian](../software_manual/matrix_solve_jacobian.md)

### Task 3
For this task, we were asked to write a routine that will create a random square matrix with dimension n.

- Code:
  - [gen_rand_matrix.py](Task3/gen_rand_matrix.py)
- Software Manual entry:
  - [gen_rand_matrix](../software_manual/gen_rand_matrix.md)

### Task 4
For this task, we were asked to write a routine that will create a random diagonally dominant matrix with dimension n.

- Code:
  - [gen_diagdom_matrix.py](Task4/gen_diagdom_matrix.py)
- Software Manual entry:
  - [gen_diagdom_matrix](../software_manual/gen_diagdom_matrix.md)

### Task 5
For this task, we were asked to write a routine that will create a random symetric matrix with dimension n.

- Code:
  - [gen_sym_matrix.py](Task5/gen_sym_matrix.py)
- Software Manual entry:
  - [gen_sym_matrix](../software_manual/gen_sym_matrix.md)

### Task 6
For this task, we were asked to write a routine that will create a random diagonally dominant symetric matrix with dimension n.

- Code:
  - [gen_diagdom_sym_matrix.py](Task6/gen_diagdom_sym_matrix.py)
- Software Manual entry:
  - [gen_diagdom_sym_matrix](../software_manual/gen_diagdom_sym_matrix.md)

### Task 7
For this task, we were asked to use each of the matrix generation routines with our Jacobi iteration to test the code.

|     Jacobian     |        Time       | # of iterations |    Result   |
|   rand_matrix    |3.9712271690368652 |       1000      |    Error    |
|    sym_matrix    |3.8992230892181396 |       1000      |    Error    |
|  diagdom_matrix  |0.11000633239746094|        27       | vector of 1s|
|diagdom_sym_matrix|0.11200642585754395|        27       | vector of 1s|

- Code:
  - [matrix_solve_jacobian_test.py](Task7/matrix_solve_jacobian_test.py)

### Task 8
For this task, we were asked to implement the Gauss-Seidel method for solving linear systems of equations.

- Code:
  - [matrix_solve_gauss_seidel.py](Task8/matrix_solve_gauss_seidel.py)
- Software Manual entry:
  - [matrix_solve_gauss_seidel](../software_manual/matrix_solve_gauss_seidel.md)

### Task 9
For this task, we were asked to run the Gauss-Seidel iteration on the same matrices as you created in Task 7. Compare the results of the Jacobi iteration runs to the Gauss-Seidel runs.

|   Gauss Seidel   |        Time        | # of iterations | vector of 1s|
|   rand_matrix    |0.0890049934387207  |       21        | vector of 1s|
|    sym_matrix    |0.07700467109680176 |       19        | vector of 1s|
|  diagdom_matrix  |0.0370020866394043  |       9         | vector of 1s|
|diagdom_sym_matrix|0.034001827239990234|       9         | vector of 1s|

By comparing the results of the Gauss-Seidel iteration with the Jacobian iteration, we can see that the Gauss Seidel converged to the desired accuracy much faster than the Jacobian iteration for every matrix we tested. Additionaly, we can see that the Guess-Seidel iteration converged with random matrices that the Jacobian iteration couldnt converge with.

- Code:
  - [matrix_solve_gauss_seidel_test.py](Task9/matrix_solve_gauss_seidel_test.py)

### Task 10
  
For this task, we were asked search the internet for sites that document the use of Jacobi iteration and/or Gauss-Seidel.

There are multiple ways to implement pivoting when solving systems of linear equations. Methods include no pivoting (when no pivoting is implemented), trivial pivoting (when row “i” is swapped with another arbitrary row when ai,i=0), and partial pivoting (when row “i” is swapped with another row “p” with the largest value for ap,i). There also exists “total pivoting”, which involves swapping rows and columns to achieve an ideal non-zero value for ai,i.

[http://mathfaculty.fullerton.edu/mathews/n2003/GaussSeidelMod.html](http://mathfaculty.fullerton.edu/mathews/n2003/GaussSeidelMod.html)<br>
[https://www3.nd.edu/~zxu2/acms40390F12/Lec-7.3.pdf](https://www3.nd.edu/~zxu2/acms40390F12/Lec-7.3.pdf)<br>

