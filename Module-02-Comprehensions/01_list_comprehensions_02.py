# Copyright https://www.globaletraining.com/
# List comprehensions provide a concise way to create lists.


def main():
    my_numbers = [18, 32, 74, 34, 69, 2, 4, 52, 61, 32, 11, 5, 17, 95, 96, 18, 38, 35, 49, 89, 54, 44, 99, 29]
    my_numbers_double = []
    for n in my_numbers:
        my_numbers_double.append(n*2)
    print(my_numbers_double)

    # TODO: Using Comprehension
    my_numbers_double_comp1 = [n * 2 for n in my_numbers]
    print(my_numbers_double_comp1)

    # TODO: Using Comprehension & condition (evens)
    my_numbers_double_comp2 = [n * 2 for n in my_numbers if n % 2 == 0]
    print(my_numbers_double_comp2)

    # TODO: Using Comprehension & condition (range)
    my_numbers_double_comp3 = [n * 2 for n in my_numbers if n % 2 == 0 if n > 50]
    print(my_numbers_double_comp3)


if __name__ == '__main__':
    main()
