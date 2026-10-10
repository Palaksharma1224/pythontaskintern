s=" Hi I am palak sharma"
longest_sentence=s.split()
max_length=0
for s in longest_sentence:
    if len(s)>max_length:
        max_length=len(s)
        longest_word=s
        print("the longest sentence is:",longest_word)
