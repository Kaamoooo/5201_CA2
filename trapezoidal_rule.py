from multiprocessing import Pool


# Trapezoidal Rule. Yang Chen A0318687L
def sequential_integrate(f, a, b, n):
    h = (b - a) / n
    # (y0 + y1) * h / 2 + (y1 + y2) * h / 2 + ... + (yn-1 + yn) * h / 2
    res = f(a) + f(b)
    for i in range(1, n - 1):
        res += 2 * f(a + i * h)
    res *= h / 2
    return res


def parallel_integrate(f, a, b, n, num_processors):
    segment_size = (b - a) / num_processors
    tasks = [(f, a + i * segment_size, a + (i + 1) * segment_size, n // num_processors) for i in range(num_processors)]
    with Pool(num_processors) as pool:
        results = pool.starmap(sequential_integrate, tasks)
    return sum(results)
