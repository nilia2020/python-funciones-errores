numbers = [1, 2, 3, 4]

numbers2 = []
for i in numbers:
    numbers2.append(i * 2)

print(numbers)
print(numbers2)

numbers3 = list(map(lambda i: i * 2, numbers))

print(numbers3)

numbers_one = [1, 2, 3, 4]
number_two = [5, 6, 7]

numbers4 = list(map(lambda a, b: a + b, numbers_one, number_two))

print(numbers4)
