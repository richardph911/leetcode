class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        left, right = 0, len(nums)-1
        # from 0 to len(nums) - 1
        while left <= right:
            # value left < right so that would be the min
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break
            #otherwise, binary search with middle
            mid = (left + right) //2
            res = min(res, nums[mid])
            #search if in left portion
            # 3   5  1
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid -1
        return res
        