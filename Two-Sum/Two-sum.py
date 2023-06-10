class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        prevMapping = {}  # dictionary to store index number and value

        for index, value in enumerate(nums):
            left = target - value  # find a number to meet target value

            if left in prevMapping:  # Check if there is a value, which we look for
                return [prevMapping[left], index]
            prevMapping[value] = index  # Add a value and index number in a dictionary
        print("working")
        return


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(nums, target))
