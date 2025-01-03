def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b!=0:
        return a/b
    else:
        return "Error: Division by zero is not possible" 
def mod(a,b):
    if b!=0:
        return a%b
    else:
        return "Error: Division by zero is not possible"
def power(a,b):
    return a**b
def floor_div(a,b):
    if b!=0:
        return a//b
    else:
        return "Error: Division by zero is not possible"
def sqrt(a):
    return a**0.5

def calculator():
    print("Enter two numbers:")
    a = float(input())
    b = float(input())
    print("Enter the operation you want to perform:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")
    print("7. Floor Division")
    print("8. Square root")
    choice = int(input())
    if choice == 1:
        print("Result: ",add(a,b))
    elif choice == 2:
        print("Result: ",sub(a,b))
    elif choice == 3:
        print("Result: ",mul(a,b))
    elif choice == 4:
        print("Result: ",div(a,b))
    elif choice == 5:
        print("Result: ",mod(a,b))
    elif choice == 6:
        print("Result: ",power(a,b))
    elif choice == 7:
        print("Result: ",floor_div(a,b))
    elif choice == 8:
        print("Result: ",sqrt(a))
    else:
        print("Invalid choice")
