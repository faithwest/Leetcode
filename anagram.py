class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        flag = True
        if len(set(s))!=len(set(t)):
            return False
        else:
            for each in set(s):
                s.count(each)==t.count(each)
                if s.count(each)!=t.count(each):
                    flag= False
        return flag
        



##############################################################################
#DOES NOT PASS ALL TEST
# class Solution(object):
#     def isAnagram(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """

#         #if strings are not of the same length  then they cannot be anagram
#         flag=True
#         if len(s) != len(t):
#             return False

        #  Use sets to compare if the characters are the same in both strings
        # count_s = {}
        # count_t = {}
        #  for char in s:
        #      if char not in count_s:
                    #count_s[char] = count_s.get(char, 0) + 1

        #  for char in s:
        #      if char not in count_s:
                    #count_s[char] = count_s.get(char, 0) + 1

#         # If the sets are equal then the strings are anagrams. Otherwise they aren't.
#         return count_s == count_t

#         # Example usage:
# s = "anagram"
# t = "nagaram"
# print(Solution().isAnagram(s, t)) 