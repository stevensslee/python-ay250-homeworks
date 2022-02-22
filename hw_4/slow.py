from time import sleep, time
from random import uniform
from math import sqrt
from time import time
import numpy as np


from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
e = ProcessPoolExecutor() 

def slowfunc(x):

    number_of_darts = x
    number_of_darts_in_circle = 0
#     start_time = time()
    for n in range(int(number_of_darts)):
        x, y = uniform(0,1), uniform(0,1)
        if sqrt((x-0.5)**2 +(y-0.5)**2) <= 0.5:
            number_of_darts_in_circle +=1
#     end_time = time()
#     execution_time = end_time - start_time
#     pi_approx = 4*number_of_darts_in_circle/float(number_of_darts)

    return number_of_darts_in_circle

if __name__ == "__main__":
    thread_pool_results = []
    num_darts =[1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7, 1e8]
    for num_dart in num_darts:
        s = time()
        results = list(e.map(slowfunc, [num_dart/e._max_workers]*e._max_workers))

        print(f"Finished in {time() - s:0.3f} sec")
        end_time = time()
        execution_time = end_time-s
        print("Pi Approximation:", 4*np.sum(results)/num_dart)
        print("Number of Darts:", np.sum(results))
        print("Execution Time (s):", execution_time)
        print("Darts Thrown per Second:", num_dart/execution_time)

#         print(results)
#         print(np.sum(results)/num_dart)
        thread_pool_results.append((4*np.sum(results)/num_dart, np.sum(results), execution_time, np.sum(results)/execution_time))
    e.shutdown()
    np.save('thread_pool_results.npy', thread_pool_results)
