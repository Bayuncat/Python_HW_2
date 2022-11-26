from functools import reduce
import math

x = int(input("Введите целое число для нахождения сумм последоательности (1 + 1/n)^n : "))
y = []
for i in range(1,x+1): y.append((1+1/i)**i)

sum_all = reduce(lambda x,y: x + y, y)
print(round(sum_all,2))