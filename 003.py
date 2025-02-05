# 3. Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":  # Output length
            return 0 
        o = 1
        os = s[0]
        
        a=0 # Start indes
        b=1 #  end  index

        l = len(s)

        while b < l:
            if a == b:
                b += 1

            elif s[b] in s[a:b]:
                a += 1
            
            else:
                b += 1
            
                if o <= b-a:
                   o=b-a
                   os = s[a:b]

        
        return o
