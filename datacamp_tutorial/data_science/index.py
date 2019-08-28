# 不想混吃等死
import pandas as pd

# trying to get data from sheet

# cr = csv.reader('ransom.csv')
df = pd.read_csv('ransom.csv')
param = df.head()
# print(df)

print(param['letter'])
print(param.letter)

# print(df.info())



