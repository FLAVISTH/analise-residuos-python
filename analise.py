import pandas as pd

df = pd.read_csv('Municipal-Diagnostico.csv', sep=';')

print(df.head())
print(df.columns)