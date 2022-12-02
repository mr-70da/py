n=int(input("enter the desired value: "))
sum=i=exp=0
temp=1
for x in range (i,n):
    sum = sum +(((-1)**exp))*(1/(temp))
    temp+=2
    exp+=1
print("pi: ",sum*4)