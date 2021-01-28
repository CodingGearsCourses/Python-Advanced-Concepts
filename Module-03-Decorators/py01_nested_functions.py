# Copyright 2020 https://www.globaletraining.com/
# Nested Functions


def my_outer_function(n):
    def my_inner_function1():
        print("Hello from inner function 1")

    def my_inner_function2():
        print("Hello from inner function 2")

    print("Hello from outer function")

    if n % 2 == 0:
        return my_inner_function2
    else:
        return my_inner_function1


x = my_outer_function(3)

x()
