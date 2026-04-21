Solutobjectclass ):
    def removeDuplicates(self, nums):
        k=1
        for i in range (1, len(nums)):
            if nums[i] != nums[i-1]:
                k+=1

        pointer=1
        for i in range (1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[pointer] = nums[i]
                pointer+= 1

        for i in range (pointer , len(nums)):
            nums[i] = '_'