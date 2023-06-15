# #FileNotFound
# # with open("a_file.txt") as file:
# #   file.read()
# try:
#     file = open("Day_30/a_file.txt")
#     a_dict = {"key":"value"}
#     print(a_dict["addfses"])
# except FileNotFoundError:
#     # print("There was an error.")
#     file = open("Day_30/a_file.txt", "w")
#     file.write("Something")
# # except KeyError:
# #     print("That key does not exist.")
# except KeyError as error_message:
#     print(f"That key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     # file.close()
#     # print("File was closed.")
#     # raise KeyError
#     raise TypeError("This is an error I made up.")



# #KeyError
# # a_dict = {"key":"value"}
# # value = a_dict["non-existent key"]

# #IndexError
# # fruit_list = ["Apple", "Banana", "Pear"]
# # fruit = fruit_list[3]

# #TypeError
# # text = "abc"
# # print(text + 5)

#When might you want to raise errors?

height = float(input("Height: "))
weight = int(input("Weight: "))

#Humans have never been taller than 3 meters, so we'll raise an error and add a message
if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")

bmi = weight/(height * height)
print(bmi)

