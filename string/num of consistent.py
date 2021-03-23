class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for value in words:
            for i in value:
                if i not in allowed:
                    count +=1
                    break
        return len(words) - count
