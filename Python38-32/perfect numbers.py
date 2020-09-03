

number_str = int(input("Please enter a number here to check:"))

divisor_int = 1
sum_of_divisors_int = 0
while divisor_int < number_str:
    if number_str % divisor_int == 0:
        sum_of_divisors_int = sum_of_divisors_int + divisor_int
    divisor_int = divisor_int + 1


if number_str == sum_of_divisors_int:
    print(number_str, "is perfect")
else:
    print(number_str, "is not perfect")
