import pandas as pd

def load_file():
    data=pd.read_csv("Data_sets\\Global YouTube Statistics.csv",encoding='latin1')
    return data