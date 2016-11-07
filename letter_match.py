class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        counter = {}
        for letter in s:
            if letter in counter:
                print(letter, counter)
                counter[letter] += 1
            else:
                counter[letter] = 1
        sub_counter = {}
        for letter in t:
            if letter in sub_counter:
                sub_counter[letter] += 1
            else:
                sub_counter[letter] = 1
        for letter in counter:
            if letter in sub_counter:
                if sub_counter[letter] != counter[letter]:
                    return letter
            else: return letter

print(Solution().findTheDifference("abcd", "abcde"))
