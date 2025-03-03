#30 - Substring with Concatenation of All Words

'''
My first FAIL!  
Time Limit Exceeded
179 / 182 testcases passed

It works, just not in time.  And I'm not fixing it.  Probably needs a re-write.
Note say to use a sliding window.  Time to research and learn it...
'''

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(words) == 0: return 0  #this is wrong

        numwords = len(words)
        strlen = len(words[0])
        concats = numwords*strlen

        checks = [0] * numwords
        returnarray = []


        #We will be taking (numwords*strlen) slices from s and testing those

        for i in range (len(s) -concats +1 ):
            # initalize the array
            checks = words.copy()

            for j in range(i, concats+i, strlen):
                segment = s[j:j+strlen]
                if segment in checks:
                    indx = checks.index(s[j:j+strlen])
                    checks.pop(indx)
                else:
                    break

            if len(checks) == 0:
                returnarray.append( i )

            
        return returnarray
