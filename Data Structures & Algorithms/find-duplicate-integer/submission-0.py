class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            expectedPosition = num - 1

            if expectedPosition == i:
                continue
            
            if nums[expectedPosition] == num:
                return num
            
            nums[expectedPosition], nums[i] = nums[i], nums[expectedPosition]

        return None

            