#Input: nums = [555,901,482,1771]
#Output: 1
#Explanation:
#Only 1771 contains an even number of digits.

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        for value in nums:
            if len(str(value))%2==0:
                count +=1
        return count
