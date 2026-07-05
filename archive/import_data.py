import pandas as pd

def load_data(filename):

    df = pd.read_csv(filename)

    df.columns = [c.strip() for c in df.columns]

    print("\nDataset Loaded")

    print(df.head())

    return df