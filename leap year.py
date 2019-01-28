a=int(input("enter the leap year:"))
if a%400==0:
    print("a is a leap year")
elif a%100==0:
    print("a is not year")
elif a%4==0:
    print("a is a leap year")
else:
    print("a is not leap year")