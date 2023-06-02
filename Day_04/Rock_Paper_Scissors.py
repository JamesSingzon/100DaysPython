import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    """

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
    """

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    """

user_choice = int(input("What do you choose?  Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
else:
    print(scissors)


mersenne_twister = random.randint(0,2)

print("Computer chose:\n")

if mersenne_twister == 0:
    print(rock)
elif mersenne_twister == 1:
    print(paper)
else:
    print(scissors)


if mersenne_twister == user_choice:
    print("Tie")
elif mersenne_twister == 0 and user_choice == 1:
    print("You win")

elif mersenne_twister == 0 and user_choice == 2:
    print("You lose")

elif mersenne_twister == 1 and user_choice == 0:
    print("You lose")

elif mersenne_twister == 1 and user_choice == 2:
    print("You win")

elif mersenne_twister == 2 and user_choice == 0:
    print("You win")

elif mersenne_twister == 2 and user_choice == 1:
    print("You lose")
