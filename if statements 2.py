var=input("enter the name")
if var.isalpha()==True:
    print("valid name")
else:
    print("invalid name")

var=input("enter the mobile numbers:")
if var.isnumeric()==True:
    print("valid numbers")
else:
    print("invalid numbers")

age,var=input("enter the age:")
if age>18:
    print("eligible")
else:
    print("not eligible")
if var.isdigit()==True:
    print("valid age")
else:
    print("invalid age")

