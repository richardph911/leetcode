class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # swap egg --> add
        # note: no 2 chars map to the same chars: a -> b, r -> b
        sdict , tdict = {}, {}
       
        for (i,j) in zip(s,t):
            # if not seen in dict and no 2 chars map to the same char a -> 0, r -> 0 
            # {f: b, o: a } sdict
            # {b:f , a: o } tdict
            # i = o, dict[o] == a?? but dict[o] == r then duplicate
            if ((i in sdict and sdict[i] != j) or (j in tdict and tdict[j] != i)):
                return False
            #else swap
            sdict[i] = j
            tdict[j] = i
        return True