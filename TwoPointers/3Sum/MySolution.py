class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        result = []
        for index in range(len(nums)):
            if index > 0 and nums[index] == nums[index - 1]:
                continue

            l, r = index + 1, len(nums) - 1
            while l < r:
                calculation = nums[index] + nums[l] + nums[r]
                if  calculation < 0:
                    l += 1
                elif nums[index] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    result.append([nums[index], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return result
