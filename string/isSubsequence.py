class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        count = 0
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False 
        
        for i in t:
            if s[count] == i :
                count +=1
                if count == len(s):
                    return True
        return False
            