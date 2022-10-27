import pandas as pd

# df = pd.read_excel('data.xlsx', sheet_name=0, index_col=0, parse_dates=['IND_DAY'])
df = pd.read_excel('data.xlsx', sheet_name='COUNTRIES', index_col=0, parse_dates=['IND_DAY'])
print(df)