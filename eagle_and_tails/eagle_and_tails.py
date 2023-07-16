import random

def play_coin_flip():
    choices = ["о", "р"]
    player_score = 0
    computer_score = 0
    while player_score < 3 and computer_score < 3:
        player_choice = input("Введіть свій вибір (Орел - о або Решка - р): ")
        # Перевіряємо, чи гравець ввів коректний вибір
        if player_choice not in choices:
            print("Некоректний вибір! Будь ласка, введіть о - означає Орел або р - означає Решка")
            continue
        # Робимо випадковий вибір
        computer_choice = random.choice(choices)
        # Виводимо результат
        print(f"Ваш вибір: {player_choice}")
        print(f"Вибір комп'ютера: {computer_choice}")
        if player_choice == computer_choice:
            print("Ви виграли раунд!")
            player_score += 1
        else:
            print("Комп'ютер виграв раунд!")
            computer_score += 1
        print(f"Рахунок: Гравець - {player_score}, Комп'ютер - {computer_score}")
        print("---------------------")
    if player_score == 3:
        print("Ви перемогли гру!")
    else:
        print("Комп'ютер переміг гру!")
        
# Викликаємо функцію для початку гри
play_coin_flip()