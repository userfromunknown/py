# Multiplication table Using for loop
print("\n\nMultiplication Table Using For loop ")
# Reading the input 
num = int(input("\nEnter the value for Multiplication Table: ")) 
n = int(input("\nEnter the Limit: ")) 
i = 1
# using for loop to iterate multiplication table n times 
print("\n\nMultiplication Table:")
for i in range(1, n+1):
 print(i,'x',num,'=',num*i)
