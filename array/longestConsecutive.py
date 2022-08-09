class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # length = count += 1
        res = 0
        nums = set(nums)
        for i in nums:
            if i - 1 not in nums:  # then num is the left most of the consecutive sequence
            #     left = i
                right = i
                while right + 1 in nums:  # scan to find the right most of the consecutive sequence
                    right += 1
                res = max(res, right - i + 1)
        return res
        