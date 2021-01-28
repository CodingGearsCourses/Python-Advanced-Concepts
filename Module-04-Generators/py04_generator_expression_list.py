# Copyright 2020 https://www.globaletraining.com/
# Simple "for" loops can be written using generator expression


# Sample list
animals = ['dog', 'cat', 'hen', 'fox', 'elephant']

# TODO: Generator Expression <<<
animals_upper_gen = (animal.upper() for animal in animals if animal != "fox")

# TODO: Print
print(list(animals_upper_gen))