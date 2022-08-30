class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        maxPro = 0
        for i in range(1, len(prices)):
            if prices[left] < prices[i]:
                maxPro = max(maxPro, prices[i] - prices[left])
            else:
                left = i
        return maxPro
                