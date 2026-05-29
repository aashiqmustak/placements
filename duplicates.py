a = []
dup=[]
noDup=[]

b = int(input("Enter number of elements: "))
for i in range(b):
    c = int(input("Enter element: "))
    a.append(c)


for i in range(len(a)):
    if a.count(a[i]) > 1:
        if a[i] not in dup:
            dup.append(a[i])
    else:
        if a[i] not in noDup:
            noDup.append(a[i])

print("Duplicate elements:", dup)
print("Non-duplicate elements:", noDup)
