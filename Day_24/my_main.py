# with open("/Users/jamessingzon/Desktop/100DaysPython/Day_24/my_file.txt") as file:
#     contents = file.read()
#     print(contents)

with open("my_file.txt", mode="r") as file:
    contents = file.read()

print(contents)