import pandas as pd

dtypes = {'POP': 'float32', 'AREA': 'float32', 'GDP': 'float32'}
# df = pd.read_csv('data.csv', index_col=0, na_values=('missing'))
df = pd.read_csv('data.csv', index_col=0, dtype=dtypes, parse_dates=['IND_DAY'])
print(df.dtypes)
print(df['IND_DAY'])
df.to_csv('formatted-data.csv', date_format='%B %d, %Y')