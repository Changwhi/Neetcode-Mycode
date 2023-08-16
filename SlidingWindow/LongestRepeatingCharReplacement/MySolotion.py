class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # understand a problem
            # find longest repeating character
            # you can change any character for k times
            # given string consists of only uppercases
        # Exploer concreate example
            # ABAB, K = 2
                # AAAA, return 4
            # AABABBA, K = 1
                # AAAABBA, return 4
            # AABBBB, K = 2
                # BBBBBB, return 5
        # Solve/Simplify
            # count a number of the same letter
            # if k = 2, you can keep counting twice if you encounter the different letter
        container = {}
        leftPointer = 0
        res = 0
        maxLength = 0
        for rightPointer in range(len(s)):
            container[s[rightPointer]] = 1 + container.get(s[rightPointer], 0)
            maxLength = max(maxLength, container[s[rightPointer]])
            while (rightPointer - leftPointer + 1) - maxLength > k:
                container[s[leftPointer]] -= 1
                leftPointer += 1
            res = max(res, rightPointer - leftPointer + 1)
        return res
