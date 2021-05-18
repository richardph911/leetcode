# return how many ways
# all the column[0] = 1
#             0   1   2   3   4   5
#  []         1   0   0   0   0   0
#  ['1']      1   1   1   1   1   1 -->if we have 5 coins then add 1+1+1+1+1 = 5
#  ['2']      1       2       3
#  ['5']      1
# if amount =4 then:4 -2 = 2 --> a[4-2]+a['2'][2]:  2+2, 2+1+1, 1+1+1+1
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        array = [0] * (amount + 1 )
        array[0] = 1
        # array[coin, 1.....5]
        for coin in coins:
            for i in range(1, amount + 1):
                if i>= coin: # if we cant choose i, then we use the previous
                    array[i] += array[i - coin]
        return array[amount]
        
