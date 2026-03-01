#Assignment Author: Liav Lugasi, ID: 213007271

#Question 2

import math

num = input("Type a number: ")

if num.isdigit() :
    num = int(num)

    if num > 0:
        num1 = num
        print(f" The number you typed is {num} and its sqrt is {math.sqrt(num1)}")

else:
    print("the number is not positive or int. ")
    str = input("Insert string: ")
    print(f"The reverse string is : {str[::-1]}")






#Question 3

num = input("Enter a number or a String: ")

if num.isdigit() :
    num = int(num)
    flag = False

    if num == 0 or num == 1:
        print (f"{num} is not a prime number.")

    elif num > 1:
        for i in range (2, num ):
            if (num % i) == 0:
                flag = True
                break

        if flag:
            print(f"{num} is not a prime number.")
            factorial = 1
            for i in range(1, num +1):
                factorial = factorial * i
            print(f"The factorial of {num} is {factorial}")

        else:
            print(f"{num} is prime")

else:
    if len(num) % 2 == 0:
        half = len(num) // 2
        f = num[half:]
        s = num[:half]
        rf = f[::-1]
        rs = s[::-1]
        print(f"The managed string is: {rs} {rf}")

    else:
        print (f"The managed string is {num[::-1]}")


#Qustion 4

import math

x = 0
y = 0
z = 0
d = 0

while d < 100:
    x += int(input("Insert the axis movement X: "))
    y += int(input("Insert the axis movement Y: "))
    z += int(input("Insert the axis movement Z: "))

    x2 = math.pow(x,2)
    y2 = math.pow(y, 2)
    z2 = math.pow(z,2)


    xyz = math.sqrt( x2 + y2 + z2)
    d = xyz

    print(f"The Robot is {d} from the starting point")


    if d > 100:
        print("The robot has moved too far! \n the distance has exceeded 100 units")
        break



#Question 5

t_hours = 0

with open("WorkerLog.txt", "a") as file:
    file.write("\n-----------------------------------\ndaily maintenance report:\n")

while True:
    name = input("Enter the name of the site (or end to finish): ")
    if name == "end":
        break

    hours = int(input(f"Enter the number of hours you worked on {name}: "))

    with open ("WorkerLog.txt", "a") as file:
        file.write(f"{name}: {hours} hours\n")

    t_hours += hours

with open ("WorkerLog.txt", "a") as file:
    file.write(f"Total hours you worked today: {t_hours}\n")
    file.write("-----------------------------------\n")



if t_hours > 8:
    print(f"Total hours you worked today: {t_hours}")
    x = f"Warning: you have exceeded 8 hours of work per day!\n"
    y = ("-----------------------------------\n")


    with open ("WorkerLog.txt" , "a") as file:
        file.write(x)
        file.write(y)
    print(x)



else:
    print(f"Total hours you worked today: {t_hours}")