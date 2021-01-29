# multiproc_test.py

import random
import multiprocessing

import time
start_time = time.time()

def list_append(count, id, out_list):
	for i in range(count):
		out_list.append(random.random())

if __name__ == "__main__":
	size = 1000000   # Number of random numbers to add
	procs = 1   # Number of processes to create

	# Create a list of jobs and then iterate through
	# the number of processes appending each process to
	# the job list
	jobs = []
	for i in range(0, procs):
		out_list = list()
		#process = multiprocessing.Process(target=list_append,
		#	                              args=(size, i, out_list))
		#jobs.append(process)
		list_append(size, i, out_list)
	# Start the processes (i.e. calculate the random number lists)
	#for j in jobs:
	#	j.start()

	# Ensure all of the processes have finished
	#for j in jobs:
	#	j.join()

	print("List processing complete " + str((time.time() - start_time)))



