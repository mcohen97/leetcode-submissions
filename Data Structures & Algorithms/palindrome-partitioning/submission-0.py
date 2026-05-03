'''
Intuition:

What makes a palindrome. At most one of chars is odd in the word, rest are even (or all even)
given a smaller subproblem. We can build iteratively on it. We add the current letter in all the sublists


'''


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isPalindrome(w):
            i, j = 0, len(w) - 1
            while i < j:
                if w[i] != w[j]:
                    return False
                i += 1
                j -= 1
            return True

        def bt(i, partition):
            if i == len(s):
                res.append(partition.copy())
                return

            j = i
            while j < len(s):
                substr = s[i:j + 1]
                if isPalindrome(substr):
                    partition.append(substr)
                    bt(j + 1, partition)
                    partition.pop()

                j += 1

        bt(0, [])
        return res
            

        