#Allows us to create a new dictionary from the items in a dict or list
#KEY WORD METHOD:
#new_dict = {new_key:new_value for item in list}
#new_dict = {new_key:new_value for (key,value) in dict.items()}
#new_dict = {new_key:new_value for (key,value) in dict.items() if test}

# Examples:
# >>> names
# ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# >>> students_scores = {student:random.randint(1,100) for student in names}
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 1, in <dictcomp>
# NameError: name 'random' is not defined
# >>> import random
# >>> students_scores = {student:random.randint(1,100) for student in names}
# >>> students_scores
# {'Alex': 94, 'Beth': 2, 'Caroline': 52, 'Dave': 9, 'Eleanor': 69, 'Freddie': 73}
# >>> passed_students = {key:value for (key,value) in students_scores.items() if value >= 60}
# >>> passed_students
# {'Alex': 94, 'Eleanor': 69, 'Freddie': 73}
# >>> students_scores.items()
# dict_items([('Alex', 94), ('Beth', 2), ('Caroline', 52), ('Dave', 9), ('Eleanor', 69), ('Freddie', 73)])
# >>> 

# Example1:
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:
result = {word:len(word) for word in sentence.split()}


print(result)

# Example2:
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:
weather_f = {day:((temp_c * 9/5) + 32) for day,temp_c in weather_c.items()}


print(weather_f)