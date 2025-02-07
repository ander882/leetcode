# 14. Longest Common Prefix 

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]

        for i in range(len(strs[0])):
            chr = strs[0][i]
            for s in strs[1:]:
                if i >= len(s):
                    return strs[0][:i]
                if s[i] != chr:
                    return strs[0][:i]
        
        return strs[0]
