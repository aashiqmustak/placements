# a = 10
# b= 20
# c= 30
# d= 40
# e= 50

# avg = (a + b + c + d + e) / 5
# print("Average = ",avg)
# print()

n = int(input())

l = list(map(int, input().split()))   # leaving
w = list(map(int, input().split()))   # entering

rem = 0
maxi = 0

for i in range(n):
    rem = rem + l[i] - w[i]
    if rem > maxi:
        maxi = rem

print(maxi)