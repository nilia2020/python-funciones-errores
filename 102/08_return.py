def sum_range(a, b):
    sum = 0
    count = 0
    for x in range(a, b):
        sum += x
        count += 1
    print("suma de ", a, "hasta ", b)
    return sum


res1 = sum_range(5, 10)
print(res1)
res2 = sum_range(res1, res1 + 100)
print(res2)
