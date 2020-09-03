# calculate the area and circumference of a circle from its radius
# Step 1: Promt for a radius
# Step 2: Apply the area formula
# Step 3: Print out the results

import math

radius_str = input("2")
radius_int = int("2")

circumference = 2 * math.pi * radius_int
area = math.pi * (radius_int ** 2)

print ("The cirumference is:" , circumference,   \
       " and the area is:" ,area)
