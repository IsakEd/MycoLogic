import pandas as pd
from dateutil import parser

def load_observations(file):

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
        
    df = df.drop(columns=['TaxonId', 'SortOrder', 'Scientific', 'Name',
    'Source', 'Observer', 'NotRedisc', 'Removed', 'Quantity', 'Accuracy'])

    df['Time'] = df['Time'].apply(lambda x: parser.parse(x))
    # Strip times from 'Time' column
    df['Date'] = df['Time'].apply(lambda x: x.date())


    return df