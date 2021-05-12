# return the index of target
# if it is in nums, or -1 if it is not in nums
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right-left)//2
            # stop till target reaches the mid
            if nums[mid]==target:
                return mid
            if nums[mid] >= nums[left]:
                # need to check if target in the range, then we go back middle 1
                if nums[left] <= target < nums[mid]:
                    right = mid -1
                else:
                    left = mid +1
            else:
                if nums[mid]<nums[right]:
                    if nums[mid]< target<= nums[right]:
                        left = mid + 1
                    else:
                        right = mid -1
        return -1
            
        
#         n = len(A)
#         left, right = 0, n - 1
#         if n == 0: return -1
        
#         while left <= right:
#             mid = left + (right - left) // 2
#             if A[mid] == target: return mid
            
#             # inflection point to the right. Left is strictly increasing
#             if A[mid] >= A[left]:
#                 if A[left] <= target < A[mid]:
#                     right = mid - 1
#                 else:
#                     left = mid + 1
                    
#             # inflection point to the left of me. Right is strictly increasing
#             else:
#                 if A[mid] < target <= A[right]:
#                     left = mid + 1
#                 else:
#                     right = mid - 1
            
#         return -1
        
