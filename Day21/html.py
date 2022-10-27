import pandas as pd
pd.read_html('data.html', index_col=0, parse_dates=['IND_DAY'])