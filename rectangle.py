# Calculating the area of a square
l = input("What is the length? ")
w = input("What is the width? ")
area = float(l) * float(w)
if l == w:
    print("That is a square, you fucking idiot.") 
else:
    print("The area of the rectangle is " + str(area))
