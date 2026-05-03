class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        posAndSpeed = zip(position, speed)
        posAndSpeed = sorted(posAndSpeed, key=lambda tup: tup[0], reverse=True)

        def calculateTimeToDestiny(pos: int, speed: int):
            return (target - pos) / speed

        for pos, speed in posAndSpeed:
            timeToDestiny = calculateTimeToDestiny(pos, speed)
            if not stack:
                stack.append(timeToDestiny)
            elif stack and timeToDestiny > stack[-1]:
                stack.append(timeToDestiny)
        
        return len(stack)

        



