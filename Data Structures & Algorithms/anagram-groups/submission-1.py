# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         L=[]
#         for j in strs:
#             letters=sorted(j)
#             found=False
#             i=0
#             while i<len(L):
#                 if sorted(L[i][0])==letters:
#                     L[i].append(j)
#                     found=True
#                     break
#                 i+=1
#             if not found:
#                 L.append([j])
#         return L

class Solution:
    def groupAnagrams(self, strs: List[str]) ->List[List[str]]:
        D={}
        for j in strs:
            letters="".join(sorted(j))
            if letters in D:
                D[letters].append(j)
            else:
                D[letters]=[j]
        return list(D.values())