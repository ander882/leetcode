# 11. Container With Most Water

'''
Ok this is the first with a write-up.  
I had to look at a solution (used below).
Really crazy neat.
'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        ai = 0
        bi = len(height) -1

        mv = 0

        while ai < bi:
            mi = min(height[ai], height[bi])
            v = (bi - ai) * mi

            if v > mv:
                mv = v
            
            if height[ai] == mi:
                ai += 1
            else:
                bi -= 1
        
        return mv
