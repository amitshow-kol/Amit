print("************************CALCULATOR*****************************")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("\n")
print("Enter 1 for Addition\nEnter 2 for Division\nEnter 3 for Multuiplication\nEnter 4 for Substraction")


Enter_num=int(input("Choose number from 1 to 4: "))

if Enter_num==1:
    print(f"Addition of {a} & {b} is {a+b}")

elif Enter_num==2:
    print(f"Division of {a} & {b} is {a/b}")

elif Enter_num==3:
    print(f"Multiplication of {a} & {b} is {a*b}")

elif Enter_num==4:
    print(f"Substraction of {a} & {b} is {a-b}")

else:
    print()

