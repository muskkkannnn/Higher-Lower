from game_data import data
from art import logo, vs
import random
#import ASCII art
print(logo)

# Choose 2 random objects from data and Print both the statements.
compare_1 = random.choice(data)

def comparison():
    print(f"Compare A: {compare_1['name']}, a {compare_1['description']}, from {compare_1['country']}.")

    # Insert 'vs.' ASCII art in between.
    print(vs)

    compare_2 = random.choice(data)
    print(f"Against B: {compare_2['name']}, a {compare_2['description']}, from {compare_2['country']}.")

    user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    
    return compare_1, compare_2

compare_1, compare_2 = comparison() 

# Input answer from user
# user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()

#'if-else' statement. Choose & Print another random object if the user choice is right. Else, Game Over.
if user_choice == "A":
    user_choice = compare_1
    other_choice = compare_2
elif user_choice == "B":
    user_choice = compare_2
    other_choice = compare_1
# else:
#     print("NO such choice.")

score = 0

if user_choice['follower_count'] > other_choice['follower_count']:
    score += 1
    print(f"You're Right! Current Score: {score}\n")

    compare_1 = compare_2
    comparison()
else:
    print(f"Sorry, That's Wrong. Final Score: {score}")

# Track Score (+1) for right answer. 
# Display Score when Game Over.    