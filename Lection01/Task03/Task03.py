# Логические операции.

a = 1 > 4   # Ложное выражение.
print(a)

a = 1 < 4 and 5 > 2     # Истинное выражение с использованием логической операции "and".
print(a)

a = 1 != 2
print(a)

a = 1 < 3 < 5   # В пайтоне можно использовать тройные и более неравенства.
print(a)

f = 1 > 2 or 4 < 6
print(f)

f = [1,2,3,4]
print(f)
print(2 in f)   # Истина.
print(not 2 in f)   # Ложь.

is_Odd = not f[0] % 2  # Проверка на чётность элемента списка.
print(is_Odd)