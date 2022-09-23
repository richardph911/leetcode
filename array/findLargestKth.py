class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # O(k+(n-k)lgk) time, min-heap

        heap = []
        for num in nums:
            heapq.heappush(heap, num)
        for _ in range(len(nums)-k):
            heapq.heappop(heap)
        return heapq.heappop(heap)