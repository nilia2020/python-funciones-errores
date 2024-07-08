set_countries = {'col', 'mex', 'bol'}

# len() : Devuelve el tamaño del conjunto
size = len(set_countries)
print(size)

print('col' in set_countries)
print('arg' in set_countries)

# add
set_countries.add('arg')
print(set_countries)
# update
set_countries.update({'per', 'ecu', 'col'})
print(set_countries)
# remove
set_countries.remove('col')
print(set_countries)
# discard, si no existe no da error, si existe lo elimna
set_countries.discard('col')
print(set_countries)
#pop(): Nos devuelve un elemento aleatorio y lo elimina y si el conjunto está vacío lanza el error “key error”.
print(set_countries.pop())
print(set_countries)
# clear borra todo el conjunto
set_countries.clear()
print(len(set_countries))