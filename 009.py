# 9. Palindrome Number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        sn = str(x)
        if sn[0] == "-": return False

        sl = len(sn)
        if sl == 1: return True

        mid = sl // 2 

        if sl%2 == 1:
            return sn[:mid] == sn[:mid:-1]
        else:
            return sn[:mid] == sn[:(mid-1):-1]
