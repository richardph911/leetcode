class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        map = defaultdict(int)
        result = 0
        for i in time:
            modNum = i % 60
            if modNum == 0:
                result += map[0]
            else:
                result += map[60 - modNum]
            map[modNum] +=1
        return result
#         result = 0 
#         hash ={}
#         for i in time:
#             modNum = i % 60
#             if modNum == 0:
#                 if 0 in hash:
#                     result += hash[0]

#             elif (60-modNum) in hash: # 60 - 20 = 40,  we need 40 so we need 60 -modnum
#                 result += hash[60-modNum]
#             if modNum in hash:
#                 hash[modNum] +=1 
#             else:
#                 hash[modNum] = 1
#         return result
