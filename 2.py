print("CONTROL FLOW STATEMENTS")
print("Finding Greatest Number")
a=int(input("Enter the Value of A:"))
b=int(input("Enter the Value of B:"))
c=int(input("Enter the Value of C:"))
if a>b and a>c: #A greater than B and Greater than C
 print("A is Greatest Among All")
elif b>a and b>c: #B greater than A and Greater than C
 print("B is Greatest Among All")
elif c>a and c>b: #C greater than A and Greater than B
 print("C is Greatest Among All")
else: #A,B,C are Equal
 print("All the values are Equal")