from random import randint

data = [randint(-10,10) for _ in range(10)]
d2 = filter(lambda x : x>=0, data)
print(data)
print(d2)
print(list(d2))