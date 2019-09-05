# 不想混吃等死
import pandas as pd
from matplotlib import pyplot as plt

# trying to get data from sheet
df01 = pd.read_csv('weight.csv')
df02 = pd.read_csv('sample_weight.csv')

arr1 = arr2 = []
for each1 in df01.values:
    arr1.append(each1[0])

for each2 in df02.values:
    arr2.append(each2[0])

# range - sets the minimum and maximum datapoints that we will include in our histogram.
# bins - sets the number of points in our histogram.
plt.hist(arr1, bins=5, range=(0,70), density=True)
plt.hist(arr2, bins=5, range=(5,25), density=True)

# plt.hist(arr1)
# plt.hist(arr2)

# Add labels
plt.xlabel('Puppy Weight (lbs)')
plt.ylabel('Number of Puppies')

# Display
plt.show()

