import pandas as pd
import csv

# data_values = []
# with open('weather_data.csv') as data:
#     value = data.readlines()
#     data_values.append(value)

# print(data_values)

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     data = list(data)
#     temperatures = []
#     for row in data[1:]:
#         temperatures.append(int(row[1]))

# print(temperatures)

squirrel_data = pd.read_csv("4. 2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(squirrel_data)

primary_fur_color = squirrel_data['Primary Fur Color']
# print(primary_fur_color)

count_gray = 0
count_cinnamon = 0
count_black = 0
for color in primary_fur_color:
    if color == 'Gray':
        count_gray+=1
    elif color == 'Cinnamon':
        count_cinnamon+=1
    elif color == 'Black':
        count_black+=1

    
squirrel_count_dic = {
    'Fur Color' : ['Gray', 'Cinnamon', 'Black'],
    'Count' : [count_gray, count_cinnamon, count_black]
}

squirrel_count = pd.DataFrame(squirrel_count_dic)
squirrel_count_csv = 'squirrel_count'
squirrel_count.to_csv(squirrel_count_csv, index=False)
print(squirrel_count)


