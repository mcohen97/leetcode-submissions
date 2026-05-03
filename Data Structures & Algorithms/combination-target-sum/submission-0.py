class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curCombination = []

        def bt(i, curSum):
            if curSum == target:
                res.append(curCombination.copy())
                return
            
            if curSum > target:
                return

            if i >= len(nums):
                return


            # Don't include this number
            bt(i+1, curSum)

            originalSum = curSum
            while curSum <= target:
                curCombination.append(nums[i])
                curSum += nums[i]
                bt(i + 1, curSum)

            while originalSum != curSum:
                curSum -= curCombination.pop()


        bt(0, 0)
        return res

        

