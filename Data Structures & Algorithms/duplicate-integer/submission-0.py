class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numbersSeen = set()

        for num in nums:
            if num in numbersSeen:
                return True
            else:
                numbersSeen.add(num)

        return False

        
         