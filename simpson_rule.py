from multiprocessing import Pool

#Simpson's Rule. Li Yuyang A0318062L
def sequential_integrate(f, a, b, n):
    h = (b - a) / n
    res = f(a) + f(b)
    for i in range(1, n):
        x_i = a + i * h
        if i % 2 == 1:
            res += 4 * f(x_i)
        else:
            res += 2 * f(x_i)
    res *= h / 3
    return res

def parallel_integrate(f, a, b, n, num_processors):
    segment_size = (b - a) / num_processors
    base_n = n // num_processors
    tasks = []
    for i in range(num_processors):
        sub_a = a + i * segment_size
        sub_b = a + (i + 1) * segment_size
        tasks.append((f, sub_a, sub_b, base_n))
    with Pool(num_processors) as pool:
        results = pool.starmap(sequential_integrate, tasks)
    return sum(results)