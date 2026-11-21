class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}

        for i in range(len(nums)):
            lookingfor = target - nums[i]
            if lookingfor in hashmap:
                return [hashmap[lookingfor], i]
            else:
                hashmap[nums[i]] = i