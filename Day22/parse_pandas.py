from ast import parse
from operator import index
import pandas as pd

# df = pd.read_csv("hrdata.csv", index_col='Name', parse_dates=['Hire Date'])
df = pd.read_csv('hrdata.csv', 
    index_col='Employee', 
    parse_dates=['Hired'], 
    header=0,
    names=['Employee', 'Hired', 'Salary', 'Sick Days'])
print(df)