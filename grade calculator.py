english=89
math=50
science=33
sum=english+math+science
percentage=sum/300*100

if(percentage>=90 and percentage<=100):
    print("Grade A")
elif(percentage>=70 and percentage<=89):
    print("Grade B")
elif(percentage>=60 and percentage<=74):
    print("Grade C")
elif(percentage>=40 and percentage<=59):
    print("Grade D")
else:
    print("Grade F")
