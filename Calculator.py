import math

class Calculator:
    def divide(a,b):
        return a / b
    
    def add(a,b):
        return a + b
    
    def subtract(a,b):
        return a - b
    
    def multiply(a,b):
        return a * b
    
    def square(a):
        return a * a
    
    def cube(a):
        return a * a * a
    
    def sqrt(a):
        return math.sqrt(a)
    
    def factorial(a):
        return math.factorial(a)
    

print("Hello, this is the 8d function calculator suited for the needs of many students across the world.")
print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Square\n6. Cube\n7. Sqrt\n8. Factorial\n9. Exit\n")
while True:
 print("Select an option: ")
 option = int(input())

 if option == 1:
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    print(Calculator.add(a,b))

 if option == 2:
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    print(Calculator.subtract(a,b))

 if option == 3:
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    print(Calculator.multiply(a,b))

 if option == 4:
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    print(Calculator.divide(a,b))

 if option == 5:
    a = float(input("Enter the number: "))
    print(Calculator.square(a))

 if option == 6:
    a = float(input("Enter the number: "))
    print(Calculator.cube(a))

 if option == 7:
    a = float(input("Enter the number: "))
    print(Calculator.sqrt(a))

 if option == 8:
    a = int(input("Enter the number: "))
    print(Calculator.factorial(a))

 if option == 9:
    print("Thanks for using the calculator!")
    exit()