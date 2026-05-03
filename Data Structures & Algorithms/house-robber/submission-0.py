'''
constraints:
rob(i) = max(rob(i + 1), nums[i] + rob(i + 2))
rob[n] = nums[n]
rob[n + 1] = 0


[1,1,3,3] 0

[4, 4,3,3]

'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        two, one = 0, nums[-1]
        n = len(nums)

        for i in range(n - 2, -1, -1):
            tmp = one
            one = max(one, nums[i] + two)
            two = tmp
        
        return one
        

        