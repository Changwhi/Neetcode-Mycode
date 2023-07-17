class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        uniqueArray = list(set(nums))
        uniqueArray.sort()
        print(uniqueArray)

        if len(uniqueArray) == 1:
            return 1
        pointer = 1
        res = 0
        while pointer < len(uniqueArray):
            tempLength = 0
            while pointer < len(uniqueArray) and (uniqueArray[pointer - 1] + 1) == uniqueArray[pointer]:
                pointer += 1
                tempLength += 1
            tempLength += 1
            pointer += 1
            if res < tempLength:
                res = tempLength

        return res

