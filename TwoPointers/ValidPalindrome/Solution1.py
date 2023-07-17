class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # convert each character into lowercase
        # convert each character into ACSII Code
        # check if each character is alphanumeric
        # if it is alphanumeric, store it into an array.
        # check if it is a palindrome

        result = ""
        for character in s:
            if character.isalnum():
                result += character.lower()
        reversed = result[::-1]
        return result == reversed


        # converted = ""
        # for char in s:
        #     lowerchar = char.lower()
        #     if ord(lowerchar) in range(48, 58) or ord(lowerchar) in range(97, 123):
        #         converted += lowerchar

        # if len(converted) == 0:
        #     return True

        # for pointer1 in range(len(converted)):
        #     if converted[pointer1] != converted[(pointer1+1) * -1]:
        #         return False
        # return True
