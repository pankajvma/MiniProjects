import pandas as pd

df = pd.read_csv('indian_states.csv')

states = df.state
x_values = df.x
y_values = df.y

map_dict = {}
x = 0
y = 0

for state in states:
    map_dict[state] = (x_values[x], y_values[y])
    x += 1
    y += 1

