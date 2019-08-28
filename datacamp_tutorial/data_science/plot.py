# 不想混吃等死
import pandas as pd
from matplotlib import pyplot as plt

# trying to get data from sheet
df01 = pd.read_csv('01.csv');df02 = pd.read_csv('02.csv');df03 = pd.read_csv('03.csv')
param01 = df01.head();param02 = df02.head();param03 = df03.head()
print(param01);print(param02);print(param03)

