import pandas as pd
from dateutil import parser

def load_observations(file, columns: list = []):

    """
    Load mushroom observation data.

    Args:
        file (str): Path to the CSV file.
        
    Returns:
        pd.DataFrame: The cleaned DataFrame.
    """

    try:
        df = pd.read_csv(file, delimiter=';', engine='python', on_bad_lines="skip", quoting=3)
    except:
        return pd.DataFrame()
        
    if columns:
        df = df[columns]

    if 'Date' not in df.columns:
        df['Time'] = df['Time'].apply(lambda x: parser.parse(x))
        # Strip times from 'Time' column
        df['Date'] = df['Time'].apply(lambda x: x.date())


    return df