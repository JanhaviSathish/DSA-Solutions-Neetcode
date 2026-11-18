class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        D={}
        for i in nums:
            if i in D:
                D[i]+=1
            else:
                D[i]=1
        sorted_desc=dict(sorted(D.items(),key=lambda item: item[1],reverse=True))
        return list(sorted_desc.keys())[:k]