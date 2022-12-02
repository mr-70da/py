n=int(input("Enter your number: "))
sum=0
arm=0
x=n
while n!=0:
   sum+sum+(n%10)
   arm=(n%10)**3+arm
   n=n//10
print("sum of its digit is : ",sum)
if arm==x:
   print(x," is armstrong number.")