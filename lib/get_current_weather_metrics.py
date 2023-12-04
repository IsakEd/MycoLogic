import requests as re
import json
import pandas as pd

def get_current_weather_metrics(lat, lon, history_days):
  endpoint = f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=temperature_2m_max,temperature_2m_mean,temperature_2m_min,rain_sum&timezone=Europe%2FBerlin&past_days={history_days - 1}&forecast_days=1'
  response = re.get(endpoint)
  data = json.loads(response.text)
  temp_max = max(data['daily']['temperature_2m_max'])
  temp_min = min(data['daily']['temperature_2m_min'])
  temp_mean = sum(data['daily']['temperature_2m_mean'])/history_days
  avg_daily_rain = sum(data['daily']['rain_sum'])/history_days
  weather_dict = {'temp_max': temp_max, 'temp_min': temp_min, 'temp_mean': temp_mean, 'avg_daily_rain': avg_daily_rain}
  return weather_dict
  


if __name__ == '__main__':
  print(get_current_weather_metrics(18.068580627441406, 59.32933776855469, 14))