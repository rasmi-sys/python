from array import *
arr1 = array('i',[1,2,3,4,5,6,7,8,9])
arr2 = array('i',[5,9,8,44,4,5,2])
arr3 = array('i',[])
# for i in range(max(len(arr1),len(arr2))):
#     val1=arr1[i] if i<len(arr1) else 0
#     val2=arr2[i] if i<len(arr2) else 0
#     arr3.append(val1+val2)
# print(arr3)

# Add only up to the shorter array (ignore extras)

# arr1 = array('i',[1,2,3,4,5,6,7,8,9])
# arr2 = array('i',[5,9,8,74,4,5,2])
# arr3 = array('i',[])
# for i in range(min(len(arr1), len(arr2))):
#     arr3.append(arr1[i] + arr2[i])
# print(arr3)


if len(arr2) == 0:
    print("Array is empty")
else:
    max_val = arr2[0]  # assume first element is the largest
    for i in range(1, len(arr2)):
        if arr2[i] > max_val:
            max_val = arr2[i]
    print("Max value:", max_val)