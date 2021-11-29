import pandas as pd

def file_subido(file):
    frame = pd.read_excel(file)
    print(frame.head())
    return frame