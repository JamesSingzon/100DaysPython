from higherlower_art import logo, vs
from higherlower_data import data
from subprocess import run
import random

def format_account(account):
    """Format account data into printable format."""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, {description}, from {country}."

def check_answer(guess, account_A, account_B):
    """Use if statement to check if user is correct."""
    if account_A["follower_count"] > account_B["follower_count"]:
        return guess == "A"
    else:
        return guess == "B"



#Print game title art.
print(logo)
score = 0
game_should_continue = True
B = random.choice(data)


while game_should_continue:

    #Generate random account from the game data.
    A = B
    B = random.choice(data)
    if A == B:
        B = random.choice(data)

    print(f"Compare A: {format_account(A)}")

    #Print game vs art.
    print(vs)

    print(f"Compare B: {format_account(B)}")

    #Ask user for a guess.
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    #Check if user is correct.
    ##Get follower count of each account.

    is_correct = check_answer(guess,A,B)

    run("clear")
    print(logo)

    #Give user feedback on their guess.
    if is_correct:
        score += 1
        print(f"You are correct! Current score: {score}.")
    else:
        game_should_continue = False
        print(f"Got that one wrong. Final score: {score}.")


