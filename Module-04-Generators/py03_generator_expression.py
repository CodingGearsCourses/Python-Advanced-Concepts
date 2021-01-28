# Copyright 2020 https://www.globaletraining.com/
# Simple "for" loops can be written using generator expression


# Generator Function <<<
def my_numbers_squared_gen(n):
    for i in range(n):
        yield i ** 2


# Using Generator Function <<<
# numbers_squared = my_numbers_squared_gen(5)

# TODO: Generator Expression <<<
numbers_squared = (n ** 2 for n in range(5))

print(numbers_squared)
print(list(numbers_squared))
# Printing
# for num in numbers_squared:
#     print(num)
