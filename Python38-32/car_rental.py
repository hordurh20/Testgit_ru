print ("Welcome to car rentals!")
rental_code = input("Would you like to continue (y/n)? ")

while rental_code == "y":


    customer_code = str(input("Customer code (b or d): "))
    rental_time = int(input("Number of days: "))
    base_charge_b = float(rental_time * 40)
    base_charge_d = float(rental_time * 60)

    odometer_start = int(input("Odometer reading at the start: "))
    odometer_end = int(input("Odometer reading at the end: "))
    total_miles = int(odometer_end - odometer_start)

    print("Miles driven: ", total_miles)
    mile_charge = int()
    if customer_code == "b":
        mile_charge = total_miles * 0.25

    if customer_code == "d":
        average_miles = int(total_miles) / int(rental_time)
        if average_miles <= 100:
            total_miles = 0
        elif average_miles > 100:
            mile_charge = (total_miles - (100 * rental_time)) * 0.25
        

    amount_due_b = float(base_charge_b + mile_charge)
    amount_due_b = round(amount_due_b, 1)

    amount_due_d = float(base_charge_d + mile_charge)
    amount_due_d = round(amount_due_d, 1)


    if customer_code == "b":
         print("Amount due:" , amount_due_b)
    elif customer_code == "d":
        print ("Amount due:" , amount_due_d)

    rental_code = input("Would you like to continue (y/n)? ")

    if rental_code == "n":
        break

    



    
