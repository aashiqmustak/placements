a = ['a', 'b', 'c', 'd']
b = input("Enter a character: ")

o = []

for i in range(len(a)):
    if a[i] == b:
        break
    o.append(a[i])

print(o)