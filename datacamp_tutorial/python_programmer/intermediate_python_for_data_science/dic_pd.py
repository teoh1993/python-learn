# Import pandas as pd
import pandas as pd

# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# Get index of 'germany': ind_ger
ind_ger = countries.index('germany')

# Use ind_ger to print out capital of Germany
print(capitals[ind_ger])

# From string in countries and capitals, create dictionary europe
europe = { 'spain':'madrid', 'france':'paris', 'germany':'bann', 'norway':'oslo' , 'australia':'vienna'}

# Print europe
print(europe)
print(europe.keys())

# Print out value that belongs to key 'norway'
print(europe['norway'])

# Add italy to europe
europe['italy'] = 'rome'

# Print out italy in europe
print('italy' in europe)

# Add poland to europe
europe['poland'] = 'warsaw'

# Print europe
print(europe)
europe['germany'] = 'berlin'
del(europe['australia'])
print(europe)

#############################################################################################
europe2 = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }
# Print out the capital of France
print(europe2['france'])

# Create sub-dictionary data
data= {}
data['capital'] = 'rome'
data['population'] = 59.83

# Add data to europe under key 'italy'
europe2['italy'] = data

# Print europe
print(europe2)

#############################################################################################

# Build cars DataFrame
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }
cars = pd.DataFrame(dict)
print(cars)

# Definition of row_labels
row_labels = ['US', 'AUS', 'JAP', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index = row_labels

# Print cars again
print(cars)

# Import the cars.csv data: cars
cars_csv = pd.read_csv('cars.csv', index_col=0)

# Print out cars
print(cars_csv)
print(type(cars_csv['country']))
print(cars['country'])
print(type(cars_csv[['country']]))
print(cars[['country']])

print(cars[['country','drives_right']])

# Print out first 3 observations
print(cars[0:3])

# Print out fourth, fifth and sixth observation
print(cars[3:7])

# Print out observation for Japan
print(cars.loc['JAP'])

# Print out observations for Australia and Egypt
print(cars.loc[['AUS','JAP']])
print(cars.iloc[[4,5], [1,2]])

# It's also possible to select only columns with loc and iloc.
# In both cases, you simply put a slice going
# from beginning to end in front of the comma:
# cars.loc[:, 'country']
# cars.iloc[:, 1]
# cars.loc[:, ['country','drives_right']]
# cars.iloc[:, [1, 2]]
