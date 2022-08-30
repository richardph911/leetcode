class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # using the idea of maxheap and negative the values
        # then heappop and add to the heap the substraction
        stoneVal = [-s for s in stones]
        # bring the smallest of stoneVal to the first []
        heapq.heapify(stoneVal)
        while len(stoneVal) > 1 :
            first = heapq.heappop(stoneVal)
            second = heapq.heappop(stoneVal)
            if first < second:
                heapq.heappush(stoneVal, first - second)
      
        stoneVal.append(0) #if stone empty
        #stoneVal [-1, 0]
        return abs(stoneVal[0])
            
        