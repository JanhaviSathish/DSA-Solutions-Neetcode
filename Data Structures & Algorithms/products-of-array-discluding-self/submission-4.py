from itertools import accumulate
import operator
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[0]*len(nums)
        suffix=[0]*len(nums)
        res=[0]*len(nums)
        prefix = list(accumulate(nums[:-1], operator.mul, initial=1))
        suffix = list(accumulate(nums[:0:-1], operator.mul, initial=1))[::-1]

        for i in range(len(nums)):
            res[i]=prefix[i]*suffix[i]
        return res



