import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import skewnorm
import json
mushrooms = json.load(open('mushrooms.json'))



def weather_plot(merged, current_weather_stats, n_days, name):

  swe_name = mushrooms[name]['swedish']

  x = np.linspace(-10, 30, 100)

  fig, axs = plt.subplots(2, 2)

  wk_mean_norm = skewnorm.fit(merged['temp_wk_mean'])
  axs[0,0].plot(x, skewnorm.pdf(x, *wk_mean_norm))
  axs[0, 0].hist(merged['temp_wk_mean'], bins=20, density=True)
  axs[0, 0].set_title(f'Latest {n_days} day mean temperature')
  axs[0, 0].set_xlabel('Temperature (°C)')
  axs[0, 0].axvline(current_weather_stats['temp_mean'], color='red', linestyle='dashed', linewidth=2)

  wk_min_norm = skewnorm.fit(merged['temp_wk_min'])
  axs[0,1].plot(x, skewnorm.pdf(x, *wk_min_norm))
  axs[0, 1].hist(merged['temp_wk_min'], bins=20, density=True)
  axs[0, 1].set_title(f'Latest {n_days} day minimum temperature')
  axs[0, 1].set_xlabel('Temperature (°C)')
  axs[0, 1].axvline(current_weather_stats['temp_min'], color='red', linestyle='dashed', linewidth=2)

  wk_max_norm = skewnorm.fit(merged['temp_wk_max'])
  axs[1,0].plot(x, skewnorm.pdf(x, *wk_max_norm))
  axs[1, 0].hist(merged['temp_wk_max'], bins=20, density=True)
  axs[1, 0].set_title(f'Latest {n_days} day maximum temperature')
  axs[1, 0].set_xlabel('Temperature (°C)')
  axs[1, 0].axvline(current_weather_stats['temp_max'], color='red', linestyle='dashed', linewidth=2)

  axs[1, 1].hist(merged['rain_wk_avg'], bins=20)
  axs[1, 1].set_title(f'Latest {n_days} day average rainfall')
  axs[1, 1].set_xlabel('Rain (mm)')
  axs[1, 1].axvline(current_weather_stats['avg_daily_rain'], color='red', linestyle='dashed', linewidth=2)

  # Adjust the spacing between subplots
  fig.tight_layout()
  fig.suptitle(f'Säsong för {swe_name}.', fontsize=16)

  plt.show()