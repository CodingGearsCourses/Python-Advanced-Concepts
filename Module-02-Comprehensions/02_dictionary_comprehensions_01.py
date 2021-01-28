# Copyright https://www.globaletraining.com/
# Dictionary comprehensions provide a concise way to create dictionaries.


def main():
    my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Creating a dictionary with key as the number and value as the squared of the number
    my_num_dict = {}
    for n in my_numbers:
        my_num_dict[n] = n ** 2
    print(my_num_dict)

    # TODO: Using Comprehension
    my_num_dict_comp1 = {n: n ** 2 for n in my_numbers}
    print(my_num_dict_comp1)

    # TODO: Using Comprehension & condition
    my_num_dict_comp2 = {n: n ** 2 for n in my_numbers if n % 2 == 0}
    my_num_dict_comp3 = {n: n ** 2 for n in my_numbers if 3 < n < 9}
    my_num_dict_comp4 = {n: n ** 2 for n in my_numbers if n % 2 == 0 if 3 < n < 9}
    print(my_num_dict_comp2)
    print(my_num_dict_comp3)
    print(my_num_dict_comp4)


if __name__ == '__main__':
    main()
