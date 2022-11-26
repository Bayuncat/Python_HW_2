from random import randint

x = int(input("Введите целое число N для создания списка цифр от -N до N : "))
y = []
for i in range(x+1): y.append(i)
for i in range(1,x+1): y.append(-i)
y.sort()
print(f'Теперь у нас есть такой список: {y}')

a=list(map(int,input("Введите список индексов для нахождения произведения чрез пробел ").split()))

result = 1
for i in a:
    try:
        result*=y[i]
    except IndexError:
        print(f'Индекса {i} нет в нашем списке')
                
print(f' Произведение значений указанных индексов = {result}')

# Задача 5 Перемешанный список "y"
for i in range(0, len(y)-1):
    j=randint(0, len(y)-1)
    y[i], y[j] = y[j], y[i]

print("Перемешенный список: ")
print(y)