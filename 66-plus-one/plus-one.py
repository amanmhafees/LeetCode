class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result=[]
        num=0
        for i in digits:
            num=num*10+i
        num=num+1
        return [int(d) for d in str(num)]
        