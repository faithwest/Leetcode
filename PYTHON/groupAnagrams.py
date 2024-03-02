# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]
 

# Constraints:

# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.



#SOLUTION################################################################

class Solution(object):
    def groupAnagrams(self,strs):
        # Initialize a dictionary to store word_groups of anagrams
        word_groups = {}

        # Iterate through each string in the input list
        for word in strs:
            # Generate a key by sorting the characters of the word
            sort_word = ''.join(sorted(word)) # Sort
            
            # If the key is not in the dictionary, add it with an empty list as its value
            if sort_word not in word_groups:
                word_groups[sort_word] = []

            # Append the word to the list corresponding to its key
            word_groups[sort_word].append(word)

        # Return the values (lists of anagrams) from the dictionary
        return list(word_groups.values())

# Example usage:
strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
strs2 = [""]
strs3 = ["a"]

solution = Solution()
print(solution.groupAnagrams(strs1))  # Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
print(solution.groupAnagrams(strs2))  # Output: [[""]]
print(solution.groupAnagrams(strs3))  # Output: [["a"]]
