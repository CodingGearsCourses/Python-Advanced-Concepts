# Copyright 2020 https://www.globaletraining.com/
# Generators


# Function
def my_numbers_squared(n):
    result = []
    for x1 in range(n):
        result.append(x1 ** 2)
    return result


# Generator
def my_numbers_squared_gen(m):
    for x2 in range(m):
        yield x2 * x2


# print(my_numbers_squared(5))
# print(list(my_numbers_squared_gen(5)))

gen1 = my_numbers_squared_gen(5)
print(gen1.__next__())
print(next(gen1))
print(next(gen1))

print("------")
for z in gen1:
    print(z)


