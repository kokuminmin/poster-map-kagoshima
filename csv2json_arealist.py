import pandas as pd
import sys
import os

df = pd.read_csv('arealist.csv')
df.to_json('arealist.json', orient='records', force_ascii=False)