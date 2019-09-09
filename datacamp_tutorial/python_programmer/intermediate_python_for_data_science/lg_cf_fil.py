# Logic, Control Flow and Filtering
import numpy as np

def p(param):
    print(param)


# Comparison of booleans
p(True == False)

# Comparison of integers
p(-5 * 15 != 75)

# Comparison of strings
p("pyscript" == "PyScript")

# Compare a boolean with an integer
p(True == 1)

x = -3 * 6
p(x >= -10)
y = "test"
p("test" <= y)
p(True > False)


my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])
print(my_house >= 18)
print(my_house <your_house )

my_kitchen = 18.0
your_kitchen = 14.0
print(my_kitchen > 10 and my_kitchen < 18)
print(my_kitchen < 14 or my_kitchen > 17)
print(my_kitchen*2 < your_kitchen*3)

print(np.logical_or(my_house > 18.5 , my_house < 10))
print(np.logical_and(my_house < 11 , your_house < 11))

room = "bed"
area = 14.0

# if-elif-else construct for room
if room == "kit" :
    print("looking around in the kitchen.")
elif room == "bed":
    print("looking around in the bedroom.")
else:
    print("looking around elsewhere.")

# if-elif-else construct for area
if area > 15 :
    print("big place!")
elif area > 10 :
    print("medium size, nice!")
else:
    print("pretty small.")
