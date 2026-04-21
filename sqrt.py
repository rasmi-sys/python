'''x=int(input("enter number"))
for i in range(x+1):

        if i*i==x:
            print("sqrt of ",x," is : ",i)
            break
        elif i * i > x:
            print("sqrt of",x,"is : ",i-1)
            break
'''


class Solution(object):
    def mySqrt(self, x):
        l, r = 0, x
        res = 0

        while l <= r:
            m = l + ((r-l)// 2)
            if m ** 2 > x:
                r = m - 1
            elif m ** 2 < x:
                l = m + 1
                res = m
            else:
                return m
        return res

print(Solution().mySqrt(17))