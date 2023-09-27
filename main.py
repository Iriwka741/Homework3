#print("Homework3 Banul")

#1.Користувач вводить із клавіатури номер дня тижня (1-7). Необхідно вивести на екран назви дня тижня.

try:
    day = int(input())
    if day == 1:
        print("Monday")
    elif day == 2:
        print("Tuesday")
    elif day == 3:
        print("Wednesday")
    elif day == 4:
        print("Thursday")
    elif day == 5:
        print("Friday")
    elif day == 6:
        print("Saturday")
    elif day == 7:
        print("Sunday")
    else:
        print("You entered incorrect data")

except ValueError as error:
    print("You entered incorrect data")
