class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        hashmap = {}

        for i in range(len(numbers)):
            lookingfor = target - numbers[i]
            if lookingfor in hashmap:
                return [hashmap[lookingfor]+1, i+1]
            else:
                hashmap[numbers[i]] = i