import random

GAME_CONDITION = "What number is missing in the progression?"


def get_logic_game():
    """
    Игра "Арифметическая прогрессия"

    :return: game_logic, correct_answer
    """
    # random
    a1 = random.randint(1, 10)  # начало прогрессии
    d = random.randint(1, 5)  # шаг прогрессии
    n = random.randint(5, 10)  # длина прогрессии
    progress = []
    i = 1
    while i < n + 1:
        an = a1 + (i - 1) * d
        i = i + 1
        progress.append(an)  # добавляем в список членов прогрессии

    x = random.randint(0, n) # случайное число с прогрессии
    correct_answer = progress[x]
    progress[x] = ".." # заменяем в списке случайное число по индексу
    game_logic = progress

    # logic game

    return game_logic, str(correct_answer)
