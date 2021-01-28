**What are comprehensions?**

numbers = [1, 2, 3, 4, 5]

**Without comprehensions**

numbers_squared = []
for n in numbers:
    numbers_squared.append(n**2)
print(numbers_squared)

**With comprehensions**

numbers_squared = [n**2 for n in numbers_squared]
print(numbers_squared)
    