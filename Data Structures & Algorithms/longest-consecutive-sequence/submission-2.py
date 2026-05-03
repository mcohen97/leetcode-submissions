class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        numbersSeen = {}

        for num in nums:
            if num not in numbersSeen:
                if num - 1 in numbersSeen:
                    numbersSeen[num] = numbersSeen[num - 1] + 1
                else:
                    numbersSeen[num] = 1
                    
                i = num + 1
                while i in numbersSeen:
                    numbersSeen[i] = numbersSeen[i-1] + 1
                    i+=1
                
        
        return max(numbersSeen.values())

            
            

        