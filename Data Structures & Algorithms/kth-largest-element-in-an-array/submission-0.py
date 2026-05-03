class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        l, r = 0, len(nums) - 1
        pivot = self.partition(nums, l, r)

        while pivot != k - 1:
        
            if pivot < k - 1:
                l = pivot + 1
            else:
                r = pivot - 1
            pivot = self.partition(nums, l, r)
        
        return nums[pivot]

    def partition(self, nums: List[int], l: int, r: int) -> int:
        pivot = r

        aux = l

        for i in range(l, r):
            if nums[i] > nums[pivot]:
                nums[aux], nums[i] = nums[i], nums[aux]
                aux += 1

        nums[aux], nums[pivot] = nums[pivot], nums[aux]
        print(nums)
        return aux


        