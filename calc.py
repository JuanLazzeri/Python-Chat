n1 = int(input("Enter a number: "))
n2 = int(input("Enter other number: "))

operation = str(input("Choose between sum, subtraction, multiplication and division: "))

def sum(n1,n2):
    return n1+n2
def subtraction(n1,n2):
    return n1-n2
def multiplication(n1,n2):
    return n1*n2
def division(n1,n2):
    return n1/n2

if operation == "sum":
    print("Result: ", sum(n1,n2))
elif operation == "subtraction":
    print("Result: ",subtraction(n1,n2))
elif operation == "multiplication":
    print("Result: ",multiplication(n1,n2))
elif operation == "division":
    print("Result: ",division(n1,n2))
else:
    print("Invalid operation")