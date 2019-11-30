#Task8
list = [] 
# number of elemetns as input 
n = int(input("Enter number of elements : "))  
for i in range(0, n): 
    ele = int(input())
    list.append(ele) # adding the element
print(list)

def multiply(list):  
    total = 1
    for x in list:
        total *= x  
    return total  
print(multiply(list))
