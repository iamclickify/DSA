class Solution:
    def twosum(self, f, nums, result):
        i = f + 1
        j = len(nums) - 1

        while i < j:
            sum = nums[f] + nums[i] + nums[j]

            if sum > 0:
                j = j - 1
            elif sum < 0:
                i = i + 1
            else:
                result.append([nums[f], nums[i], nums[j]])
                i = i + 1
                j = j - 1

                while(i < j and nums[i] == nums[i-1]):
                    i = i + 1
                while(i < j and nums[j] == nums[j+1]):
                    j = j - 1
             
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        nums.sort()
        result = []

        for f in range(len(nums)-1):
            if nums[f] > 0:
                break
            if f == 0 or nums[f] != nums[f-1]:
                self.twosum(f, nums, result)

            f = f + 1

        return result
