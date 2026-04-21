import array
a = array.array('i',[4,5,6,7,3,2,54,64])
a_sorted = array.array('i', sorted(a))
print(a)
print(a_sorted)