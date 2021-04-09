import pandas as pd

squirrel_census_data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv') # reading csv

attribute_to_check = 'Primary Fur Color' # We have to find the number of squirrels with different colors

total_squirrels = squirrel_census_data[attribute_to_check]
gray_squirrels = squirrel_census_data[squirrel_census_data[attribute_to_check] == 'Gray']
cinnamon_squirrels = squirrel_census_data[squirrel_census_data[attribute_to_check] == 'Cinnamon']
black_squirrels = squirrel_census_data[squirrel_census_data[attribute_to_check] == 'Black']


data_dict = {
    "Fur color": ['Gray', 'Cinnamon', 'Black'],
    "Squirrel count": [len(gray_squirrels), len(cinnamon_squirrels), len(black_squirrels)]
}

for data in data_dict.items():
    print(data)

print("Data Stored in the CSV")

# Creating and saving dataframe as CSV
df = pd.DataFrame(data_dict)
df.to_csv('squirrel_count_data_frame.csv')