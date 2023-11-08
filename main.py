import pandas as pd
import numpy as np
from weather_from_observations import weather_from_observations
from get_current_weather_metrics import get_current_weather_metrics
from load_observations import load_observations
from plot import weather_plot
import ast


###############################
n_days = 7
your_lat = 58.4
your_lon = 15.6
latin_last_name = "lutescens"
generate_weather = True
do_plot = True
###############################


df = load_observations(f'observations/{latin_last_name}.csv')

if df.empty:
  print('Error: Could not load observations.')
  exit()

if generate_weather:
  weather = weather_from_observations(df, n_days, latin_last_name)
  weather.to_csv(f'weather/{latin_last_name}.csv', index=False)

weather = pd.read_csv(f'weather/{latin_last_name}.csv')

merged = pd.merge(df, weather, left_index=True, right_index=True)

temp_wk_max_values = []
temp_wk_min_values = []
temp_wk_mean_values = []
rain_wk_avg_values = []

indices_to_remove = []

# Calculate values and append them to the lists
for index, row in merged.iterrows():
  if any(["None" in str(x) for x in row]):
    indices_to_remove.append(index)
    continue
  temp_wk_max_values.append(max(ast.literal_eval(row['temperature_2m_max'])))
  temp_wk_min_values.append(min(ast.literal_eval(row['temperature_2m_min'])))
  temp_wk_mean_values.append(np.mean(ast.literal_eval(row['temperature_2m_mean'])))
  rain_wk_avg_values.append(np.mean(ast.literal_eval(row['rain_sum'])))

# Remove rows with missing values
merged = merged.drop(indices_to_remove)

# Assign the lists to new columns in the DataFrame
merged['temp_wk_max'] = temp_wk_max_values
merged['temp_wk_min'] = temp_wk_min_values
merged['temp_wk_mean'] = temp_wk_mean_values
merged['rain_wk_avg'] = rain_wk_avg_values

# Remove outliers
merged = merged[(merged['temp_wk_max'] < 30) & (merged['temp_wk_min'] > -5) & (merged['temp_wk_mean'] > -5) & (merged['temp_wk_mean'] < 30)]


current_weather_stats = get_current_weather_metrics(your_lat, your_lon, n_days)

merged.to_csv('merged.csv', index=False)

if do_plot:
  weather_plot(merged, current_weather_stats, n_days, latin_last_name)