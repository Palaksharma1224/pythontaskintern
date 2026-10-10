a=input("enter the word")
count_vowel=0
count_constants=0
for i in a:
    if (i=="a"or i=="e" or i=="o" or i=="u" or i=="i"):
        count_vowel+=1
    else:
        count_constants+=1
print(count_vowel)
print(count_constants)