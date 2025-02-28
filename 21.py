# 22 Generate Parentheses

#hahaha
## Beats 99.22% !

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        nleft = 0
        nright = 0
        str = ""
        rtrn = []

        while True:

            while nleft < n:
                str+= "("
                nleft +=1
            
            while nright < n:
                str += ")"
                nright += 1
            
            rtrn.append(str)

            while True:
                if str[-1] == ")":
                    str=str[:-1]
                    nright -=1
                elif nleft > nright+1:
                    str = str[:-1] + ")"
                    nright +=1
                    nleft -=1
                    break
                else:
                    str=str[:-1]
                    nleft -=1
                if str == "": break

            if str == "": break
        
        return rtrn

