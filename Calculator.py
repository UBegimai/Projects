c = input("Выберите операцию(+, -, *, /, %, **, //): ")
a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))

if c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '*':
    print(a * b)
elif c == '/':
    print(a / b)
elif c == '%':
    print(a % b)
elif c == '**':
    print(a ** b)
elif c == '//':
    print(a // b)
else:
    print('Данной операции нет в системе')