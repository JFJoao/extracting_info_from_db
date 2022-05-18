# import csv
#
# with open("weather_data.csv") as weather_file:
#     weather_data = csv.reader(weather_file)
#     temperatures = []
#     for each in weather_data:
#         if each[1] != 'temp':
#             temperatures.append(int(each[1]))
#     print(temperatures)

import pandas
import statistics

# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
# print(data[data.temp == data["temp"].max()])

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(data["Primary Fur Color"])
gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
cinnamon_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# print(black_squirrel_count)
data_dict = {
    "Primary Fur Color" : ["Gray", "Black", "Cinnamon"],
    "Count" : [gray_squirrel_count, black_squirrel_count, cinnamon_squirrel_count]
}
df_data = pandas.DataFrame(data_dict)
print(df_data)
df_data.to_csv("Squirrel Colours Count")
