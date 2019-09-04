# 不想混吃等死
import pandas as pd
from matplotlib import pyplot as plt

# trying to get data from sheet
df01 = pd.read_csv('catdog.csv');
hours = df01.head()
print(hours);



# plt.bar(hours.officer, hours.avg_hours_worked,yerr=hours.std_hours_worked)

# plt.show()



# Plot the number of hours spent on desk work
plt.bar(hours.officer, hours.avg_hours_worked, label='avg_hours_worked')

# Plot the hours spent on field work on top of desk work
plt.bar(hours.officer,hours.std_hours_worked,bottom=hours.avg_hours_worked, label="std_hours_worked")

# Add a legend
plt.legend()
# Display the plot
plt.show()

