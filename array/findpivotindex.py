# Input: nums = [1,7,3,6,5,6]
# Output: 3
# Explanation:
# The pivot index is 3.
# Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
# Right sum = nums[4] + nums[5] = 5 + 6 = 11
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
#         middle = len(nums) // 2
#         for i in range(len(nums)):
#             if sum(nums[:i]) == sum(nums[i+1:]):
#                 return i
#         return -1
        right = sum(nums)
        left = 0
        for i, val in enumerate(nums):
            right -= val
            if right == left:
                return i
            left += val
        return -1