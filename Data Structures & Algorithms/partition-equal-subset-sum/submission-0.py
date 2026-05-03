class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        cache = set()
        cache.add(0)
        halfSum = sum(nums) / 2

        for num in nums:
            cacheCopy = cache.copy()
            for s in cacheCopy:
                newSum = s + num
                if newSum == halfSum:
                    return True
                cache.add(newSum)
        
        return False        