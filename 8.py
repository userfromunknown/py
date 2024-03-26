class Area:
 def circle(self,r):
 print("Area of the Circle is :",3.14*r*r)
 def square(self,a):
 print("Area of the Square is :",(a*a))
 def rectangle(self,l,b):
 print("Area of the Rectangle is :",(l*b))
print("Program Using Class")
obj=Area()
radius=float(input("Enter the radius :"))
obj.circle(radius)
side=int(input("\nEnter the side of a Square:"))
obj.square(side)
length=int(input("\nEnter the length of a rectangle:"))
width=int(input("Enter the width of a rectangle:"))
obj.rectangle(length,width)