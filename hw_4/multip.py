
import multiprocessing
from time import sleep, time
from random import uniform
from math import sqrt
from time import time
import os
import sys
import logging
import random
from slowfunc import slowfunc
from multiprocessing import Pool 

pool = Pool()     # start 4 worker processes 
        
if __name__ == "__main__":
    s = time()
    results = list(pool.map(slowfunc, [200000000/os.cpu_count()]*os.cpu_count()))
    print(f"Finished in {time() - s:0.3f} sec")
    print(results)
    
    pool.terminate()
