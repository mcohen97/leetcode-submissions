class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for i in range(len(s))]

        def endsWithWord(i, word):
            # print("compare", word, "with", s[:i+1])
            if len(word) > i + 1:
                return False
            
            for j in range(len(word)):
                if word[j] != s[i - len(word) + 1 + j]:
                    # print(word[j], "!=", s[i - len(word) + 1 + j])
                    return False
            
            # print("Same word")
            return True


        for i in range(len(s)):
            for word in wordDict:
                if endsWithWord(i, word):
                    dp[i] = i + 1 == len(word) or dp[i - len(word)]
                    if dp[i]:
                        break
        # print(dp)
        return dp[-1]
        