from game_data import data                                          #import ASCII art
from art import logo, vs
import random
print(logo)

# Choose 2 random objects from data and Print both the statements.
def comparison(compare_1):
    print(f"Compare A: {compare_1['name']}, a {compare_1['description']}, from {compare_1['country']}.")
    print(vs)                                                       # Insert 'vs.' ASCII art in between.

    compare_2 = random.choice(data)
    print(f"Against B: {compare_2['name']}, a {compare_2['description']}, from {compare_2['country']}.")

    # Input answer from user
    user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()

    return compare_2, user_choice

compare_1 = random.choice(data)
compare_2, user_choice = comparison(compare_1)              #Input compare_1 value, Catching compare_2 & user_choice values

game_continue = True
score = 0

#'if-else' statement. Choose & Print another random object if the user choice is right. Else, Game Over.
while game_continue:
    if user_choice == "A":
        chosen_option = compare_1
        other_option = compare_2
    elif user_choice == "B":
        chosen_option = compare_2
        other_option = compare_1
    else:
        print("Invalid choice.")
        break
    
    if chosen_option['follower_count'] > other_option['follower_count']:
        score += 1
        print(f"You're Right! Current Score: {score}\n")
        
        compare_1 = compare_2
        compare_2, user_choice = comparison(compare_1)
    else:
        game_continue = False
        print(f"Sorry, That's Wrong. Final Score: {score}")

        # Track Score (+1) for right answer. 
        # Display Score when Game Over.    