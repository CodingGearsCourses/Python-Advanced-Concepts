# Copyright 2020 https://www.globaletraining.com/
# Generator pipeline


def get_odd_numbers_squared_and_ending_in_1():
    for n in range(1000):
        if n % 2 != 0:  # Odds
            n **= 2  # Squared
            if n % 10 == 1: # Ending in 1
                print("Match Found --> {}".format(n))


get_odd_numbers_squared_and_ending_in_1()