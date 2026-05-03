class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minSpeed = 1
        maxSpeed = max(piles)
        sol = math.inf

        while minSpeed <= maxSpeed:
            m = (minSpeed + maxSpeed) // 2

            time = 0

            for pile in piles:
                time += math.ceil(pile / m)
            
            if time <= h:
                sol = min(sol, m)
                maxSpeed = m - 1
            else:
                minSpeed = m + 1
            
        return sol
        