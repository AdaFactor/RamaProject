import pandas as pd

df = pd.read_csv('./list_name.csv')
cols = [c for c in df.columns]
print(df)