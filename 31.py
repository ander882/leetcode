# next permotation

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1: return
        
        # Find the frst nuber to permute on.
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                #we found the place!
                break

        #nums[i:] will be worked on later
        # nums[i] is where the next permutation happens
        # nums[:i] is already good.  in descending order

        # nums[i] now gets the next higher number in nums[:i+1]

        #Find the next higner number
        for j in range(len(nums)-1, -1, -1):
            if nums[j] > nums[i]:
                break
        
        if i == j == 0:
            #The end for all permutations.  Start over
            # instead of the sort function, everything is in decreasing order
            # so swap values from the last/front, last-1/front+1, etx
            nums.sort()
            return 
        
        # switch the 2 numbers
        nums[j], nums[i] = nums[i], nums[j]

        # now sort nums[i+1:]
        nums[i+1:] = sorted(nums[i+1:])

        return
