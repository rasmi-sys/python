class Solution(object):
    def plusOne(self, digits):
        if len(digits)==0:
            return [1]
        if digits[-1] != 9:
            digits[-1]+=1
            return digits
        else:
            digits= self.plusOne(digits[:-1])
            digits.append(0)
            return digits

print(Solution().plusOne([9,9,9 ]))