class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ch = ''
        count = 0
        for i in s:
            if i not in ch:
                ch += i
            else:
                ch = ch[ch.index(i) + 1:] + i
            count = max(count, len(ch))
        return count
