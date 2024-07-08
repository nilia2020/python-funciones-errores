# Sets (Conjuntos). Se pueden modificar. No tienen un orden. No permiten duplicados
set_countries = {'col', 'mex', 'bol'}
print(set_countries)
print(type(set_countries))
# Si yo agrego elementos repetidos, se eliminan
set_countries2 = {'col', 'mex', 'bol', 'col'}
print(set_countries2)
print(type(set_countries2))
# Los escribo desordenados y repetidos
set_numbers = {1,2,2,3,4,5,8,6,7}
# Me los imprime ordenados y sin repeticiones 
print(set_numbers)
print(type(set_numbers))
# Un conjunto mixto
set_types = {'Luz', 1, True, 100.0}
print(set_types)
print(type(set_types))
# con la función set lo creo a partir de otro tipo de datos
set_from_string = set('durand')
print(set_from_string)
print(type(set_from_string))
set_from_tuple = set(('ab', 'bc', 'cd', 'ef', 'ab'))
print(set_from_tuple)
print(type(set_from_tuple))
# la podemos crear a partir de una lista
numbers = [1,2,3,1,2,3,4]
print(numbers)
set_numbers= set(numbers)
print (set_numbers) # {1, 2, 3, 4}
# si quiero convertir este set único a una lista, lo puedo hacer:
unique_numbers = list(set_numbers)
print (unique_numbers)
print(type(numbers))