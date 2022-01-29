#!/usr/bin/env python
import prompt
import random


def main():
    ''''
    Запустите игру, и ответьте на все вопросы правильно
    '''

    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    if name:
        print("Hello, {}!".format(name))
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")
    krug = 0
    while krug < 3:
        # n случайное число с 1 до 100
        n = random.randint(1, 100)
        print("Question: ", n)
        answer = prompt.string('Your answer: ')
        # проверка n число на четность
        if n % 2 == 0 and answer == 'yes' or n % 2 == 1 and answer == 'no':
            print("Correct!")
            # если количество раундов 3 (счет начинается с нуля 0, 1, 2)
            if krug == 2:
                print("Congratulations, {}!".format(name))
        else:
            if n % 2 == 0:
                print("'{}' is wrong answer ;(. Correct answer was 'yes'.".format(answer))
                print("Let's try again, {}!".format(name))
            else:
                print("'{}' is wrong answer ;(. Correct answer was 'no'.".format(answer))
                print("Let's try again, {}!".format(name))
            break
        # после каждого раунда прибавляем на +1
        krug = krug + 1


if __name__ == "__main__":
    main()
