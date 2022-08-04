class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapS, mapT = {}, {}
        for i in s:
            mapS[i] = 1 + mapS.get(i, 0)
        for i in t:
            mapT[i] = 1 + mapT.get(i, 0)
        return mapS == mapT