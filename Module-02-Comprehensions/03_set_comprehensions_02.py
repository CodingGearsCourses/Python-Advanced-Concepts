# Copyright https://www.globaletraining.com/
# Set comprehensions provide a concise way to create sets.


jan_2020_austin_temp_f = [57, 61, 66, 71, 74, 75, 68, 71, 78, 78, 59, 63, 61, 76,
                          82, 70, 61, 69, 58, 61, 62, 59, 66, 67, 66, 77, 69, 73,
                          62, 50, 61]


def main():
    # Convert the temperature in fahrenheit to celsius and ignore duplicates
    # c = (f - 32) * (5/9)
    set_jan_2020_austin_temp_c = set()
    for f in jan_2020_austin_temp_f:
        t_celsius = round((f - 32) * (5/9), 2)
        set_jan_2020_austin_temp_c.add(t_celsius)
    print(set_jan_2020_austin_temp_c)

    # TODO: Using Comprehension
    set_jan_2020_austin_temp_comp = {round((f - 32) * (5/9), 1) for f in jan_2020_austin_temp_f}
    print(set_jan_2020_austin_temp_comp)


if __name__ == '__main__':
    main()
