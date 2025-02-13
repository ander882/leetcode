# 20. Valid Parentheses

'''
Ok, I'd like to come back to this one.  
3 ms  Beats 21.87%
horrible!
'''

class Solution:
    def isValid(self, s: str) -> bool:
        
        que=[]

        while s:
            if s[0] in '([{':
                que.append(s[0])
                s=s[1:]
                continue

            if len(que) == 0:
                return False

            if s[0] == "}":
                if que[-1] == "{":
                    que.pop()
                else:
                    return False
            
            elif s[0] == "]":
                if que[-1] == "[":
                    que.pop()
                else:
                    return False
            
            elif s[0] == ")":
                if que[-1] == "(":
                    que.pop()
                else:
                    return False
            
            else:
                return 3

            s=s[1:]
        
        if len(que) > 0:
            return False
        else:
            return True
