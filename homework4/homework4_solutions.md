# Homework4<br>

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
For this task, we were asked to determine if there might be an advantage to using one of the hybrid methods (developed in the previous tasksheet) for root finding.<br>

In order to compare bisection method, newton's method, and the bisection method, I ran each of their multiple-root finding versions on the same equation and with the the same tolerance. I then compared the execution time of each of them. The results are shown below:

|   Root-finding Algorithm           |    Execution Time    |
|   root_solve_bisection_intervals   |  0.1910111904144287  |
|   root_solve_newton_intervals      |  0.1160066127777099  |
|   root_solve_secant_intervals      |  0.128007173538208   |

We can see from the results above that Newton's method performed the fastest compared to the other 2 methods. The secant method, although slower, didnt perform that much slower than Newton's method. (Probably because the 2 methods are very similar). Had the worst performance, meaning that the bisection method converges slower than Newton's method or the secant method.

### Task 2
For this task, we were asked to develop code to compute the length of a vector of arbitrary length using the 1-norm, 2-norm, and infinity norm. 

- Code:
  - [vector_1norm.py](Task2/vector_1norm.py)
  - [vector_2norm.py](Task2/vector_2norm.py)
  - [vector_infnorm.py](Task2/vector_infnorm.py)
- Software Manual entry:
  - [vector_1norm](../software_manual/vector_1norm.md)
  - [vector_2norm](../software_manual/vector_2norm.md)
  - [vector_infnorm](../software_manual/vector_infnorm.md)

### Task 3
For this task, we were asked to develop codes that compute the absolute and relative error in using one vector x as an approximation of another vector, x*. Create these routines for the 1-norm, 2-norm, and infinity norm. 

- Code:
  - [abs_error_1norm.py](Task3/abs_error_1norm.py)
  - [abs_error_2norm.py](Task3/abs_error_2norm.py)
  - [abs_error_infnorm.py](Task3/abs_error_infnorm.py)
- Software Manual entry:
  - [abs_error_1norm](../software_manual/abs_error_1norm.md)
  - [abs_error_2norm](../software_manual/abs_error_2norm.md)
  - [abs_error_infnorm](../software_manual/abs_error_infnorm.md)

### Task 4
For this task, we were asked to write codes that return (1) the sum of two vectore, (2) difference of two vectors, and (3) a scalar multiple of a vector.

- Code:
  - [vector_add.py](Task4/vector_add.py)
  - [vector_scal_mult.py](Task4/vector_scal_mult.py)
  - [vector_sub.py](Task4/vector_sub.py)
- Software Manual entry:
  - [vector_add](../software_manual/vector_add.md)
  - [vector_scal_mult](../software_manual/vector_scal_mult.md)
  - [vector_sub](../software_manual/vector_sub.md)

### Task 5
For this task, we were asked to write a code that implements a "SAXPY" operation involing input of a couple of vectors and a scalar.

- Code:
  - [vector_SAXPY.py](Task5/vector_SAXPY.py)
- Software Manual entry:
  - [vector_SAXPY](../software_manual/vector_SAXPY.md)

### Task 6
For this task, we were asked to write codes to implement (1) the dot product of two vectors and (2) the cross product of two vectors.

- Code:
  - [vector_cross.py](Task6/vector_cross.py)
  - [vector_dot.py](Task6/vector_dot.py)
- Software Manual entry:
  - [vector_cross](../software_manual/vector_cross.md)
  - [vector_dot](../software_manual/vector_dot.md)

### Task 7
For this task, we were asked to create a routine that will return the output from multiplying a matrix into a vector from the left (Of the form y = Ax).

- Code:
  - [matrix_vec_mult.py](Task7/matrix_vec_mult.py)
- Software Manual entry:
  - [matrix_vec_mult](../software_manual/matrix_vec_mult.md)

### Task 8
For this task, we were asked to download and use the "Hello World" handout that uses OpenMP to do a single print of a string for each processor our computer has, and then report how many processors our computer has.<br>

I was not succesful in being able to download a C compiler onto my computer, and thus was unable to compile or run the "Hello World" code. However, I was able to look onto my processor information in the task manager and determine that my computer has 4 processors.

### Task 9

For this task, we were asked to use OpenMP to try to speed up the matrix-vector multiplication (from task 7) using more than one processor.

I made an attempt to speed up the matrix-vector multiplication using multiple processors, but even though I used multiple processors, the execution time ended up a lot slower.

- Code:
  - [matrix_vec_mult_normal.py](Task9/matrix_vec_mult_normal.py)
  - [matrix_vec_mult_threading.py](Task9/matrix_vec_mult_threading.py)

### Task 10
  
For this task, we were asked search the internet for sites that document optimization flags on compilers that you might use. <br>

Optimization flags on compilers enable the compiler to attempt to improve the performance of a program by taking advantage of the computers multiple processors. This performance boost usually comes at the expense of compilation time. By default, the compiler will not attempt to utilize multiple processors, and so these “optimiation flags” must be turned on in order for the compiler to use them. In C, the gcc compiler’s optimization flags can be turned on with the –o0, -o1, -o2, -o3 options.

[https://gcc.gnu.org/onlinedocs/gcc/Optimize-Options.html](https://gcc.gnu.org/onlinedocs/gcc/Optimize-Options.html)<br>
[https://developers.redhat.com/blog/2018/03/21/compiler-and-linker-flags-gcc/](https://developers.redhat.com/blog/2018/03/21/compiler-and-linker-flags-gcc/)<br>

