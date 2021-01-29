# Homework7<br>

## [Back](../)

- [x] [Task 1](#task-1)
- [x] [Task 2](#task-2)
- [x] [Task 3](#task-3)
- [x] [Task 4](#task-4)
- [x] [Task 5](#task-5)
- [x] [Task 6](#task-6)
- [x] [Task 7](#task-7)
- [x] [Task 8](#task-8)
- [ ] [Task 9](#task-9)
- [x] [Task 10](#task-10)

### Task 1
For this task, we were asked to implement the method of Steepest Descent for solving linear systems of equations.

- Code:
  - [matrix_cholesky_facmatrix_solve_steepest_descent.py](Task1/matrix_solve_steepest_descent.py)
- Software Manual entry:
  - [matrix_solve_steepest_descent](../software_manual/matrix_solve_steepest_descent.md)

### Task 2
For this task, we were asked to tryout our steepest descent method on a sequence of matrices based on the Hilbert matrix.

To test the steepest descent method, I multiplied Ax to get b, with x being a vector of 1s (and A as the hilbert matrix). Using this value for b, I solved the system Ax=b using the steepest descent method for various sizes of matrices.

I was suprised to see that the steepest descent method was able to maintain a reasonable accuracy for hilbert matrices as large as 128*128. 

The results are shown below:

Absolute error for 4x4: 0.025503769943724174<br>
Absolute error for 8x8: 0.05967782703661602<br>
Absolute error for 16x16: 0.06989105656070722<br>
Absolute error for 32x32: 0.07431655921793938<br>
Absolute error for 64x64: 0.1136873213128524<br>
Absolute error for 128x128: 0.1353195615455678<br>


- Code:
  - [hilbert_matrix_steepest_descent_test.py](Task2/hilbert_matrix_steepest_descent_test.py)

### Task 3
For this task, we were asked to implement the Conjugate Gradient method for solving linear systems of equations.

- Code:
  - [matrix_solve_conjugate_gradient.py](Task3/matrix_solve_conjugate_gradient.py)
- Software Manual entry:
  - [matrix_solve_conjugate_gradient](../software_manual/matrix_solve_conjugate_gradient.md)

### Task 4
For this task, we were asked to test the steepest descent method and conjugate gradient method. To do this, a square symmetric diagonally dominant matrix was generated, and then the number of iterations required to produce a solution to the linear system was reported.

The results from the test are shown below:

Steepest Descent 100x100:   Absolute Error=1.4160319069471702e-07  Iteration Count=11<br>
Conjugate Gradient 100x100: Absolute Error=3.124948204702947e-07   Iteration Count=6<br>

We can see from this test that the conjugate gradiant method was able to solve the system of equations in less iterations than the steepest descent method.

- Code:
  - [steepest_descent_conjugate_gradient_compare.py](Task4/steepest_descent_conjugate_gradient_compare.py)

### Task 5
For this task, we were asked to compare our results in Task 4 to the use of Gaussian Elimination

The results from the test are shown below:

Steepest Descent 100x100:   Absolute Error=4.3170405239986345e-15  Iteration Count=21 time=0.07500410079956055<br>
Conjugate Gradient 100x100: Absolute Error=1.0243070691865838e-12  Iteration Count=11 time=0.02300119400024414<br>
Guass Elimination 100x100:  Absolute Error=8.70587598461163e-15                       time=0.15800929069519043<br>

We can see that Guess elimination took 2-4 times longer to solve the system to the same accuracy as the Conjugate Gradiant and Steepest descent methods. 

- Code:
  - [steepest_descent_conjugate_gradient_gauss_elimination_compare.py](Task5/steepest_descent_conjugate_gradient_gauss_elimination_compare.py)

### Task 6
For this task, we were asked to repeat the work in Task 5 but use Jacobi iteration instead of Gaussian elimination.

The results from the test are shown below:

Steepest Descent 100x100: Absolute Error=5.399155085589337e-15  Iteration Count=21 time=0.07000422477722168<br>
Conjugate Gradient 100x100: Absolute Error=1.093679044844119e-12  Iteration Count=11 time=0.021001100540161133<br>
Jacobian 100x100: Absolute Error=3.434090490215475e-14  Iteration Count=47 time=0.18301033973693848<br>

We can see that the jacobian iteration took 2-9 times longer to solve the system to the same accuracy as the Conjugate Gradiant and Steepest descent methods. 

- Code:
  - [steepest_descent_conjugate_gradient_jacobian_compare.py](Task6/steepest_descent_conjugate_gradient_jacobian_compare.py)

### Task 7
For this task, we were asked to repeat Task 6 using Gauss-Seidel instead of Jacobi Iteration.

The results from the test are shown below:

Steepest Descent 100x100: Absolute Error=4.669540497562317e-15  Iteration Count=21 time=0.07500433921813965<br>
Conjugate Gradient 100x100: Absolute Error=1.0547209362808094e-12  Iteration Count=11 time=0.021001338958740234<br>
Gauss Seidel 100x100: Absolute Error=5.850611998216189e-14  Iteration Count=15 time=0.05600285530090332<br>

We can see that the Gauss-Seidel method took was able to solve the system at about the same speed as the Conjugate Gradiant and Steepest descent methods. In fact, tge Gauss-Siedel method performed faster than the Steepest Descent method, but the GConjugate Gradient method was the fastest of them all.


- Code:
  - [steepest_descent_conjugate_gradient_gauss_seidel_compare.py](Task7/steepest_descent_conjugate_gradient_gauss_seidel_compare.py)

### Task 8
For this task, we were asked to implement a matrix multiplication routine for a tridiagonal matrix that avoids as many computations with zeros as possible.

- Code:
  - [matrix_solve_tridiagonal.py](Task8/matrix_solve_tridiagonal.py)
- Software Manual entry:
  - [matrix_solve_tridiagonal](../software_manual/matrix_solve_tridiagonal.md)

### Task 9
For this task, we were asked to create an analogous routine where the matrix is penta-diagonal with two diagonals above and below the main diagonal of the matrix.

Not complete

### Task 10
  
For this task, we were asked search the internet for sites that document the use of conjugate gradient methods.

The conjugate gradient method is a numerical method to iteratively solve a system of linear equations. It is particularly good at sparse systems, where other direct method would struggle. The Conjugate gradient method is much more efficient than other gradient-based methods, such as the steepest descent method. Unlike other iterative methods, the conjugate gradient method is guaranteed to converge after a finite amount of iterations. (Although due to machine precision, the method may take additional iterations to achieve a desired accuracy.

[https://en.wikipedia.org/wiki/Conjugate_gradient_method](https://en.wikipedia.org/wiki/Conjugate_gradient_method)
[https://www.sciencedirect.com/topics/engineering/conjugate-gradient-method](https://www.sciencedirect.com/topics/engineering/conjugate-gradient-method)
[https://optimization.mccormick.northwestern.edu/index.php/Conjugate_gradient_methods](https://optimization.mccormick.northwestern.edu/index.php/Conjugate_gradient_methods)

