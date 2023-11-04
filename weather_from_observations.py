from weather_from_coordinates import weather_from_coordinates
import pandas as pd

def weather_from_observations(observations_df, n_days: int, mushroom_name: str):
  """
  Get weather data for observations based on coordinates and date range.
  
  Args:
      observations_df (pd.DataFrame): DataFrame containing observation data.
      n_days (int): Number of days to fetch weather data for.
      mushroom_name (str): Name of the mushroom species.
      
  Returns:
      pd.DataFrame: DataFrame containing weather data for the specified observations.
  """
  print("Running")
  weather = pd.DataFrame()

  for index, row in observations_df.iterrows():

    if index < len(weather):  # Only get weather data for rows that don't already have it
      continue

    if index % 100 == 0:
      print(f'Getting weather data for row {index} of {len(observations_df)}')

    end_date = row['Date']
    start_date = end_date - pd.Timedelta(days=n_days)
    lon = row['Longitude']
    lat = row['Latitude']
    
    response = weather_from_coordinates(lon, lat, start_date, end_date)

    if response.empty:
      weather.to_csv(f'weather/{mushroom_name}_incomplete.csv', index=True)
      print(f"Weather fetching incomplete, missing {len(observations_df) - len(weather)} rows. \n")
      return weather

    wth = dict(response)
    # Append the data as a new row to the weather DataFrame and reassign the result
    weather = weather._append(wth, ignore_index=True)
  return weather

if __name__ == '__main__':
  weather_from_observations(pd.read_csv('observations/semilanceata.csv', delimiter=';', engine='python'), 7, 'semilancie')