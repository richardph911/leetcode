#Input: nums = [1,2,3,1]
#Output: true
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
        
        # sets = {}
        # for i in nums:
        #     if i not in sets:
        #         sets[i] = 1
        #     else:
        #         return True
        # return False
