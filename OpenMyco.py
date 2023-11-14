import pandas as pd

df = pd.read_csv("observations/semilanceata.csv", delimiter=';', engine='python', on_bad_lines="skip", quoting=3)

print(df)

print(df.shape)
print(df.columns)

# Make a new dataframe out of the columns we want
locations = df[['Accuracy', 'Latitude', 'Longitude']]
locations.to_csv('EarthEngine/locations.csv', index=False)
