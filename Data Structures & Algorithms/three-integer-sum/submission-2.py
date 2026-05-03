class Solution:

    # [-4, -1,-1, 0, 1,2]
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        print("nums:", nums)
        solution = []

        i = 0

        while i < len(nums) - 2:
            first = nums[i]

            j = i + 1
            k = len(nums) -1

            while j < k:
                if nums[j] + nums[k] == -first:
                    solution.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                elif nums[j] + nums[k] > -first:
                    k -= 1
                else:
                    j += 1
                
           
            i += 1

            while nums[i] == nums[i-1] and i < len(nums) - 2:
                i += 1
            

        return solution
                
