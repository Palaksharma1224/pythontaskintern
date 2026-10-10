def fact_num(num):
    if num==0 and num==1:
        print("the number is negative")
    else:
        fact=1
        for i in range(1,num+1):
            fact=fact*i
            print("factorial",fact)
fact_num(5)