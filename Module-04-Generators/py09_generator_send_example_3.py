# Copyright 2020 https://www.globaletraining.com/
# Generator send method


def simple_gen(start_number=10):
    i = start_number
    while True:
        x = (yield i * 2)
        if x:         # check if used send()
            i += x
        else:
            i += 1


gen1 = simple_gen()

print(gen1.__next__())
print(gen1.send(10))
print(gen1.__next__())
print(gen1.send(20))
print(gen1.__next__())
print(gen1.__next__())
print(gen1.__next__())
print(gen1.__next__())
print(gen1.__next__())
print(gen1.__next__())
print(gen1.__next__())
print(gen1.__next__())
print(gen1.__next__())
print(gen1.__next__())
print(gen1.__next__())
print(gen1.__next__())
print(gen1.__next__())
print(gen1.send(20))
print(gen1.send(20))
print(gen1.__next__())
print(gen1.__next__())
print(gen1.__next__())