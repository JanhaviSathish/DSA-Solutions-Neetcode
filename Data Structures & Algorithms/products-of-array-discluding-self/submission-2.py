'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        self=[]
        for i in range(len(nums)):
            product=1
            for j in range(len(nums)):
                if j==i:
                    continue
                else:
                    product*=nums[j]
            self.append(product)
        return self
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        self=[0]*len(nums)
        zero_count=0
        product=1
        for i in range (len(nums)):
            if nums[i]==0:
                zero_count+=1
            else:
                product*=nums[i]
        if zero_count>1:
            return self
        for j in range(len(nums)):
            if zero_count==1:
                if nums[j]==0:
                    self[j]=product
            else:
                self[j]=product//nums[j]
        return self
        