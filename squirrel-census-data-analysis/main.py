import pandas as pd

squirrel_census_data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

# print(squirrel_census_data)
attribute_to_check = 'Primary Fur Color'

gray_squirrels = squirrel_census_data[squirrel_census_data[attribute_to_check] == 'Gray']
cinnamon_squirrels = squirrel_census_data[squirrel_census_data[attribute_to_check] == 'Cinnamon']
black_squirrels = squirrel_census_data[squirrel_census_data[attribute_to_check] == 'Black']

print(f"Gray: {len(gray_squirrels)}")
print(f"Cinnamon: {len(cinnamon_squirrels)}")
print(f"Black: {len(black_squirrels)}")
