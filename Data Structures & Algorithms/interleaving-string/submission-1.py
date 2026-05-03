class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        cache = {("", "", ""): True}

        def memo(s1, s2, s3):
            key = (s1, s2, s3)
            if key in cache:
                return cache[key]
            
            cache[key] = False

            if not s3:
                return cache[key]
                
            if s1 and s1[0] == s3[0]:
                cache[key] = cache[key] or memo(s1[1:], s2, s3[1:])

            if s2 and s2[0] == s3[0]:
                cache[key] = cache[key] or memo(s1, s2[1:], s3[1:])

            print(key)
            return cache[key]

        memo(s1, s2, s3)
        return cache[(s1, s2, s3)]

            
            
            
            


