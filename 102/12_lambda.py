def increment(x):
    return x + 1


result = increment(10)
result2 = lambda x: x + 1
print(result)
print(result2(20))

full_name = lambda name, last_name: f"Su nombre es: {name.title()} {last_name.title()}"

text = full_name("jorge", "niglia")
print(text)
