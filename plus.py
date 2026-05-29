a = int(input("Enter a number: "))

b = []

for i in range(1,a):
    
    if (i*i >=a):
        break
    b.append(i*i)
print(b)