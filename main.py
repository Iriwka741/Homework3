#print("Homework3 Banul")

#1.Користувач вводить із клавіатури номер дня тижня (1-7). Необхідно вивести на екран назви дня тижня.

#try:
    #day = int(input())
    #if day == 1:
        #print("Monday")
    #elif day == 2:
        #print("Tuesday")
    #elif day == 3:
        #print("Wednesday")
    #elif day == 4:
        #print("Thursday")
    #elif day == 5:
        #print("Friday")
    #elif day == 6:
        #print("Saturday")
    #elif day == 7:
        #print("Sunday")
    #else:
        #print("You entered incorrect data")

#except ValueError as error:
    #print("You entered incorrect data")
################################################
#2. Користувач вводить два числа. Визначити, чи рівні ці числа, і, якщо ні, вивести їх на екран у порядку зростання

#try:
    #num1 = int(input("Enter first number: "))
    #num2 = int(input("Enter second number "))

    #if num1!= num2 and num1 < num2:

        #print(str(num1) + " " + str(num2))

   # elif num1 != num2 and num1 > num2:

        #print(str(num2) + " " + str(num1))

   # else:

        #print("num1 = num2")
#finally:
    #print("End of calculation")
    ###########################################

#3.Користувач вводить два числа та матем дію: + - * або / Залежно від введеної матем дії вивести результат

try:

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second  number: "))
    user_select = str(input("Enter match action: "))
    math_action = ("Enter math action")
    match math_action:
        case '+':
            print("num1 + num2")
        case '-':
            print("num1 - num2")
        case '*':
            print("num1 * num2")
        case '/':
            print("num1 / num2")
        case _:
            print("you entered something wrong")
except Exception as e:
    print(f"Error: {e}")

