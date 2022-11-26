from functools import reduce

a = input("Введите вещественное число для нахождения суммы его цифр: ")

x = list(str(a))
y = []

for i in x:
    if i.isdigit(): y.append(i)

y=list(map(int,y))
sum_all = reduce(lambda x,y: x + y, y)
print(sum_all)