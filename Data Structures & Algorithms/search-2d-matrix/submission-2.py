class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t, b, r, l = 0, len(matrix) - 1, len(matrix[0]) - 1, 0

        while l <= r and t <= b:
            row = (t + b) // 2

            if target < matrix[row][0]:
                b = row - 1
            elif target > matrix[row][-1]:
                t = row + 1
            else:
                while l <= r:
                    mid = (l + r) // 2

                    if matrix[row][mid] == target:
                        return True
                    elif target < matrix[row][mid]:
                        r = mid - 1
                    else:
                        l = mid + 1

        return False