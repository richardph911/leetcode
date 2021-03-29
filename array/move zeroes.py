#
#Input: nums = [0,1,0,3,12]
#Output: [1,3,12,0,0]

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        j=0
        for i in range(length):
            if nums[i]!=0:
                nums[i], nums[j]=nums[j], nums[i]
                j+=1
