def increment(x):
    return x + 1


increment2 = lambda x: x + 1


def hof(x, func):
    return x + func(x)


hof2 = lambda x, func: x + func(x)

result = hof(2, increment)
result2 = hof2(3, increment2)
result3 = hof2(2, lambda x: x + 2)
result4 = hof2(2, lambda x: x * 3)

print(result)
print(result2)
print(result3)
print(result4)
