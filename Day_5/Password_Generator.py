import random

print("Welcome to the PyPassword Generator!")
num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like?\n"))
num_numbers = int(input("How many numbers would you like?\n"))
valuable = ""

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
library = [letters, numbers, symbols]

for letter in range(0,num_letters):
    valuable = valuable + f"{random.choice(letters)}"
for number in range(0,num_numbers):
    valuable = valuable + f"{random.choice(numbers)}"
for symbol in range(0,num_symbols):
    valuable = valuable + f"{random.choice(symbols)}"


# for i in range(0,num_letters+num_symbols+num_numbers):
#     valuable = valuable + f"{random.choice(random.choice(library))}"
valuable = "".join(set(valuable))


print(f"Here is your password:  {valuable}")