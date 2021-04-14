class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = dict()
        for i, value in enumerate(nums):
            comp = target - value
            if comp in dic:
                return [dic[comp], i]
            dic[value] = i
        return []
