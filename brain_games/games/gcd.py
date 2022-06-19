import random

GAME_CONDITION = "Find the greatest common divisor of given numbers."


def get_logic_game():
    """
     самый большой делитель

    :return:
    """
    # random
    a = random.randint(1, 1000)
    b = random.randint(1, 1000)

    game_logic = "{} {}".format(a, b)

    # logic game

    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a

    correct_answer = a + b

    return game_logic, str(correct_answer)
