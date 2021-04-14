#Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
#Output: 6
#Explanation: [4,-1,2,1] has the largest sum = 6.
# compare max ( nums[i] with sum of current and nums[i] )
# then compare max(total and sum of current)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
  
        newNum = maxTotal = nums[0]

        for i in range(1, len(nums)):
            newNum = max(nums[i], nums[i] + newNum)
            maxTotal = max(newNum, maxTotal)

        return maxTotal
