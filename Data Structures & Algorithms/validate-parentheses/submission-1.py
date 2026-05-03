class Solution:
    def isValid(self, s: str) -> bool:
        openingBrackets ={'(': ')', '{': '}', '[': ']'}
        closingBrackets = {')': '(', '}' : '{', ']': '['}

        stack = []

        for c in s: 
            if c in closingBrackets and len(stack) > 0 and stack[-1] == closingBrackets[c]:
                stack.pop()
            else:
                stack.append(c)
        
        return len(stack) == 0

        


    
    


        