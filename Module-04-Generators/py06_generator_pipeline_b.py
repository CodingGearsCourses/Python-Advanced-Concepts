# Copyright 2020 https://www.globaletraining.com/
# Generator pipeline


def odd_filter(nums):
    for num in nums:
        if num % 2 == 1:
            yield num


def squared(nums):
    for num in nums:
        yield num ** 2


def ending_in_1(nums):
    for num in nums:
        if num % 10 == 1:
            yield num


def convert_to_string(nums):
    for num in nums:
        yield "Match Found --> " + str(num)


gen_pipeline = convert_to_string(ending_in_1(squared(odd_filter(range(1000)))))

for n in gen_pipeline:
    print(n)