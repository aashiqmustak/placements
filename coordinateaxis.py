a = int(input("Enter the x-coordinate: "))

b = int(input("Enter the y-coordinate: "))

if a > 0 and b > 0:
    print("The point is in the First Quadrant")

elif a < 0 and b > 0:
    print("The point is in the Second Quadrant")

elif a < 0 and b < 0:
    print("The point is in the Third Quadrant")

elif a > 0 and b < 0:
    print("The point is in the Fourth Quadrant")

elif a == 0 and b == 0:
    print("The point is at the Origin")
else :
    print("The point is on the Axis")