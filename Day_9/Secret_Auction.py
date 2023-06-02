import subprocess

subprocess.run('clear')
print("""
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                      /_______________\")
""")
print("Welcome to the secret auction program.")
more = True
registry = {}
highest_bid = 0
while more:
    name = input("What is your name?: ")
    bid = input("What is your bid?: $")
    more = input("Are there any other bidders?  Type 'yes' or 'no'.\n")
    registry[name] = int(bid)
    subprocess.run('clear')
    if more == 'no':
        more = False
        for key in registry:
            if registry[key] > highest_bid:
                highest_bid = registry[key]
        print("The highest bidder is "+ str(highest_bid) + "!  Congratulations!")
