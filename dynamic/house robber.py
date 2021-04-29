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
