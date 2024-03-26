import re
print("\t\t Program for String Handling and Regular Expressions”)
input_text = """
Some example Emails are:
Valid:
professor123@gmail.com
alan2004@gmail.com
Invalid:
unknown@gmail
googlegmail.com
"""
pattern = r'\S+@\S+\.\S+'
emails = re.findall(pattern, input_text)
if emails:
 print("Found email addresses:")
 for email in emails:
 print(email)
else:
 print("No email addresses found.")
class py_reverse:
 def revr(self, strs):
 sp=strs.split()
 sp.reverse()
 res=" ".join(sp)
 return res
str1=input("Enter a string with 2 or more words: ")
print("Reverse of string word by word: \n",py_reverse().revr(str1));