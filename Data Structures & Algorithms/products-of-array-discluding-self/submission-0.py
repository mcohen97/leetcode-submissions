class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        productOfAll = 1
        zeroPosition = None

        answer = [0 for num in nums]

        for i, num in enumerate(nums):
            if num == 0 and zeroPosition != None:
                return answer
            if num == 0:
                zeroPosition = i
            else:
                productOfAll *= num
        
        for i, num in enumerate(nums):
            if zeroPosition == None:
                answer[i] = productOfAll // num
            elif zeroPosition != None and i == zeroPosition:
                answer[i] = productOfAll
            else:
                answer[i] = 0
        
        return answer