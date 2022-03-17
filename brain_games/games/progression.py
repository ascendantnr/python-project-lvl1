import random

GAME_CONDITION = "What number is missing in the progression?"


def get_logic_game():
    """
    Игра "Арифметическая прогрессия"

    :return: game_logic, correct_answer
    """
    # random
    n = random.randint(5, 10) # начало прогрессии
    d = random.randint(1, 5) # шаг прогресс
    t = random.randint(50, 100) # конец прогрессии

    l = [] # пустой список
    i = 0

    for i in range(n, t, d):
        l.append(i) # добавляем в список членов прогрессии
        x = random.randint(0, len(l) - 1) # случайное число с прогрессии

    correct_answer = l[x]
    l[x] = '..' # заменяем в списке случайное число по индексу
    game_logic = l

    # logic game

    return game_logic, str(correct_answer)
