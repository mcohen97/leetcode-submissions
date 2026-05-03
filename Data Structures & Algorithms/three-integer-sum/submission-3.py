class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        i = 0

        while i < len(nums):
            j = i + 1
            k = len(nums) - 1
            
            first = nums[i]

            while j < k:
                second = nums[j]
                third = nums[k]

                if first + second + third == 0:
                    res.append([first, second, third])
                    while j < len(nums) - 1 and nums[j+1] == nums[j]:
                        j += 1
                    j += 1
                elif first + second + third > 0:
                    k -= 1
                else:
                    j += 1

            while i < len(nums) - 1 and nums[i+1] == nums[i]:
                i += 1

            i += 1
            
        
        return res

            

    

        