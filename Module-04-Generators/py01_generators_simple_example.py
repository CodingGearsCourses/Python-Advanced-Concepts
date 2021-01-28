# Copyright 2020 https://www.globaletraining.com/
# Generators


def my_generator():
    yield 100
    yield 200
    yield 300
    yield 400


x = my_generator()
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())  # StopIteration

# for loop (Handles StopIteration Error)
# for i in gen:
#     print(i)
