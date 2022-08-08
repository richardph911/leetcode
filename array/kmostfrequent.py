class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Input: nums = [1,1,1,2,2,3,6], k = 2
        # Output: [1,2]
        # idea is to get dict of freq
        freq = {}
        count = [[] for i in range(len(nums) + 1)]
        for i in nums:
            # get {1:3, 2:2, 3:1}
            freq[i] = 1 + freq.get(i, 0)
        for i, frequent in freq.items():
            count[frequent].append(i)
        # count [[],[3, 6],[2],[1],[],[],[]] # sort frequency ascending so 1 will have the most frequent
        res = []
        for i in range(len(count) -1, 0 , -1 ):
            for val in count[i]:
                res.append(val)
            # res [1,2,3,6]
            if len(res) == k:
                return res