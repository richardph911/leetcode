
# how many coin needed to make the change
# [1,2,5,11]
# --> 11
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # output must return int type.
        array = [float('inf') for i in range(amount + 1)] # set each index to inf
        array[0] = 0 # must be 0
        for i in range(1, amount+1):
            for coin in coins:
                if i>=coin:
                    # [0,1,2,3,4,...11]
                    # [1,1,2,2,.....  ]
                    # at i = 2: means if amount = 2 then
                    # coin 1: min([2-1]+1, inf) -> a[1]+1 = 1
                    # coin 2: min([2-2]+1, inf) -> a[0]+1 = 1
                    # cant be coin 5
                    # then min at 2 = 1
                    array[i]= min(array[i], array[i-coin]+1)
        # return the weight in that index
        # return array[amount] if array[amount] != float('inf') else -1
        if array[amount] != float('inf'):
            return int(array[amount])
        else:
            return -1

        
