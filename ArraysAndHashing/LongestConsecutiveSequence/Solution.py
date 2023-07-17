class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numsSet = set(nums)  # no duplicate element
        result = 0
        for number in nums:
            if (number -1) not in numsSet:
                length = 1
                while number + length in numsSet:
                    length += 1
                result = max(result, length)
        return result
