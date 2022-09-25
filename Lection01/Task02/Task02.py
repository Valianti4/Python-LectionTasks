# Ввод и вывод данных.

# print() - отвечает за вывод данных в консоль.
# input() - отвечает за ввод данных в консоль.

# print('Введите а');
# a = int(input())    # Указываем тип данных.
# print('Введите b');
# b = int(input())
# print(a, b)
# print(f'{a} {b}')
# print(a, '+', b, '=', a+b)  # Так можно записать действие.

a = 200
b = 100
c = a + b
print(c)    # Так тоже можно записывать действие.

a = 12
b = 5
c = a // b  # Так производится целочисленное деление без остатка. С одним слешем - деление с дробным результатом.
print(c)

a = 12
b = 7
c = a % b   # Так производится деление с остатком.
print(c)

a = 2
b = 5
c = a ** b  # Так производится возведение в степень.
print(c)

a = 1.3
b = 3
c = round(a * b, 2)   # Так производится округление дробных чисел до второго знака.
print(c)

a = 2
a += 5  # Так пишется сокращение от выражения a = a + 5.
print(a)    # Точно также это работает и с другими арифметическими действиями.