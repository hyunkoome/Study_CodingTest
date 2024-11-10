import time
import numpy as np

if __name__ == "__main__":
    N = 1000

    # method 1
    nums = list(range(N))

    start_time = time.time()
    print("Using List")
    print(500 in nums)
    print(f"Elapsed Time: {time.time() - start_time: .10f} seconds")

    # method 2
    nums_set = set(nums)
    start_time = time.time()
    print("Using Set")
    print(500 in nums_set)
    print(f"Elapsed Time: {time.time() - start_time: .10f} seconds")

    # method 4
    dict_nums = {d: d for d in range(N)}
    start_time = time.time()
    print("Using Dict")
    print(500 in dict_nums)
    print(f"Elapsed Time: {time.time() - start_time: .10f} seconds")

    # method 3
    nums_array = np.array(nums)
    start_time = time.time()
    print("Using Numpy")
    print(np.isin(500, nums_array))
    print(f"Elapsed Time: {time.time() - start_time: .10f} seconds")







