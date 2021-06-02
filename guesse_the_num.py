import random

guesses_made = 0
name = input('Введите ваше имя: ')
answer = input('Хотите ли вы сыграть?: ')

if answer == 'нет':
    print('Игра завершена.')

number = random.randint(1, 10)
print(f'{name} загадал число от 1 до 10.')
while guesses_made < 10:
    guess = int(input('Угадайте число: '))
    guesses_made +=1
    if guess > number:
        print('Число большое, есть еще попытка.')
    elif guess < number:
        print('Маленькое...')
    elif guess == number:
        answer2 = input('Хотите ли вы пройти игру еще раз?: ')
        if answer2 == 'нет':
            print('Игра завершилась. Спасибо за игру!')
            break
print(f'Попыток сделано: {guesses_made}.')