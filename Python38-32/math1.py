import math
radius_str = input("Enter the radius of your circle: ")
radius_str #what is the value associated with radius_str
radius_int = int(radius_str) #convert the string to an integer
radius_int #check the value of the integer
int(radius_str) #what does int() return without assignment (=)
radius_str # int() does not modify radius_str!!
math.pi
circumference = 2 * math.pi * radius_int
area = math.pi * radius_int ** 2
math.pi * radius_int ** 2
print ("Circumference: ", circumference, ", area: ", area)
