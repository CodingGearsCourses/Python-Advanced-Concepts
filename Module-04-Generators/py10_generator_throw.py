# Copyright https://www.globaletraining.com/
# Generators throw method


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


pipeline = ending_in_1(squared(odd_filter(range(100000))))

for x in pipeline:
    if len(str(x)) >=5:
        pipeline.throw(ValueError("Too Long!"))
    print(x)

print(pipeline.__next__())




