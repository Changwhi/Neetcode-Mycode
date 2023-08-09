class Solution:
    def trap(self, height: List[int]) -> int:
        ptr1 = 0
        result = 0
        block = 0
        for ptr2 in range(1,len(height)):
            if height[ptr1] == 0:
                ptr1 += 1
            elif ptr2-ptr1 > 1 and height[ptr1] <= height[ptr2]:
                result = result + block
                ptr1 = ptr2
                block = 0
            else:
                block = block + (height[ptr1] - height[ptr2])
                print(block)

        return result

