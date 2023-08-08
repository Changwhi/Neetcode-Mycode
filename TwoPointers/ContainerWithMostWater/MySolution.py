class Solution:
    def maxArea(self, height: List[int]) -> int:
        ptr1 = 0
        ptr2 = len(height) - 1
        result = 0

        while (ptr1 < ptr2):
            maxHeight = min(height[ptr1], height[ptr2])
            distance = ptr2 - ptr1
            tempResult = distance * maxHeight
            if tempResult > result:
                result = tempResult
            if height[ptr1] < height[ptr2]:
                ptr1 += 1
            else:
                ptr2 -= 1
        return result






