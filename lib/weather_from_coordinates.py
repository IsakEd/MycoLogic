import requests as re
import json
import pandas as pd 
import time

def weather_from_coordinates(lon, lat, start_date, end_date):
  """
  Returns the weather at the given coordinates.
  """
  endpoint = f'https://archive-api.open-meteo.com/v1/archive?latitude={lat}&longitude={lon}&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min,temperature_2m_mean,rain_sum,windspeed_10m_max&windspeed_unit=ms&timezone=Europe%2FBerlin'
  
  
  try:
    response = re.get(endpoint)
    data = json.loads(response.text)
    df = pd.DataFrame(data)

  except:
    if "Minutely" in response.text:
      print('Error: Could not get weather data from the API. Waiting 1 minute and trying again.')
      time.sleep(60+1)
      response = re.get(endpoint)
      data = json.loads(response.text)
      df = pd.DataFrame(data)

    elif "Hourly" in response.text:
      print('Error: Could not get weather data from the API. Waiting 1 hour and trying again.')
      time.sleep(60*60+1)
      response = re.get(endpoint)
      data = json.loads(response.text)
      df = pd.DataFrame(data)

    else:
      print('Unknown error \n')
      print(response.text)
      time.sleep(60+1)
      response = re.get(endpoint)
      data = json.loads(response.text)
      return pd.DataFrame()


  return df.daily

if __name__ == '__main__':
  print(weather_from_coordinates(18.068580627441406, 59.32933776855469, '2023-10-01', '2023-10-20'))