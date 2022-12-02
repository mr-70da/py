lst = list(input("Please Enter An Array: "))
m = int(input("Enter m:"))
n = int(input("Enter n: "))
p = int(input("Enter p: "))
new_lst = list(range(n - m))
lst.pop(p)
for x in range(m, n):
    new_lst[x - m] = lst[x]
print(new_lst)