class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []
        for num in nums:
            for i, v in enumerate(res):
                if num <= v:
                    res[i] = num
                    break
            else:
                res.append(num)
        return len(res)
