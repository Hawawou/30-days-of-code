import pandas as pd
df = pd.read_json('data.json', orient='index', convert_dates=['IND_DAY'])
print(df)