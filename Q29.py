base= int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))
i=0
result= 1
while i < exponent:
   result = result * base
   i=i+1
print(result)