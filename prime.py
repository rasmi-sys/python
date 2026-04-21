n = int(input("enter a num : "))
if n <= 1:
    print("not prime")
else:

    for i in range(2, int(n**0.5) + 1):
#        print(int(n**0.5))
        if n % i == 0:
            print("not prime")
            break
    else:
        print(" prime")