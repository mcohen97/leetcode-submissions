class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = Counter(s1)

        l = r = 0

        while r < len(s2):
            if s2[r] not in counter:
                counter = Counter(s1)
                r += 1
                l = r
                continue

            print(s2[l], s2[r], counter)
            while counter[s2[r]] == 0 and l < r:
                counter[s2[l]] = counter[s2[l]] + 1
                l += 1
                
            counter[s2[r]] = counter[s2[r]] - 1
            
            if all(v == 0 for v in counter.values()):
                return True
            
            r+= 1
                        

        return False