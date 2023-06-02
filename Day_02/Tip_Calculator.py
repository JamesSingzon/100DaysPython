print("Welcome to the tip calculator.")
subtotal = float(input("What was the total bill? $"))
tip = 1+int(input("What percentage tip would you like to give? 10, 12, or 15? "))/100
split = int(input("How many people to split the bill? "))

total = "{:.2f}".format(subtotal * tip / split,2)

print(f"Each person should pay: ${total}")