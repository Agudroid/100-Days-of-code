import pandas as pd
import csv


# First form to take the data
with open('../weather_data.csv') as file:
    lines = file.readlines()
    temperatures = []
    for line in lines:
        row = line.split(",")
        if row[1] != 'temp':
            temperatures.append(int(row[1]))
    print(temperatures)

# Second for of extract data
with open('../weather_data.csv') as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != 'temp':
            temperatures.append(int(row[1]))
    print(temperatures)

# Third form using pandas
dataframe = pd.read_csv('../weather_data.csv')
print(dataframe['temp'])
