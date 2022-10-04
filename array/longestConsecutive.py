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
        
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            # check if its the start of a sequence
            # only check if that number is the start. if not, ignore.
            # if that start, then add up the start which is 1 + length --> 2->3>4
            #return the longest length
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest