import random


def roll_dice():
    return random.randint(1, 6)


def play_game():
    player_scores = [0, 0]  # Рахунок гравців [Гравець 1, Гравець 2]
    current_player = 0  # Індекс поточного гравця

    while max(player_scores) < 10:
        input(f"Гравець {current_player + 1}, натисніть Enter для кидка кубиків...")

        dice1 = roll_dice()
        dice2 = roll_dice()
        total = dice1 + dice2

        print(f"Гравець {current_player + 1} кидає кубики: {dice1}, {dice2} (сума: {total})")

        if total in (7, 11):
            print(f"Гравець {current_player + 1} виграв заробляє 1 бал")
            player_scores[current_player] += 1
        elif total in (2, 8, 12):
            print("Гравець не заробляє 1 бал")
        else:
            print("Спеціальний раунд - Додатковий раунд!")

            while True:
                input("Натисніть Enter для кидка кубика в Додатковому раунді...")
                dice = roll_dice()
                print(f"Гравець {current_player + 1} кидає кубик в Додатковому раунді: {dice}")

                if dice == 7:
                    print("Вихід з Додаткового раунду. Гравець не заробляє 1 бал")
                    break
                elif dice in (3, 4, 5, 6, 9, 10):
                    print("Вихід з Додаткового раунду. Гравець виграє 1 бал")
                    player_scores[current_player] += 1
                    break
                elif dice in (2, 8, 12):
                    print("Продовження Додаткового раунду...")
                else:
                    print("Непередбачене число. Спробуйте ще раз...")

        print(f"Рахунок: Гравець 1: {player_scores[0]}, Гравець 2: {player_scores[1]}\n")
        current_player = (current_player + 1) % 2

    winner = player_scores.index(10) + 1
    print(f"Гравець {winner} переміг!")
