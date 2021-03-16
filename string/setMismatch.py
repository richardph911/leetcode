class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # find duplicate
        newList = []
        results = []
        for i in nums:
            # need to check if in newList first to append
            # otherwise it will add all nums into results list
            if i in newList:
                results.append(i)
            newList.append(i)
        j = 1
        while( j <= len(nums) +1):
            if(j not in nums):
                results.append(j)
                return results
            j += 1