# !/usr/bin/env python3

def admin_login(username, password):
    # your code here
    if (username == "admin" or username =="ADMIN") and password =="12345":
        return "Access granted"
    else:
        return "Access denied" 
# print(admin_login("admin", 12345))

def hows_the_weather(temperature):
    # your code here
    if temperature <40:
        return "It's brisk out there!"
    elif temperature >=40 and temperature<=65:
        return "It's a little chilly out there!"
    elif temperature >85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"
    

def fizzbuzz(num):
    # your code here
    if num % 3 ==0 and num % 5 != 0:
        return "Fizz"
    elif num %3 != 0 and num % 5 == 0:
        return "Buzz" 
    elif num %3 ==0 and num % 5 == 0:
        return "FizzBuzz"
    else:
        return num
# print(fizzbuzz(11))

#  Write a method `calculator` that takes three arguments: an operation and two
#   numbers. If the operation is one of the following: `+`, `-`, `*`, or `\`,
#   return the value of calling the operation on the two numbers. Otherwise,
#   output a message saying "Invalid operation!" and return `nil`.
def calculator(operation, num1, num2):
    # your code here
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        print("Invalid operation!")

# print(calculator("d", 2,3))