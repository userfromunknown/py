import os
print("FILE HANDLING PROGRAM IN PYTHON")
# Create a Directory
path = "Z:\Lab"
try:
 os.mkdir(path)
except OSError:
 print ("Creation of the directory %s failed" % path)
else:
 print ("Successfully created the directory %s " % path)
#Writing the content
file=open("Z:\Lab\sample.txt","w")
str1=input("Enter your String:")
file.write(str1)
file.close() 
#Reading the content
file=open("Z:\Lab\sample.txt","r")
print("File Content:\n",file.read())
file.close() 
# Remove the Directory
choice=int(input("Do you want to remove the directory press 1:"))
if(choice==1):
 os.remove("Z:\Lab\sample.txt")
 os.rmdir(path)
 print ("Successfully Deleted the directory %s " % path)
else:
 print ("Deletion of the directory %s failed" % path)
