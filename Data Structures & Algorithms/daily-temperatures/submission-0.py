class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        solution = [0 for t in temperatures]

        for i, temp in enumerate(temperatures):
            if not stack:
                stack.append((temp, i))
            else: 
                while stack and temp > stack[-1][0]:
                    prevTemp, pos = stack.pop()
                    solution[pos] = i - pos
                stack.append((temp, i))
        return solution

                

