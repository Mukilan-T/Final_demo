import array as arr
from array import *

a = arr.array('i', [])

k = int(input("Enter size of array:"))
for i in range(0, k):
    num = int(input("Enter %d array element:" % (i + 1)))
    a.append(num)

print("All array elements are:", end="")
for i in a:
    print(i, end=" ")
    
a.reverse()
print("\nReverse the order of the items:")
for i in a:
    print(i, end=" ")
