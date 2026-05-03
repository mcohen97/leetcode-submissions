class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        candidates.sort()

        print(candidates)

        def bt(i, cur, curSum):
            print(i, cur, curSum)
            if curSum == target:
                res.append(cur.copy())
                return

            if i >= len(candidates) or curSum > target:
                return

            e = candidates[i]


            cur.append(e)
            bt(i+1, cur, curSum + e)
            cur.pop()

            nextPos = i

            while nextPos < len(candidates) and candidates[nextPos] == e :
                nextPos += 1

            bt(nextPos, cur, curSum)


        bt(0, [], 0)

        return res        