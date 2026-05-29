a = [10,3,10,6,2,5,1]
even = []
odd = []

for i in range(0,len(a)):
    if(a[i]%2==0):
        even.append(a[i])
        even.sort()
    else:
        odd.append(a[i])
        odd.sort()

print(even)
print(odd)