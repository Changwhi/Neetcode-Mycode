class Solution:
    def twoSum(self, numbersd: List[int], target: int) -> List[int]:
        hash={}
        for key, num in enumerate(numbersd):
            if num in hash:
                return [hash[num] + 1,key + 1]
            else:
                hash[target-num]=key
