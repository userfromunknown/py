import mysql.connector
#Connection to Mysql Database
connection=mysql.connector.connect(
 host='localhost',
 username='root', 
 password='vysya', 
 database='addressbook' 
 )
#Create Table if not Already Exists
cursor=connection.cursor()
cursor.execute(" Create Table If not Exists contacts(ID int AUTO_INCREMENT 
PRIMARY KEY,Name varchar(255) not null,Phno varchar(20),Email 
varchar(255))")
#Save Changes
connection.commit()
#Add Contact Details
def contact_details(name,phno,email):
 qry="insert into contacts(NAME,PHNO,EMAIL) values (%s,%s,%s)"
 cursor.execute(qry,(name,phno,email))
 connection.commit()
#Display Contact Details
def display_details():
 qry="Select *from contacts"
 cursor.execute(qry)
 details=cursor.fetchall()
 
 if not details:
 print("No Contact Details Found")
 else:
 print("Contact Details in a Database are:")
 for detail in details:
 print(detail)
#main program
print("\t\tMYSQL ADDRESSBOOK")
n=int(input("Enter no of Contact details: ")) 
for i in range (0,n): 
 print("\t\tADDRESSBOOK DETAILS: ",i+1)
 name=input("Enter your Name: ")
 phno=input("Enter your Phone Number: ")
 email=input("Enter your Email: ")
 contact_details(name,phno,email)
 
display_details()
#Close the Connection
cursor.close()
connection.close()
print("Connection Disconnected...")
