# d={"h":1,"e":2,"l":3,"l":4,"o":5}
# print(d.values())

string="hello"
frequency={}
for char in string:
    if char in frequency:
        frequency[char]+=1
    else:
        frequency[char]=1

print(frequency)


# count the frequency of each character in the string