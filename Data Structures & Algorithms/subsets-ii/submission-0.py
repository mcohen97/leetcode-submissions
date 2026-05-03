'''
Intuition:

[1,2,1]

'''

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def bt(i, cur):
            if i >= len(nums):
                res.append(cur.copy())
                return
            
            cur.append(nums[i])
            bt(i + 1, cur)
            cur.pop()

            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1

            bt(i+1, cur)

        bt(0, [])
        return res 

        

