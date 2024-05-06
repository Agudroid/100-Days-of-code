import pandas as pd


# The idea of the project is count the squirrels diveded by the color of her fur
if __name__ == '__main__':

    squirrel_dict = {}
    squirrel_df = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
    red_color_df = squirrel_df[squirrel_df['Primary Fur Color'] == 'Cinnamon']
    grey_color_df = squirrel_df[squirrel_df['Primary Fur Color'] == 'Gray']
    black_color_df = squirrel_df[squirrel_df['Primary Fur Color'] == 'Black']
    squirrel_dict['Fur Color'] = ['Red', 'Grey', 'Black']
    squirrel_dict['Count'] = [len(red_color_df), len(grey_color_df), len(black_color_df)]
    pd.DataFrame(squirrel_dict).to_csv('Squirrel_Census.csv')
