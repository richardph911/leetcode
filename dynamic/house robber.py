#For example: num = [1,7,9,4], at the beginning, max_3_house_before, max_2_house_before, adjacent are initialized to 0, so it is like putting 3 zeros before the input list [0, 0, 0, 1, 7, 9, 4]. Here are steps for calculating the max sum for each house(the sliding window is marked by parentheses):
#
#[(0, 0, 0, 1), 7, 9, 4], cur = max(0+1, 0+1)
#
#-> [ (0, 0, 1, 7), 9, 4], cur = max(0+7, 0+7)
#
#-> [(0, 1, 7, 9), 4], cur = max(0+9, 1+9)
#
#-> [(1, 7, 10, 4)], cur = max(1+4, 7+4)
#
#-> [7, 10, 11], 10 is the max sum of path that includes num[-2], 11 is the max sum of path that includes num[-1], so return max(10, 11)
class Solution:
    
    def rob(self, nums):
        last, now = 0, 0
        for i in nums: last, now = now, max(last + i, now)
        return now
#        if not nums:
#            return 0
#
#        dp = {}
#        dp[0] = 0
#        dp[1] = nums[0]
#
#        for i in range(2, len(nums) + 1):
#            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])
#        return dp[len(nums)]
