# Homework8<br>

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
For this task, we were asked to implement the power method for finding the largest eigenvalue in magnitude of a square matrix.

- Code:
  - [matrix_power_iteration.py](Task1/matrix_power_iteration.py)
- Software Manual entry:
  - [matrix_power_iteration](../software_manual/matrix_power_iteration.md)

### Task 2
For this task, we were asked to try out our power method on the Hilbert matrix of order n = 10.

- Code:
  - [hilbert_matrix_power_iteration_test.py](Task2/hilbert_matrix_power_iteration_test.py)

After testing the power method on the 10x10 hilber matrix, the largest eigenvalue for 10x10 was found to be: 1.7519196702597382
  
### Task 3
For this task, we were asked to implement the inverse power method for finding the smallest eigenvalue of a square matrix.

- Code:
  - [matrix_inverse_power_iteration.py](Task3/matrix_inverse_power_iteration.py)
- Software Manual entry:
  - [matrix_inverse_power_iteration](../software_manual/matrix_inverse_power_iteration.md)

### Task 4
For this task, we were asked to try out our inverse power method on the Hilbert matrix of order n = 10.

- Code:
  - [hilbert_matrix_inverse_power_iteration_test.py](Task4/hilbert_matrix_inverse_power_iteration_test.py)

After testing the inverse power method on the 10x10 hilber matrix, the smallest eigenvalue for 10x10 was found to be: 1.0932741624186234e-13

### Task 5
For this task, we were asked to implement the power method with shifting to try to estimate eigenvalues of a matrix.

- Code:
  - [matrix_find_eigenvalues.py](Task5/matrix_find_eigenvalues.py)
- Software Manual entry:
  - [matrix_find_eigenvalues](../software_manual/matrix_find_eigenvalues.md)
  
### Task 6
For this task, we were asked to try out your shifted power method on the Hilbert matrix of order n = 10.

- Code:
  - [hilbert_matrix_find_eigenvalues_test.py](Task6/hilbert_matrix_find_eigenvalues_test.py)

After testing the shifted power method on the 10x10 hilber matrix, 8 of the 10 eigenvalues were found. They eigenvalues found were:<br>
[1.0932741624186234e-13, 1.7519196702649693, 0.34292954848351387, 0.03574181627165062, 0.0025308907686925376, 0.00012874961431114508, 0.34217589549639754, 1.7084449918328068]
  
### Task 7
For this task, we were asked to write a routine that will compute an estimate of the 2-condition number using the power method and inverse power method.

- Code:
  - [matrix_condition_number.py](Task7/matrix_condition_number.py)
- Software Manual entry:
  - [matrix_condition_number](../software_manual/matrix_condition_number.md)

### Task 8
For this task, we were asked to Try out the condition number code on the Hilber matrix for n = 10.

- Code:
  - [hilbert_matrix_condition_number_test.py](Task8/hilbert_matrix_condition_number_test.py)

The estimated condition number for the 10x10 hilbert matrix was computer to be 16024522763706.78.
  
### Task 9
For this task, we were asked to combine the tridiagonal matrix multiplication routine to compute the 2-condition number of a tridiagonal matrix.

Not complete

### Task 10
  
For this task, we were asked to search the internet for sites that document the use of Power iteration and/or Inverse Power Iteration. 

The power method and inverse power method are used to find the largest and smallest eigenvalues (and their corresponding eigenvectors) for a given matrix. These eigenvalues are useful because they can be used to approximate the condition number for a matrix. The inverse power method is extra useful because it can be shifted to converge to any eigenvalue, which makes it possible to find all the eigenvalues for a matrix. This method is especially useful for sparse matrices.

[http://math.ntnu.edu.tw/~min/matrix_computation/power_method.pdf](http://math.ntnu.edu.tw/~min/matrix_computation/power_method.pdf)
[http://www.netlib.org/utk/people/JackDongarra/etemplates/node96.html](http://www.netlib.org/utk/people/JackDongarra/etemplates/node96.html)
[https://www.sciencedirect.com/topics/mathematics/inverse-power-method](https://www.sciencedirect.com/topics/mathematics/inverse-power-method)

