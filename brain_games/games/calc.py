import random

GAME_CONDITION = "What is the result of the expression?"


def get_logic_game():
    """
    Калкулятор

    :return:
    """
    operation = ['+', '-', '*']
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    c = random.choice(operation)
    game_logic = "{} {} {}".format(a, c, b)

    if c == '-':
        correct_answer = a - b
    elif c == '+':
        correct_answer = a + b
    elif c == '*':
        correct_answer = a * b

    return game_logic, str(correct_answer)
