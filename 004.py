# 4. Median of Two Sorted Arrays

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a=0
        b=0

        la = len(nums1) 
        lb = len(nums2)
        even = (la + lb) % 2 == 0

        ua = a<la
        ub = b<lb

        num = int((la+lb)/2)
        if even:
            num -= 1

        def popnext():
            nonlocal a
            nonlocal b
            nonlocal ua
            nonlocal ub

            ab = 0
            if not ua:
                ab = 2
            elif not ub:
                ab = 1
            else:  # ab = 0:
                if nums1[a] < nums2[b]:
                    ab = 1
                else:
                    ab = 2
            
            if ab == 1:
                r=nums1[a]
                a+=1
                ua = a<la
            else:
                r=nums2[b]
                b+=1
                ub = b<lb
            return r

        while num > 0:

            popnext()

            num -= 1

        if even:
            r1 = popnext()
            r2 = popnext()
            return (r1+r2)/2
        else:
            return popnext()

