# Copyright https://www.globaletraining.com/
# List comprehensions provide a concise way to create lists.

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def main():
    final_list = []
    for n in my_list:
        final_list.append(n + 10)

    print(final_list)

    # TODO: Using Comprehension
    final_list_comp1 = [n + 10 for n in my_list]
    print(final_list_comp1)

    # TODO: Using Comprehension & condition
    final_list_comp2 = [n + 10 for n in my_list if n % 2 == 0]
    print(final_list_comp2)


if __name__ == '__main__':
    main()