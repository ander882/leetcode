#
Code
Testcase
Testcase
Test Result
7. Reverse Integer

class Solution:
    def reverse(self, x: int) -> int:

        ne = x < 0  # Negative?
        if ne:
            x = x * -1
        # only working with positive numbers now.

        on = 0  # Output Number

        while x > 0:
            on = on*10 + x%10
            x //= 10

        if on > 2**31-1:
            return 0
        if ne:
            return on*-1
        else:
            return on
