class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digitMap = {
            2: ["A", "B", "C"],
            3: ["D", "E", "F"],
            4: ["G", "H", "I"],
            5: ["J", "K", "L"],
            6: ["M", "N", "O"],
            7: ["P", "Q", "R", "S"],
            8: ["T", "U", "V"],
            9: ["W", "X", "Y", "Z"]
        }

        combinations = [""]

        for digit in digits:
            tmp = []
            letters = digitMap[int(digit)]
            for comb in combinations:
                for letter in letters:
                    tmp.append(comb + letter.lower())
            combinations = tmp

        return combinations



