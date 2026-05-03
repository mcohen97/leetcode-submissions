class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        opening, closing = 0, 0

        res = []

        comb = ""

        def bt():
            nonlocal opening, closing, res, comb
            if opening > n or closing > n:
                return

            if opening == n and closing == n:
                res.append(comb)
            
            if opening > closing:
                comb += ")"
                closing += 1
                bt()
                closing -= 1
                comb = comb[:-1]

            comb += "("
            opening += 1
            bt()
            opening -= 1
            comb = comb[:-1]
        
        bt()
        return res