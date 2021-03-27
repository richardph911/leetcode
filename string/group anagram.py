class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lists = {}
        for val in strs:
            # using sorted and join to compare string
            x = ''.join(sorted(val))
            # check if x same string value
            # check if in lists already?
            if x in lists:
                lists[x].append(val)
            else:
                lists[x] = [val]
        return lists.values()
            
