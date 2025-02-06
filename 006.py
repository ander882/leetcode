#6. Zigzag Conversion

class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows < 1: 
            return ""
        if numRows == 1: 
            return s

        rows = [""] * numRows

        sl = len(s)
        si = 0

        cr = 0

        while si<sl:

            if cr == 0:
                for cr in range(numRows):
                    rows[cr] = rows[cr] + s[si]
                    si+=1
                    if si == sl: break
            
            else:
                rows[cr] = rows[cr] + s[si]
                si += 1
            
            cr -= 1

        return "".join(rows)
