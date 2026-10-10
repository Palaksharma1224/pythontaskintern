num=int(input("enter the number"))
t1=0
t2=1
for i in range(0,num):
    print(t1,end="\t")
    t3=t1+t2
    t1=t2
    t2=t3