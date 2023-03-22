# Calculator


print("Choose operation to be executed")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

operation = input("Enter choice:")

if operation == "1":
    num1 = float(input("Enter first number:"))
    num2 = float(input("Enter second number"))
    print(int(num1) + int(num2))
elif operation == "2":
    num1 = float(input("Enter first number:"))
    num2 = float(input("Enter second number:"))
    print(int(num1) - int(num2))
elif operation == "3":
    num1 = float(input("Enter first number:"))
    num2 = float(input("Enter second number:"))
    print(int(num1) * int(num2))
elif operation == "4":
    num1 = float(input("Enter first number:"))
    num2 = float(input("Enter second number:"))
    print(int(num1) / int(num2))
else:
    print("Blank space")




git