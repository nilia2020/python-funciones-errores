import random

countries = ["col", "mex", "bol", "per"]
population_2 = {country: random.randint(1000000, 100000000) for country in countries}
print(population_2)
result = {
    country: population
    for (country, population) in population_2.items()
    if population > 50000000
}
print(result)

text = "Hola soy Jorge"
unique = {c: c.upper() for c in text if c in "aeiou"}
print(unique)
