# 8. String to Integer (atoi)

class Solution:
    def myAtoi(self, s: str) -> int:
        
        si = 0
        sl = len(s)

        if s == "": return 0

        while si < sl and s[si] == " ":
            si += 1

        ne = False
        if si < sl and s[si] == "-":
            ne = True
            si += 1
        elif si < sl and s[si] == "+":
            si += 1
        
        while si < sl and s[si] =="0":
            si += 1

        on = 0
        
        while si < sl and s[si] in "1234567890":
            on = on*10 + int(s[si])
            si += 1
        
        if on > 2**31-1:
            if ne:
                return -2**31
            else:
                return 2**31-1
        
        if ne:
            on = on * -1
        
        return on
