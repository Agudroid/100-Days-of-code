import pandas as pd

# Every table is a Dataframe, every single column is a series
dataframe = pd.read_csv('../weather_data.csv')

# To transform the dataframe in a dictionary
print(dataframe.to_dict())

# To Transform a series of a dataframe in a list
temp_list = dataframe['temp'].to_list()
print(f'Average temperature: {round(sum(temp_list)/len(temp_list),2)}')

# Or
avg_temp = round(dataframe['temp'].mean(), 2)
print(f'Average temperature: {avg_temp}')

# To get the max row of a column
max_temp = dataframe['temp'].max()
print(f'Max value: {max_temp}')

# Also you can get the column like this
print(dataframe.temp)

# Get a row
print(dataframe[dataframe.day == 'Monday'])

# Get the row with maximum temperature
print(dataframe[dataframe.temp == dataframe.temp.max()])

# Convert Monday´s temperature to Fahrenheit
print(f'Fahrenheit temperature on monday: {dataframe[dataframe.day == "Monday"].temp[0] * 1.8 + 32}')

# Create a dataframe from Scratch
data_dict = {
    'students': ['Any', 'James', 'Angela'],
    'scores': [76, 56, 38]
}

student_df = pd.DataFrame(data_dict)
print(student_df)
