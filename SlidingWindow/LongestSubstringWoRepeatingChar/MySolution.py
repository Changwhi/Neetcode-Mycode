class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Understand the problem
            # given a string.
            # A function should find the number of
            # 1. longestcontiguous
            # 2. non-empty
            # 3. withouth reapeating characters.
        # Explore Concreate Examples
            # abcda - 4
            # ab dee - 2
        # Solve/simplify
            # code below
            # You can not use index with set
            # You can use index with a given list to move the pointer
        # Look back and Refactor
            # delete the if statement
        res, count = 0, 0
        secondS = set()
        for char in s:
            #if char in secondS:
            while char in secondS:
                secondS.remove(s[count])
                count += 1
            secondS.add(char)
            res = max(res, len(secondS))
        return res
