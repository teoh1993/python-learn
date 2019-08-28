# 不想混吃等死
import pandas as pd

# trying to get data from sheet

# cr = csv.reader('01.csv')
df01 = pd.read_csv('01.csv')
param01 = df01.head()

less_then_five = param01[param01.frequency < 5]
print(less_then_five)

letter_param = param01.letter[param01.frequency < 5]
print(letter_param)

b = param01[param01.letter == 'B']
print(b)

print(param01.letter_index);print(param01.frequency)
