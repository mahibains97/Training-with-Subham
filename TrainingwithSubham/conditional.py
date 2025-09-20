day_of_week = input("PLease enter the day of week: ").lower()
print(day_of_week)

if day_of_week == "sunday" or day_of_week == "saturday":
    print("I'll learn the DevOps")
else:
    print("I'll practice the DevOps")

num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))

choice = input("pleae enter the oprator: (Options +, -, *, /, %)")

if choice == "+":
    sum_of_num = num1 + num2
    print("Addition: ", sum_of_num)
elif choice == "-":
    sub_of_num = num1 - num2
    print("Subtraction: ", sub_of_num)
elif choice == "*":
    mul_of_num = num1 * num2
    print("Multiplicaton: ", mul_of_num)
elif choice == "/":
    div_of_num = num1 / num2
    print("Division: ", div_of_num)
elif choice == "%":
    rem_of_num = num1 % num2
    print("Remainder: ", rem_of_num)
else:
    print("Invalid oprator")
    