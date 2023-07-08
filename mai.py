import pandas as pd
import numpy as np
import math

df = pd.read_excel("kvgwerwr.xlsx")

print(len(df))

key = df.iloc[1,15]
print(key)
