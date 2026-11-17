class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        D={}
        for i in nums:
            if i not in D:
                D[i]=1
            else:
                D[i]+=1
        for i in D:
            if D[i]>1:
                return True
        return False
            