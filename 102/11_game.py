import random


def options_choose():
    options = ("piedra", "papel", "tijera")
    user_option = input("piedra, papel o tijera => ")
    user_option = user_option.lower()
    if not user_option in options:
        print("esa opcion no es valida")
        return None, None

    computer_option = random.choice(options)

    print("User option =>", user_option)
    print("Computer option =>", computer_option)
    return user_option, computer_option


def rules(user_option, computer_option, user_wins, computer_wins):

    if user_option == computer_option:
        print("Empate!")
    elif user_option == "piedra":
        if computer_option == "tijera":
            print("piedra gana a tijera")
            print("user gano!")
            user_wins += 1
        else:
            print("Papel gana a piedra")
            print("computer gano!")
            computer_wins += 1
    elif user_option == "papel":
        if computer_option == "piedra":
            print("papel gana a piedra")
            print("user gano")
            user_wins += 1
        else:
            print("tijera gana a papel")
            print("computer gano!")
            computer_wins += 1
    elif user_option == "tijera":
        if computer_option == "papel":
            print("tijera gana a papel")
            print("user gano!")
            user_wins += 1
        else:
            print("piedra gana a tijera")
            print("computer gano!")
            computer_wins += 1
    return user_wins, computer_wins


def check_winner(user_wins, computer_wins):
    if computer_wins == 2:
        print("El ganador es la computadora")
        return True
    if user_wins == 2:
        print("El ganador es el usuario")
        return True
    return False


def run_game():
    user_wins = 0
    computer_wins = 0
    rounds = 1
    winner = False
    while True:
        print("*" * 10)
        print("ROUND", rounds)
        print("*" * 10)

        print("computer_wins", computer_wins)
        print("user_wins", user_wins)

        rounds += 1

        user_option, computer_option = options_choose()

        user_wins, computer_wins = rules(
            user_option, computer_option, user_wins, computer_wins
        )
        winner = check_winner(user_wins, computer_wins)
        if winner:
            print("computer_wins", computer_wins)
            print("user_wins", user_wins)
            break


run_game()
