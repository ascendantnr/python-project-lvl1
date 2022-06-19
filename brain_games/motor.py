import prompt


def motor(game):
    """
    Двигатель игры
    :return:
    """
    # Приветствие
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print("Hello, {}!".format(name))

    krug = 0
    # печать на экран условие игры
    print(game.GAME_CONDITION)

    while krug < 3:
        # получить логику игры и правильный ответ
        game_logic, correct_answer = game.get_logic_game()
        print("Question:", game_logic)
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print("Correct!")
            # если количество раундов 3 (счет начинается с нуля 0, 1, 2)
            if krug == 2:
                print("Congratulations, {}!".format(name))
        else:
            game_over(answer, correct_answer, name)
            break
        # после каждого раунда прибавляем на +1
        krug = krug + 1


def game_over(answer_user, correct_answer, name):
    """
    Конец игры
    :return:
    """
    print("'{}' is wrong answer ;(. Correct answer was '{}'."
          .format(answer_user, correct_answer))
    print("Let's try again, {}!".format(name))
