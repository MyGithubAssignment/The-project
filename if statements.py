age=int(input("enter the age of person" ))
if age>18:
    print("eligible")
    print("join us today")
else:
    print("not eligible")
    print("come next year")


x=int(input("enter the marks"))
if x<100 and x>90:
    print("A")
elif x>70 and x<=90:
    print("B")
elif x>40 and x<=70:
    print("C")
else:
    print("FAIL")

z=int(input("enter the integers:"))

if z%2==0:
    print("even")
else:
    print("odd")

b=input("enter the name:")
print("name")


var=input("enter the name")
if var.isalpha()==True:
    print("valid name")
else:
    print("invalid name")