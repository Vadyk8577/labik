q1 = int (input('Введите число 1: '))
q2 = int (input('Введите число 2: '))
q3 = int (input('Введите число 3: '))
q4 = int (input('Введите число 4: '))
v = int (input('Какую операцию вы хотите выполнить? \n 1 Сложение \n 2 Вычитание \n 3 Деление \n 4 Умножение \n'))

if v == 1:
    r = q1 + q2 + q3 + q4
    p = 'сложения'
    t = p
if v == 2:
    r = q1 - q2 - q3 - q4
    l = 'вычитания'
    t = l
if v == 3:
    r = float(q1 / q2 / q3 / q4)
    m = 'деления'
    t = m
if v == 4:
    r = q1 * q2 * q3 * q4
    n = 'умножения'
    t = n
print ('Результат ',t,' = ',r)