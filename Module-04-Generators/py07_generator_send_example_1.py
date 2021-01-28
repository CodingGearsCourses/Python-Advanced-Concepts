# Copyright 2020 https://www.globaletraining.com/
# Generator send method


def simple_gen(number=10):
    for n in range(number):
        val = yield n * 2
        print("received", val)


gen1 = simple_gen()

print(gen1.__next__())
print(gen1.send(10))
print(gen1.__next__())
print(gen1.send(20))
print(gen1.__next__())
print(gen1.__next__())