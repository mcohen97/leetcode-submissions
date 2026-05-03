class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def bt(i, db, cur):
            if i >= len(nums):
                res.append(cur.copy())

            for num in nums:
                if num not in db:
                    db.add(num)
                    cur.append(num)
                    bt(i + 1, db, cur)
                    db.remove(cur.pop())
            
        
        bt(0, set(), [])

        return res        