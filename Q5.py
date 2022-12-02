str= input()
i=len(str)
rev=""
while i > 0:
    rev=rev+str[i-1]
    i=i-1
print(rev)
