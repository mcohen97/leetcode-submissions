class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2


            if target == nums[m]:
                return m

            isLeftPortion = nums[m] >= nums[l]

            if target < nums[m]:
                if isLeftPortion:
                    if target < nums[l]:
                        l = m + 1
                    else:
                        r = m - 1
                else:
                    r = m - 1
            else:
                if isLeftPortion:
                    l = m + 1
                else:
                    if target > nums[r]:
                        r = m - 1
                    else:
                        l = m + 1
            
        return -1