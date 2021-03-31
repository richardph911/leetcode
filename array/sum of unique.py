
#Input: nums = [1,2,3,2]
#Output: 4
#Explanation: The unique elements are [1,3], and the sum is 4.
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        total = 0
        for value in nums:
            if nums.count(value)==1:
                total+=value
        return total
            
