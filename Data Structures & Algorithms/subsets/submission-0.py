class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sol = []

        def bt(i, curSet):
            nonlocal sol
            if i >= len(nums):
                sol.append(curSet.copy())
                return

            # Set with the current number
            curSet.append(nums[i])
            bt(i+1, curSet)

            # Set without the current number
            curSet.pop()
            bt(i+1, curSet)

        bt(0, [])

        return sol

