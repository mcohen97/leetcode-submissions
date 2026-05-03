class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        accumProductLeft2Right = [0 for num in nums]
        accumProductRight2Left = [0 for num in nums]

        left2RightAccum = 1
        right2LeftAccum = 1
        
        for i, num in enumerate(nums):
            left2RightAccum *= nums[i]
            accumProductLeft2Right[i] = left2RightAccum

            right2LeftAccum *= nums[-(1 + i)]
            accumProductRight2Left[-(1 + i)] = right2LeftAccum    

        answer = [0 for num in nums]

        for i, num in enumerate(nums):
            left2i = accumProductLeft2Right[i - 1] if i > 0 else 1
            right2i = accumProductRight2Left[i + 1] if i < len(nums) - 1 else 1

            answer[i] = right2i * left2i

        return answer
        