list = [] 
# number of elemetns as input 
n = int(input("Enter number of elements : "))  
for i in range(0, n): 
    ele = str(input())
    list.append(ele) # adding the element 
print(list) 

l = []
for i in list:
    length = 0
    for j in i:
        length += 1
    l.append(length)
l.sort()  # arranging lengths in ascending order
print(l[-1]) # finding maximum in the list