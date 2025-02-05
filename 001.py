# problem 001  - Two Sums

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s={}
        for i, val in enumerate(nums):
            n = target - val
            if n in s:
                return [s[n], i]
            else:
                s[val] = i
        return []

