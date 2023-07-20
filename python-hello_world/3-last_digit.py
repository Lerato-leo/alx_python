import random
number = random.randint(-10000, 10000)

Last_digit = int(str(number)[-1])

if Last_digit > 5:
    print("Last digit of " + str(number) + " is " + str(Last_digit)  + " and is greater than 5")
elif Last_digit == 0:
    print("Last digit of " + str(number) + " is " + str(Last_digit)  + " and is 0")
elif Last_digit < 6 and Last_digit != 0 :
    print("Last digit of " + str(number) + " is " + str(Last_digit)  + " and is less than 6 and not 0")