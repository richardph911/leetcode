# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
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
    # class Solution:
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     seen = {}
    #     left = 0
    #     output = 0
    #     # a b c d a b
    #     # 0 1 2 3 x
    #     # output = max(output, right - left + 1)
    #     for current_index, val in enumerate(s):
    #         if val in seen:
    #             # then need to move the left pointer
    #             left = max(left, seen[val] +1)
    #         #not seen
    #         output = max(output, current_index - left + 1)
    #         seen[val] = current_index
    #     return output
                
