class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        i = 0
        j = len(nums) - 1

        while i <= j:
            nums[i] = nums[i] * nums[i]
            i = i + 1
        nums.sort()
        return nums