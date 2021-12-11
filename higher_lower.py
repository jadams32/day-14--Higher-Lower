
# import logo
from game_art import logo
from game_art import vs

# import random
import random
#import game data
from game_data import data

from os import system, name

# select two random entities
entity_a = random.choice(data)
entity_b = random.choice(data)

score = 0

def play_again():
    play = input('Would you like to play again? "Yes" or "No".\n').lower()
    if play == "yes":
        clear()
        entity_a = random.choice(data)
        entity_b = random.choice(data)
        main_game(score, entity_a, entity_b)

def correct(score):
    score += 1
    print(f"You are correct! Your current score is {score}")
    return score

def clear():
        # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def main_game(score, entity_a, entity_b):
    if entity_a == entity_b:
        entity_a = random.choice(data)
        entity_b = random.choice(data)

    print(logo)
    print(f'Compare A: {entity_a.get("name")}, {entity_a.get("description")}, from {entity_a.get("country")}')
    print(vs)
    print(f'Against B: {entity_b.get("name")}, {entity_b.get("description")}, from {entity_b.get("country")}')
    choice = input('Who has more followers? Type "A" or "B":\n').lower()

    if choice == "a" and entity_a.get("follower_count") > entity_b.get("follower_count"):
        clear()
        main_game(correct(score), entity_b, random.choice(data))


    elif choice == "b" and entity_b.get("follower_count") > entity_a.get("follower_count"):
        clear()
        main_game(correct(score), entity_b, random.choice(data))

    elif choice == "a" and entity_a.get("follower_count") < entity_b.get("follower_count"):
        print(f"That is incorrect! You lose.")
        play_again()

    else:
        print(f"That is incorrect! You lose.")
        play_again()

main_game(0, entity_a, entity_b)

# Task list
# Refractor code
# Comment code
