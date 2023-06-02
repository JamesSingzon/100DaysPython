height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))


BMI = weight/height**2
BMI_rounded = round(BMI)
conditions = ("underweight", "normal weight", "overweight", "obese", "clinically obese")

if BMI < 18.5:
    print(f"Your BMI is {BMI_rounded}, you are {conditions[0]}.")
elif BMI < 25:
    print(f"Your BMI is {BMI_rounded}, you have a {conditions[1]}.")
elif BMI < 30:
    print(f"Your BMI is {BMI_rounded}, you are slightly {conditions[2]}.")
elif BMI < 35:
    print(f"Your BMI is {BMI_rounded}, you are {conditions[3]}.")
else:
    print(f"Your BMI is {BMI_rounded}, you are  {conditions[4]}.")
