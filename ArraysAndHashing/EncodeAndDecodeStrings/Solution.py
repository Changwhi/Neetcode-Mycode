class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        encodedWord = ""
        for word in strs:
            encodedWord += str(len(word)) + "#" + word
        print(encodedWord)
        return encodedWord

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        decodedList = []
        pointer = 0

        while pointer < len(str):
            startIndex = pointer
            while str[startIndex] != '#':
                startIndex += 1
            length = int(str[pointer:startIndex])
            decodedList.append(str[startIndex + 1 : startIndex + 1 + length])
            pointer = startIndex + 1 + length
        return decodedList
