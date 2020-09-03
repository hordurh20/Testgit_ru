days_str = input("Number of days after 9/25/09: ")
days_str = int(days_str) #convert the string to an integer
miles = (days_str * 38241 * 24) + 16637000000
miles = float(miles)
kilometers = (days_str * 38241 * 24 * 1.609344) + (16637000000 * 1.609344)
kilometers = float(kilometers)
AU = ((days_str * 38241 * 24)/ 92955887.6) + (16637000000 / 92955887.6)
AU = float(AU)

print("Miles from the sun:", round(miles))
print("Kilometers from the sun:", round(kilometers))
print("AU from the sun:", round(AU))
