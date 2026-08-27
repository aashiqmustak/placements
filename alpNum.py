n = int(input("Enter number of elements: "))

import pandas


txt= ""
num = []

for i in range(n):
    b = input("Enter value: ")

    if b.isalpha():
        txt += b
    else:
        num.append(int(b))


num_sum = sum(num)

print("Alphabets:", txt)
print("Sum of Numbers:", num_sum)