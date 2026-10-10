def prime_num(a):
    if a>1:
        for i in range(2,a):
            if a%i==0:
             print(a,"is not a prime number")
             break
            else:
               print(a,"is a prime number")
    else:
       print(a,"is not prime")
prime_num(int(input("enter the number")))