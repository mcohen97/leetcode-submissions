class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def bt(i):
            if i > len(nums) - 1:
                return [[]]
            
            sub = bt(i+1)

            res = []
            
            for comb in sub:
                for j in range(len(comb) + 1):
                    sol = comb.copy()
                    sol.insert(j, nums[i])
                    res.append(sol)

            return res

        return bt(0)