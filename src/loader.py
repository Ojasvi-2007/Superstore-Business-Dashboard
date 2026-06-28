import pandas as pd


def load_data(path):
    df = pd.read_excel(path)

    df["Order Date"] = pd.to_datetime(df["Order Date"])
    df["Ship Date"] = pd.to_datetime(df["Ship Date"])
    return df