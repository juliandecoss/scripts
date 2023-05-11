from copy import deepcopy
class Solution:
    def asteroidCollision(self, asteroids: list) -> list:
        res = []
        jump = False
        for pos,value in enumerate(asteroids):
            while len(res) and res[-1] > 0 and value <0:
                if res[-1] > -1*value:
                    jump = True
                    break
                elif res[-1] < -1*value:
                    res.pop()
                elif res[-1] == -1*value:
                    jump = True
                    res.pop()
                    break
            if not jump:
                res.append(value)
            jump = False
        return res

sol = Solution()


print(sol.asteroidCollision([8,-8]))