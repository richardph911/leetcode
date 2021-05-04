# we just push onto stack and pop if closing is next. at the end if empty then valid true


        class Solution:
    def isValid(self, s):
        stack = [0]
        mapping = {0: None, '(':')', '[':']', '{':'}'}
        for c in s:
            if c in mapping:
                stack.append(c)
            else:
                if mapping[stack.pop()] != c: return False
        return stack == [0]
        
        
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
            elif len(stack) <= 0:
                return False
            elif char == ")" and stack.pop() != "(":
                return False
            elif char == "]" and stack.pop() != "[":
                return False
            elif char == "}" and stack.pop() != "{":
                return False
        if len(stack) == 0:
            return True
        return False
        
        
      
