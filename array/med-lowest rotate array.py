# return the minimum element of this array.
# just rotate the sorted array, so left and right are sorted too
# using binary search to find the lowest
# at the end, return low or high fine
class Solution:
    def findMin(self, nums: List[int]) -> int:
        low , high = 0, len(nums) -1
        while low<high:
            mid = low + (high-low) //2
            mid_element = nums[mid]
            if mid_element > nums[high]:
                low = mid+1
            else:
                high = mid
        return nums[low]
            
        
        # low = 0
        # high = len(nums) - 1
        # while low <= high:
        #     mid = low + (high - low) // 2
        #     ele = nums[mid]
        #     if ele > nums[high]:
        #         low = mid + 1
        #     elif mid == 0 or nums[mid - 1] > nums[mid]:
        #         return nums[mid]
        #     else:
        #         high = mid - 1
        
