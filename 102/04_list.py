# Creamos una lista de números con un for

numbers = []

for element in range(1, 11):
    numbers.append(element * 2)

print(numbers)

# Ahora en una sóla linea de código 'list comprenhension'

numbers_2 = [element * 2 for element in range(1, 21)]
print(numbers_2)

# con un condicional

numbers_3 = []

for element in range(1, 11):
    if element % 2 == 0:
        numbers_3.append(element * 2)

print(numbers_3)

# condicional y for en list comprenhension


numbers_4 = [element * 2 for element in range(1, 11) if element % 2 == 0]

print(numbers_4)
