class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0

        max_pro , min_pro = nums[0], nums[0]

        #result will store the final max product
        result = max_pro

        for i in range(1, len(nums)):
            current = nums[i]#=3,-2,4

            temp_max = max( current ,  max_pro*current, current*min_pro) #=6,-2,4

            min_pro = min( current ,  max_pro*current, current*min_pro) #=3,-2,-8

            max_pro = temp_max #=6,6,6

            result = max(result, max_pro)#=6,6,6

        return result
