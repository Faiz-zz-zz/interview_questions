class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        interLeftX = max(A, E)
        interLeftY = max(F, B)
        interRightX = min(G, C)
        interRightY = min(D, H)

        print(interLeftX, interLeftY, interRightX, interRightY)

        if interLeftX <= interRightX and interRightY >= interLeftY:
            return abs((A - C) * (B - D)) + abs((E - G) * (F - H)) - abs((interLeftX - interRightX) * (interLeftY - interRightY))
        else:
            return abs((A - C) * (B - D)) + abs((E - G) * (F - H))


print(Solution().computeArea(-2, -2, 2, 2, 1, -3, 3, -1))