class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r: 
            leftNum = numbers[l]
            rightNum = numbers[r]
            currentSum = leftNum + rightNum

            if currentSum == target:
                return [l+1, r+1]
            elif currentSum < target:
                l += 1
            else:
                r -= 1

        return []
            