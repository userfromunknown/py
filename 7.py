print("EXCEPTION HANDLING")
try:
 number1, number2 = eval(input("Enter two numbers separated by a comma: "))
 result = number1 / number2
 print("Result is", result)
 if(number1==0):
 raise RuntimeError()
except ZeroDivisionError:
 print("Division by Zero")
except SyntaxError:
 print("A comma may be Missing in the Input")
except RuntimeError:
 print("May be Meaningless")
except:
 print("Something Wrong in the Input")
else:
 print("No Exceptions")
finally:
 print("\t******")