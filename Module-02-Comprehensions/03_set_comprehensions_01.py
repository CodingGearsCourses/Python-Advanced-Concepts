# Copyright https://www.globaletraining.com/
# Set comprehensions provide a concise way to create sets.


set_nums = {1, 5, 2, 4, 4, 5, 9, 10, 11, 5, 7, 12, 19, 2, 5, 6}
set_cities = {'Boston', 'Chicago', 'Houston', 'Denver', 'Boston', 'Houston', 'Denver', 'Miami'}
list_nums = [1, 4, 9, 5, 3, 4, 7, 8, 9, 2, 3, 4, 5, 6, 7, 5, 3, 9, 1, 5, 9, 4, 2, 8, 1, 3, 7, 8, 9, 4, 3, 2]


def main():
    set_list_nums = set()
    for n in list_nums:
        set_list_nums.add(n)
    print(type(set_list_nums))
    print(set_list_nums)

    # TODO: Using Comprehension
    set_list_nums_comp1 = {n for n in list_nums}
    print(type(set_list_nums_comp1))
    print(set_list_nums_comp1)

    # TODO: print set_cities
    print(set_cities)

if __name__ == '__main__':
    main()