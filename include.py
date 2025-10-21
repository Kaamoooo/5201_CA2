import numpy as np

problem_sizes = [10000,50000,100000,500000,1000000,5000000,10000000,20000000]
processor_nums = [1,2,4,8]

a = 0
b = 5

def target_function(x):
    return np.exp(-x) * np.sin(5 * x)