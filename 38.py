# 38. Count and Say

def nextrle(s: str) -> str:

    engine = 0
    caboose = len(s)
    returnstr = ""

    while engine < caboose:
        char = s[engine]
        count = 1
        engine += 1
        while engine < caboose and s[engine] == char:
            count += 1
            engine += 1
        returnstr += str(count) + char
    return returnstr

class Solution:

    # ok the write up is crazy on this problem.
    # if I have to re-read it more than 3 times, it needs a re-write

    # looked at the first hint.  Darn
    # Decided to use tuples instead of the arrays
    # now decided to just use the string.


    def countAndSay(self, n: int) -> str:
        if n == 1: return "1"

        returnstr = "11"
        for i in range(2, n):
            returnstr = nextrle(returnstr)
        
        return returnstr
