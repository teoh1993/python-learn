
print("\n ############################################# Python List #############################################\n")
# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Adapt list areas
areas = ["hallway", hall, "kitchen", kit, "living room", liv, "bedroom", bed, "bathroom", bath]

# Print areas
print(areas)

# house information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom", bed],
         ["bathroom", bath]]

# Print out house
print(house)

# Print out the type of house
print(type(house))

# Print out second element from areas
print(areas[1])

# Print out last element from areas
print(areas[-1])

# Print out the area of the living room
print(areas[-5])

# Sum of kitchen and bedroom area: eat_sleep_area
eat_sleep_area = areas[3]+areas[7]

# Print the variable eat_sleep_area
print(eat_sleep_area)

# Use slicing to create downstairs
downstairs = areas[0:6]

# Use slicing to create upstairs
upstairs = areas[6:10]

# Print out downstairs and upstairs
print("downstairs"+str(downstairs))
print('upstairs'+str(upstairs))

# Alternative slicing to create downstairs
downstairs1 = areas[:6]

# Alternative slicing to create upstairs
upstairs1 = areas[-4:]

# Print out downstairs and upstairs
print("downstairs1"+str(downstairs1))
print('upstairs1'+str(upstairs1))

x = [["a", "b", "c"],
     ["d", "e", "f"],
     ["g", "h", "i"]]
print(x[2][0])
print(x[2][:2])


# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correct the bathroom area
areas[-1] = 10.50

# Change "living room" to "chill zone"
areas[4] = 'chill zone'

# Add poolhouse data to areas, new list is areas_1
areas_1 = areas + ["poolhouse", 24.5]

# Add garage data to areas_1, new list is areas_2
areas_2 = areas_1 + ['garage', 15.45]

# Create areas_copy
areas_copy = list(areas)

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)
print(areas_copy)

print("\n #######################################################################################################\n")

