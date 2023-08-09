class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        ptrL, ptrR = 0, len(height)-1
        maxLeft = height[ptrL]
        maxRight = height[ptrR]
        result = 0

        while ptrL < ptrR:
            if height[ptrL] < height[ptrR]:
                ptrL += 1
                maxLeft = max(maxLeft, height[ptrL])
                result += (maxLeft - height[ptrL])
            else:
                ptrR -= 1
                maxRight = max(maxRight, height[ptrR])
                result += (maxRight - height[ptrR])
        return result

