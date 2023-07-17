class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # Create an extra array.
        # Iterate through each number in the input array
        # For each number, multiply it by all the numbers in the extra array, excluding the number at the current index.
        # Store the product in the corresponding index of the extra array.
        # ---------------------------------------------------------------------------------------------
        # After attempting the initial approach, I realized it inmultiple times, which was not allowed.
        # I found a solution by utilizing prefix and postfix arrays to calculate the desired products.

        result = [1 for i in range(len(nums))]

        prefix = 1
        for index in range(len(nums)):
            result[index] = prefix
            prefix *= nums[index]

        postfix = 1
        for index in range(len(nums) - 1, -1, -1):
            result[index] *= postfix
            postfix *= nums[index]
        return result
