a, b, c = map(int, input('Введите три целых числа через пробел: ').split())

x = a * b
y = b * c
z = c * a

print('Умножение:')
print('a * b =', x)
print('a * c =', y)
print('c * a =', z)

d = a ** 4
e = b % c
g = c // a

print('Возведение в степень,остаток,целочисленное деление:')
print('a ^ 4 =', d)
print('b % C =', e)
print(' c // a =', g)

s = d + e + g
print('Сумма =', s)

Dmitrieva