class Solution(object):
    def searchInsert(self, nums, target):
        l, r = 0, len(nums) - 1

        while l <= r:
            middle = (l + r) // 2

            if target == nums[middle]:
                return middle
            elif target > nums[middle]:
                l = middle + 1
            else:
                r = middle - 1

        return l

print(Solution().searchInsert([1,3,5,6],9))