# Операции условия if else и циклы.

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

# Цикл while.

from typing import List


a = 23
i = 0
while a != 0:
    i = i * 10 + (a % 10)
    a //= 10
print(i)

# В пайтоне у цикла while имеется блок else.

a = 23
i = 0
while a != 0:
    i = i * 10 + (a % 10)
    a //= 10
else:
    print('Пожалуй')
    print('хватит.')
print(i)

# Цикл for.

List = [1,2,3,4,10,5]
for i in List:
    print(i**2)


for i in range(4):
    print(i)

for i in range(1, 10, 2):   # Где 1 - с какого числа цикл начнёт работу, 10 - общее число элементов, 2 - шаг итерации цикла.
    print(i)