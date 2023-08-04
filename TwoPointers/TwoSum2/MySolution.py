class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        basket = {}

        for index, value in enumerate(numbers):
            requiredSecondValue = target - value

            if requiredSecondValue in basket:
                return (basket[requiredSecondValue] + 1, index + 1)
            basket[value] = index

        # using dictionary instead of two pointer
