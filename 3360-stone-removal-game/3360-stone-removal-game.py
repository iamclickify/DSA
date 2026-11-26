class Solution:
    def canAliceWin(self, n: int) -> bool:
        stones = 10
        steps = 0

        while n >= stones:
            n = n - stones
            stones = stones - 1
            steps = steps + 1

        if steps % 2 == 0:
            return False
        else:
            return True