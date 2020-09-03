a = input("give a number: ")
a = int(a)
b =1 
c = 0
while b<=a:
    c = c + b
    b = b + 1
average_float = c/(b-1)
print("Result: ", average_float) 