# a = [1, 2, 3, 4, 5]

# for i in range(len(a)):
#     if a[i]%2 == 0:
#         a[i] = "+"
#     else:
#         a[i] = "-"
# print(a)


a = int(input("Enter number: "))

for i in range(a):
    for j in range(a):
        if (i+j)%2 == 0:
            print("-", end="")
        else:
            print("+", end="")