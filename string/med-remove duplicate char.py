class Solution:
    # your ouput need to chose the "closet" in lexicalgraphical order a b c ..z
    # input = "cbacdcbc"
    def removeDuplicateLetters(self, s: str) -> str:
        #  ch = ch[ch.index(i) + 1:] + i
        ch = { values:index for index, values in enumerate(s)} # create ch: {'c':7, 'b':6, 'a':2, 'd': 4}
        res = []
        # ["c"] "b"
        for index, char in enumerate(s):
            # condition
            # res not empty
            # "c" > "b" lexcical then pop c out and add b first
            # index < index of last character in res []: compare index(c) and ch["c"]: 2 < 7 then c must appear at least one
            if char not in res:
                while res and char < res[-1] and index < ch[res[-1]]:
                    res.pop()
                # a = 3 > a in ch = 2 so a only one. then add c
                res.append(char)
        return "".join(res)
        
