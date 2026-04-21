N = 10

a = 0
b = 1

for i in range(N):
    print(a, end=" ")
    next_number = a + b
    a = b
    b = next_number