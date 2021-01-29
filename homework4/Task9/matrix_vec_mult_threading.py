'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       October 29 2019
written for:        Homework4 Task6
course:             Math 4610

purpose:            Implement a method that returns the product of a matrices with a vector.
'''


import multiprocessing
import time
start_time = time.time()



def matrix_mult_part(count,row,iter_count,matrix1,vector2,return_list):
    #compute just one row of the matrix
    for i in range(count):
        sum = 0
        for k in range(iter_count):
            sum += matrix1[row][k] * vector2[k][0]

        return_list[row] = sum

def matrix_mult(matrix1,vector2):
    iter_count = len(matrix1[0]) # = len(vector2)
    height = len(matrix1)
    final_matrix = [[0] for j in range(height)]

    manager = multiprocessing.Manager()
    return_list = manager.list([0 for i in range(height)])


    jobs = []

    for i in range(0, height): #For each row in the matrix, create a job that computes the answer for that row

        process = multiprocessing.Process(target=matrix_mult_part,
                                      args=(10000,i,iter_count,matrix1,vector2,return_list))
        jobs.append(process)

    for j in jobs:
        j.start()

    for j in jobs:
        j.join()

    for i in range(len(return_list)):
        final_matrix[i][0] = return_list[i]

    return final_matrix


#The code below is used just for testing.
if __name__ == "__main__":
    vector1 = [[2,1,4],[0,1,1],[3,6,9]]
    vector2 = [[6],[1],[-2]]



    print(matrix_mult(vector1,vector2))
    print(str((time.time() - start_time)))