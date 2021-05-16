# coin change
O(S*N)--> s step n elemeents
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # create a temp array with number of elements as amount+1
        # and populate the array with the (amount+ 1 ) number.
        
        # We do amount+1 as the initial minimum will always be greater than amount and
        # the length is greater than amount as this will help intialize first element to be zero
        # output of temp for amount 11 ---> [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]
        temp_arr = [amount+1] *(amount+1)
        
        # output of temp after initialization ---> is [0, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]
        temp_arr[0]=0
        
        # iterate through 1 to the amount+1
        for i in range(1, amount+1):
            
            # iterate through all the coin in coins
            for value in coins:
                
                # if the amount index is greater than equal to the value of the coin
                if i >=value:
                    
                    # update the temp array by finding the minimum between
                    # current element in the temp array and element present in the index - value of temp array plus 1.
                    # 1 is added because the count of the number of coins increases if the minimum is met.
                    temp_arr[i] = min(temp_arr[i], temp_arr[i-value]+1)
          
        # The last element in the temp array, if it is equal to the amount +1, then the amount can't be made from the given coins.
        if temp_arr[amount] == amount+1:
            return -1
        
        # or else return the last element from the temp array.
        return temp_arr[amount]
