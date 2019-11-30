#Task 7
a = float(input("Input first number: "))
b = float(input("Input second number: "))
c = float(input("Input third number: "))

l = []
l.append(a)
l.append(b)
l.append(c)

l.sort()

print("Median of given three numbers: ",l[1])