length = int(input("Input the length of series: "))


#erum med +4 og -4
variable_1 = -2
variable_2 = 0
    
for x in range(1, length+1):
    if x%2==1:
        variable_1+=4
        print(variable_1)
    else:
        variable_2-=4
        print(variable_2)
        
        

the_sum = variable_1 + variable_2

print('Sum:', the_sum)

length = int(input("Input the length of series: "))

var = 0
sign = -1
for x in range(1, length+1):
    sign*=-1   
    ans = 2*x*sign
    var+= ans
    print(ans)
print('Sum:', var)
