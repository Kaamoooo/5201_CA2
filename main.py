import time
from include import *

if __name__ == "__main__":

    #Set this to use either Trapezoidal Rule or Simpson's Rule
    USE_TRAPEZOIDAL_RULE = False

    if USE_TRAPEZOIDAL_RULE:
        from trapezoidal_rule import sequential_integrate, parallel_integrate
        print("Running Trapezoidal Rule")
    else:
        from simpson_rule import sequential_integrate, parallel_integrate
        print("Running Simpson's Rule")
        pass
    
    print("\nSequential execution through all test size")
    cumulative_time = 0
    for size in problem_sizes:
        start = time.time()
        res = sequential_integrate(target_function, a, b, size)
        end = time.time()
        sequential_time = end - start
        cumulative_time += sequential_time
        print(f"Size:  {size}\tTime: {sequential_time:.6f}\t Cumulative_time:{cumulative_time:.6f}\t Result: {res:.10f}")
    print(f"Cumulative time: {cumulative_time:.6f}")

    print("\nStability test for maximum size:")
    stability_cumulative_time = 0
    max_size = problem_sizes[-1]
    for i in range(5):
        start = time.time()
        res = sequential_integrate(target_function, a, b, max_size)
        end = time.time()
        sequential_time = end - start
        stability_cumulative_time += sequential_time
        print(f"Size:  {max_size}\tTime: {sequential_time:.6f}\t Cumulative_time:{stability_cumulative_time:.6f}\t Result: {res:.10f}")
    print(f"Cumulative time: {stability_cumulative_time:.6f}")
    
    print("\nParallel execution:")
    for processor_num in processor_nums:
        print(f"{processor_num} Processors:")
        parallel_cumulative_time = 0
        for size in problem_sizes:
            start = time.time()
            res = parallel_integrate(target_function, a, b, size, processor_num)
            end = time.time()
            sequential_time = end - start

            print(f"Size:  {size}\tTime: {sequential_time:.6f}\tResult: {res:.10f}")
            parallel_cumulative_time += sequential_time
        print(f"{processor_num} processors cumulative time: {parallel_cumulative_time:.6f}\n")
