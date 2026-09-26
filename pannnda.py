# import csv

# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     next(data) 
#     temperatures = []
#     for row in data:
#         print(row) 
#         temperatures.append(int(row[1])) 
# print(temperatures)

import pandas
data = pandas.read_csv("weather_data.csv")
temperatures = data["temp"]
# print(data)
print(temperatures)
print(data.head(3))
print(data.tail(3))
print(int(data["temp"].mean()))
maximum = data["temp"].max()
print(data[data.temp == maximum])
monday = data[data.day == "Monday"]
print((monday.temp * 1.8) + 32)