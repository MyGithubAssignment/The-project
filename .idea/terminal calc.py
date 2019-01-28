
a=float(input("enter the intergers number of a:"))
b=float(input("enter the integers number of b:"))
sum=a+b
product=a*b
difference=a-b
quiotent=a/b
module=a%b
print("sum=%f",sum)
print("product=%f",product)
print("difference=%f",difference)
print("quiotent=%f",quiotent)
print("module=%f",module)


a=int(input("enter the leap year:"))
if a%400==0:
    print("a is a leap year")
elif a%100==0:
    print("a is not year")
elif a%4==0:
    print("a is a leap year")
else:
    print("a is not leap year")

length=float(input("enter the value of length:"))
breadth=float(input("enter the value of breadth:"))
if length==breadth:
    print("it is square")
else:
    print("it is rectangle")