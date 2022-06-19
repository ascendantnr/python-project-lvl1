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

    x = random.randint(0, n - 1)
    correct_answer = progress[x]

    copy_progress = progress
    copy_progress[x] = ".."
    list_to_str = " ".join(map(str, copy_progress))
    game_logic = list_to_str

    # logic game

    return game_logic, str(correct_answer)
