set_a = {'col', 'mex', 'bol', 'bra', 'uru', 'ven', 'usa'}
set_b = {'per', 'arg', 'bol', 'ecu', 'chi', 'par'}

# unión de conjuntos
set_union = set_a.union(set_b)
print(set_union)
print(set_a | set_b)

# interseccio de conjuntos
set_intersection = set_a.intersection(set_b)
print(set_intersection)
print(set_a & set_b)

# diferencia le resta al primer conjunto los elementos repetidos en el segundo
set_difference = set_a.difference(set_b)
print(set_difference)
print(set_a - set_b)

# diferencia simétrica  resta la intersección de los dos conjuntos
set_symmetric_diff = set_a.symmetric_difference(set_b)
print(set_symmetric_diff)
print(set_a ^ set_b)
