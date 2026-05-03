class Solution:

    operators = ['+', '-', '*', '/']

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in self.operators:
                stack.append(int(token))
                continue

            val1 = int(stack.pop())
            val2 = int(stack.pop())

            newValue = None
            if token == '+':
                newValue = val1 + val2
            elif token == '-':
                newValue = val2 - val1
            elif token == '*':
                newValue = val1 * val2
            elif token == '/':
                newValue = int(val2 / val1)

            stack.append(newValue)
               
        return stack[0]
                