# import csv
# with open("Day_25/weather_data.csv") as wthr:
#     temperatures = []
#     data = csv.reader(wthr)
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))



#         temperatures.append(row[1])
#     temperatures.pop(0)
#     for item in range(len(temperatures)):
#         temperatures[item] = int(temperatures[item])
#         # with open("Day_25/temp_data.csv", mode="a") as temp_data:
#         #     temp_data.write(int(item))
# print(temperatures)


import pandas

# data = pandas.read_csv("Day_25/weather_data.csv")
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].mean()
# print(temp_list)
# temp_list = data["temp"].max()
# print(temp_list)

#Get data in columns
# print(data["condition"])
# print(data.condition)

#Get data in rows
# print(data[data.temp == data["temp"].max()])

# monday = data[data.day == "Monday"]
# monday_temp = int(monday["temp"])
# print(monday_temp * (9/5)+32)

# #Create a dataframe from scratch
# data_dict = {
#     "students":["Amy", "James", "Angela"],
#     "scores":[76, 56, 65]
# }

# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("Day_25/new_data.csv")

#Import Squirrel data csv, create table of fur color and the count

data = pandas.read_csv("Day_25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

fur_series = data["Primary Fur Color"]
colors = data["Primary Fur Color"]
gray = data[fur_series == "Gray"]["Primary Fur Color"].count()
cinn = data[fur_series == "Cinnamon"]["Primary Fur Color"].count()
black = data[fur_series == "Black"]["Primary Fur Color"].count()


# print(colors.dropna())


fur_color_count = {"colors":[], "count":[]}

for i in colors.dropna().unique():
    fur_color_count["colors"].append(i)
    fur_color_count["count"].append(data[fur_series == i]["Primary Fur Color"].count())

print(fur_color_count)
print(gray)
print(cinn)
print(black)

df_gen = pandas.DataFrame(fur_color_count)
print(df_gen)
df_gen.to_csv("Day_25/fur_color_count.csv")