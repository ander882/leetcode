#  I am not doing this one.  Because I found one of the best write-ups and code examples that I have seen myself in a long time.
#  I'll tip my hat to myash2708.

# 29 - Divide Two Integers
# (Python) Easiest Optimal Solution ✔︎

'''
myash2708
Python
Time Complexity: O(Log(Dividend/Divisor))
Space Complexity: O(1)
Intuition
The problem requires performing integer division without using the / or * operators. 
Instead of subtracting the divisor one by one from the dividend (which takes O(Dividend/Divisor) time), 
we optimize by doubling the divisor using bitwise shifts (<<), 
reducing the number of operations to O(log(Dividend/Divisor)).

Approach
Handle Edge Cases:
• If dividend == 0, return 0 (anything divided by a nonzero number is 0).
• If divisor == 1, return dividend directly.
• If divisor == -1, return -dividend (handling overflow cases later).
Determine Sign of the Result:
• If dividend and divisor have the same sign, the result is positive.
• If they have different signs, the result is negative.
Convert to Absolute Values:
• We work with positive values to simplify calculations.
Bitwise Subtraction Using Doubling:
• Goal: Find how many times divisor can fit into dividend.
• Instead of subtracting divisor one by one, we double it (temp_divisor <<= 1) until it exceeds dividend.
• Track how many times it was doubled using multiple <<= 1.
• Subtract temp_divisor from dividend and add multiple to quotient.
Adjust the Sign and Handle Overflow:
• Multiply quotient by sign to restore its correct sign.
• Clamp the result within the 32-bit integer range ([-2³¹, 2³¹ - 1]).

Code
'''

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        
        quotient = 0

        if dividend==0: return 0
        elif divisor==1: quotient = dividend
        elif divisor==-1: quotient = -dividend

        else:
            sign = 1 if (dividend>0)==(divisor>0) else -1

            dividend = abs(dividend)
            divisor = abs(divisor)

            while dividend>=divisor:
                temp_divisor, multiple = divisor, 1

                while dividend >= (temp_divisor<<1):
                    temp_divisor <<= 1
                    multiple <<= 1

                dividend -= temp_divisor
                quotient += multiple

            quotient*=sign

        if quotient > (2**31)-1: return (2**31)-1
        elif quotient < -(2**31): return -(2**31)
        return quotient

Thank You!
