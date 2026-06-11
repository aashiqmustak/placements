b = int(input("Enter a binary number "))
decimal = 0
i = 0

while b != 0:
    rem = b % 10
    decimal = decimal + rem * (2 ** i)
    b = b // 10
    i += 1
print(decimal)