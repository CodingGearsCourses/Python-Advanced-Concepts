# Copyright 2020 https://www.globaletraining.com/
# Generator Performance

import sys
from random import randint
from time import sleep, perf_counter


# Function that returns a list
def my_random_nums_squared_list(count, start_num, end_num):
    result = []
    for n in range(0, count):
        result.append(randint(start_num, end_num) ** 2)
    return result


# TODO: Generator Function
def my_random_nums_squared_gen(count, start_num, end_num):
    for n in range(0, count):
        yield randint(start_num, end_num) ** 2


# # Using list
# # -----------------------------------------------------
print(">>>>> Without Generator<<<<<")
t_start = perf_counter()
a1_list = my_random_nums_squared_list(20000000, 10, 100)
size = sys.getsizeof(a1_list) / (1024 * 1024)
t_end = perf_counter()
print("Size : ", round(size, 2), "MB")
duration = t_end - t_start
print("Duration : {} secs".format(round(duration, 8)))
print()

# Using Generator
# -----------------------------------------------------
print(">>>>> Using Generator Function <<<<<")
t_start = perf_counter()
a2_genobj = my_random_nums_squared_gen(20000000, 10, 100)
size = sys.getsizeof(a2_genobj) / (1024 * 1024)
t_end = perf_counter()
print("Size : ", round(size, 2), "MB")
duration = t_end - t_start
print("Duration : {} secs".format(round(duration, 8)))
print()