def add(a , b):
    return a + b


def subtract(a , b):
    return a - b


def multiply(a , b):
    return a * b


def divide(a , b):
    if b == 0:
        return "Division by 0 is not allowed"
    return a / b

a = int(input("enter a number :"))
operation = input("enter your operation between + - * / :")
b = int(input("enter another number :"))


if operation == '+':
    print((a, b))
elif operation == '-':
    print(subtract(a, b))
elif operation == '*':
    print(multiply(a , b))
elif operation == '/':
    print(divide(a, b))
else:
    print("your operation isn't between + - * /")
