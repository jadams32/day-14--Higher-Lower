# Task list
# import logo
from game_art import logo
from game_art import vs

# import random
import random
#import game data
from game_data import data

# select two random entities
entity_a = random.choice(data)
entity_b = random.choice(data)

# Present the logo to the user
print(logo)


print(f'Compare A: {entity_a.get("name")}, {entity_a.get("description")}, from {entity_a.get("country")}')
print(vs)
print(f'Against B: {entity_b.get("name")}, {entity_b.get("description")}, from {entity_b.get("country")}')
choice = input('Who has more followers? Type "A" or "B":\n').lower()

def play_again():
    pass

score = 0

if choice == "a" and entity_a.get("follower_count") > entity_b.get("follower_count"):
    score += 1
    print(f"You are correct! Your current score is {score}")
    entity_a = entity_b
    entity_b = random.choice(data)

elif choice == "b" and entity_b.get("follower_count") > entity_a.get("follower_count"):
    score += 1
    print(f"You are correct! Your current score is {score}")
    entity_a = entity_b
    entity_b = random.choice(data)

elif choice == "a" and entity_a.get("follower_count") < entity_b.get("follower_count"):
    print(f"That is incorrect! You lose.")
    play_again()

else:
    print(f"That is incorrect! You lose.")
    play_again()

print(entity_a.get("follower_count"))
print(entity_b.get("follower_count"))
print(entity_a)
print(entity_b)

# Task list
# places different aspects of the game into functions
# Allow the user to keep guessing until they get it wrong
# Refractor code
# Comment code
