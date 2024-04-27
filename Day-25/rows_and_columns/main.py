import pandas as pd

# Every table is a Dataframe, every single column is a series
dataframe = pd.read_csv('../weather_data.csv')

print(dataframe.to_dict())

temp_list = dataframe['temp'].to_list()
print(f'Average temperature: {round(sum(temp_list)/len(temp_list),2)}')

# Or
avg_temp = round(dataframe['temp'].mean(), 2)
print(f'Average temperature: {avg_temp}')
