import random

GAME_CONDITION = "Answer 'yes' if the number is even, otherwise answer 'no'."


def get_logic_game():
    """
    Игра угадай четные цифры
    :return:
    """

    game_logic = random.randint(1, 100)
    if game_logic % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return game_logic, str(correct_answer)
