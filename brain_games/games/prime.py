import random

GAME_CONDITION = "Answer ""yes"" if given number is prime. " \
                 "Otherwise answer ""no""."


def get_logic_game():
    """
    Игра "Простое число"

    по формуле Решето Эратосфена

    :return: game_logic, correct_answer
    """

    n = random.randint(0, 10000)  # случайное число с 0 до 10000
    game_logic = n
    a = list(range(n + 1))
    a[1] = 0
    spisok = []

    i = 2
    while i <= n:
        if a[i] != 0:
            spisok.append(a[i]) # добавление в список всех чисел не равных к нулю
            for j in range(i, n + 1, i):
                a[j] = 0
        i += 1

    if n in spisok:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return game_logic, str(correct_answer)
