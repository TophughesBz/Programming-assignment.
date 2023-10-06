year =int(input("Enter your year of choice :"))

indicator = year % 4
if( indicator== 0):
     print("This is a leap year!!")
else:
     print("This is not a leap year!!")

