class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        solution = []

        def backtracking(closeCount: int, openCount: int):
            if openCount == n and closeCount == n:
                solution.append("".join(stack))
                return
            
            if openCount > closeCount and closeCount < n:
                stack.append(")")
                backtracking(closeCount + 1, openCount)
                stack.pop()
            
            if openCount < n:
                stack.append("(")
                backtracking(closeCount, openCount + 1)
                stack.pop()

        backtracking(0, 0)
        return solution


