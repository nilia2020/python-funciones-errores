# dictionario

dict = {}

for i in range(1, 11):
    dict[i] = i * 2
print(dict)
print(type(dict))

# dictionary comprenhension

dict_2 = {i: i * 2 for i in range(1, 11)}
print(dict_2)

#
import random

# a partir de una lista
countries = ["col", "mex", "bol", "per"]
population = {}
for country in countries:
    population[country] = random.randint(1000000, 100000000)

print(population)

# con dict comprenhension

population_2 = {country: random.randint(1000000, 100000000) for country in countries}

print(population_2)

# a partir de dos listas

names = ["maria", "luz", "juan", "mica"]
ages = [45, 36, 19, 14]

# Con comprenhension

print((list(zip(names, ages))))
new_dict = {name: age for (name, age) in zip(names, ages)}
print(new_dict)
