#importing module in our program
import maths
print("Mathematical Operations Using Module")
# Getting user input
num1=int(input("Enter the First Value:"))
num2=int(input("Enter the Second Value:"))
#Calling functions from the module
print("Sum of two numbers is:",maths.sum(num1,num2))
print("Difference of two numbers is:",maths.diff(num1,num2))
print("Product of two numbers is:",maths.product(num1,num2))
print("Division of two numbers (Quotient) is:",maths.quo(num1,num2))