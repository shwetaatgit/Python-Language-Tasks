#Task6
print("Length of the triangle sides: ")
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

l =[]
l.append(x)
l.append(y)
l.append(z)
l.sort()
if l[0]+ l[1] >= l[2]:
    if x == y == z:
        print("Equilateral triangle")
    elif x==y or y==z or z==x:
        print("isosceles triangle")
    else:
        print("Scalene triangle")
else:
    print("It is not a triangle")