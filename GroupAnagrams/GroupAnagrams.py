class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        # loop through each word
        # store each character in dictionary
        # print out

        result = collections.defaultdict(list)

        for word in strs:
            key = [0] * 26  # 26 elements, index number represents the ASCII, value is the number of word

            for character in word:
                key[ord(character) - ord("a")] += 1  # a = 65. So, a to z is equal to 0 to 26
            result[tuple(key)].append(word)
        return result.values()

        # using hash map (dictionary)
        # convert character into number to use it as a index number
        # assign a key value as list(or tuple) to hashmap
        # using list to store data and maintain the order
