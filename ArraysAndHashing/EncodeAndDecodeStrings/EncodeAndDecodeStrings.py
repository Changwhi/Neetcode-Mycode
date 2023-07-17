class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        encodedWord = ""
        for word in strs:
            encodedWord = encodedWord + word + ":;"
        print(encodedWord)
        return encodedWord

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        decodedList = []
        word = ""
        for letter in str:
            print(letter)
            if letter == ";" and word[-1] == ":":
                decodedList.append(word[:-1])
                word = ""
                print(decodedList)
            else:
                word += letter
        return decodedList
