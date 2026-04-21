from array import *

arr = array('i', [])
n = int(input("Enter the size of the array"))
for i in range(n):
    x = int(input("Enter the next element of the array"))
    arr.append(x)
print(arr)
# val= int(input("Enter the element you want to search in the array"))
# index=0
# for i in arr:
#     if i==val:
#         print(index)
#         break
#     index+=1

# print("element does not exist in the array")

val = int(input("Enter the index of element you want to delete in the array"))
# if 0 <= val < len(arr):
#     del arr[val]
# else:
#     print("Invalid index")

if val < 0 or val >= len(arr):
    print("invalid index")
else:
    for i in range(val, n - 1):
        arr[i] = arr[i + 1]
    arr.pop()

print(arr)

# reverse

for i in range(len(arr)//2):
    temp = arr[i]
    arr[i] = arr[len(arr)-1-i]
    arr[len(arr)-1-i] = temp
print(arr)
