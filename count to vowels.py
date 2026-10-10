def vowel_count(string):
   count_vowel=0
   count_constants=0
   for i in string:

         if(i=="a"or i=="e" or i=="o" or i=="u" or i=="i"):
            count_vowel+=1
         else:
             count_constants+=1

   print("vowels=",count_vowel)
   print("constants=",count_constants)       

vowel_count("apple")