from multiprocessing import Pool

# Trapezoidal Rule. Yang Chen A0318687L
def sequential_integrate(f, a, b, n):
    h = (b - a) / n
    # (y0 + y1) * h / 2 + (y1 + y2) * h / 2 + ... + (yn-2 + yn-1) * h / 2
    res = 0
    for i in range(n - 1):
        res += f(a + i * h) + f(a + (i + 1) * h)
    res *= h / 2
    return res


def parallel_integrate(f, a, b, n, num_processors):
    segment_size = (b - a) / num_processors
    tasks = [(f, a + i * segment_size, a + (i + 1) * segment_size, n // num_processors) for i in range(num_processors)]
    with Pool(num_processors) as pool:
        results = pool.starmap(sequential_integrate, tasks)
    return sum(results)
