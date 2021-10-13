from numpy import load
import pandas as pd


def get_table(filename):
    """[get pandas table from (un)compressed npz/npy format]

    Args:
        filename (string): [location string of the file(name)]

    Returns:
        [dataframe]: [pandas dataframe containing the numpy array(s)]
    """
    data = load(filename)
    lst = data.files
    df = pd.Dataframe()
    for item in lst:
        df[item] = data[item]
    print(df)
    return df

test_df = pd.read_csv("metadata.csv")
print(test_df["File Location"][0])