'''
import multiprocessing.dummy as mp
import multiprocessing
import queue

def helloWorldPrinting(threadNum):
    print("Hello from processor #" + str(threadNum) + "!")

if __name__ == "__main__":
    numThreads = multiprocessing.cpu_count()
    p = mp.Pool(numThreads)
    for i in range(numThreads):
        p.map(helloWorldPrinting, [i])
    p.end()
    '''

