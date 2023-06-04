#Create a new list from a previous list
#Previously we've been using a for loop
#KEY WORD METHOD:
# new_list = [new_item for item in list]
#PYTHON SEQUENCES:
#list
#range
#string
#tuple

#Conditional List Comprehension
#2 new keywords
# new_list = [new_item for item in list if test]


#Examples
# >>> numbers = [1,2,3]
# >>> new_numbers = [n+1 for n in numbers]
# >>> new_numbers
# [2, 3, 4]
# >>> name = "James"
# >>> letter_list = [letter for letter in name]
# >>> letter_list
# ['J', 'a', 'm', 'e', 's']
# >>> double_num = [2*num for num in range(1,5)]
# >>> double_num
# [2, 4, 6, 8]
# >>> names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
# >>> names[4] = "Eleanor"
# >>> names
# ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# >>> short_names = [name for name in names if len(name) <= 4]
# >>> short_names
# ['Alex', 'Beth', 'Dave']
# >>> long_names = [name.upper() for name in names if len(name) < 4]
# >>> long_names
# []
# >>> long_names = [name.upper() for name in names if len(name) > 4]
# >>> long_names
# ['CAROLINE', 'ELEANOR', 'FREDDIE']
# >>> 


# Example1:
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆

#Write your 1 line code 👇 below:

squared_numbers = [num**2 for num in numbers]

#Write your code 👆 above:

print(squared_numbers)

# Example2:
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above

#Write your 1 line code 👇 below:

result = [num for num in numbers if num%2 == 0]

#Write your code 👆 above:

print(result)

# Example3:
with open("file1.txt") as f1:
    f1_list = [int(line) for line in f1.readlines()]
print(f1_list)
with open("file2.txt") as f2:
    f2_list = [int(line) for line in f2.readlines()]
print(f2_list)

result = [common_num for common_num in f2_list if common_num in f1_list]
# Write your code above 👆

print(result)