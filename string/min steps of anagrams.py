
#Input: s = "bab", t = "aba"
#Output: 1
#Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        for i in s:
            # replace '' foe each same occurance
            t = t.replace(i, '', 1)
        return len(t)
        
