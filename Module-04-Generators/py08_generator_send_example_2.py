# Copyright 2020 https://www.globaletraining.com/
# Generator send method


def simple_gen(number=10):
    for n in range(number):
        val = (yield number * 2)
        print("received", val)
        if val:
            number += val
        else:
            number += 1


gen1 = simple_gen()

print(gen1.__next__())
print(gen1.send(100))
print(gen1.__next__())
print(gen1.send(200))
print(gen1.__next__())
print(gen1.__next__())
print(gen1.__next__())
print(gen1.__next__())
print(gen1.__next__())
print(gen1.__next__())
# print(gen1.__next__())  # Error