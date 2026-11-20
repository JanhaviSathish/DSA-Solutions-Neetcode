class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedstr=""
        for i in strs:
            encodedstr=encodedstr+i+"~"
        return encodedstr
    def decode(self, s: str) -> List[str]:
        strs=[]
        strs=s.split("~")[:-1]
        return strs


        
