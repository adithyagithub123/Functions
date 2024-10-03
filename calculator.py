def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def division(a,b):
    return a/b

print("Please select the opperation ")
print("1. Addition")
print("2.Subtraction")
print("3.Multiply")
print("4.Divide")

choice = int(input("Please enter your choice 1/2/3/4 : "))

num1 = int(input("Enter the first number :"))
num2 = int(input("Enter the second number :"))

if choice == 1 :
    print("total is ", add(num1,num2))

elif choice == 2 :
    print("Difference is ", subtract(num1 , num2))

elif choice == 3 :
    print("The product is ", multiply(num1 , num2))

elif choice == 4 :
    print("The quotient is ", division(num1 , num2))

else :
    print("Invalid input !")
