# 不想混吃等死
import pandas as pd
from matplotlib import pyplot as plt

# trying to get data from sheet
df01 = pd.read_csv('01.csv');df02 = pd.read_csv('02.csv');df03 = pd.read_csv('03.csv')
param01 = df01.head();param02 = df02.head();param03 = df03.head()
print(param01);print(param02);print(param03)
print(plt.style.available)

# plt.style.use('fivethirtyeight')
plt.style.use('ggplot')
# plt.style.use('seaborn')
# plt.style.use('default')

plt.xlabel('letter_index')
plt.ylabel('frequency')
plt.title('cool title', fontsize=40)
plt.plot(param01.letter_index, param01.frequency, label='label01', color='tomato', linewidth=1, linestyle='-', marker='x')
plt.plot(param02.letter_index, param02.frequency, label='label02', color='orange', linewidth=1, linestyle=':', marker='s')
plt.plot(param03.letter_index, param03.frequency, label='label03', color='seagreen', linewidth=1, linestyle='-.', marker='d')

# error
# plt.text(param01.letter_index, param01.frequency, 'Text Message')
# plt.legend(color='green')

plt.legend()
plt.show()

