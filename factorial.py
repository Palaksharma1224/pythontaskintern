n=int(input("enter the number"))
if n<0:
    print("the number is negative")
else:
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print("factorial=",fact)