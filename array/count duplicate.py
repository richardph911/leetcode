#Input:
#[4,3,2,7,8,2,3,1]
#
#Output:
#[2,3]
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        seen = set()

        for n in nums:
            if n in seen:
                ans.append(n)
            seen.add(n)
        return ans
        
