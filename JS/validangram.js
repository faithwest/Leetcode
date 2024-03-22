// class Solution:
//     def isAnagram(self, s: str, t: str) -> bool:
//         """
//         Checks if two strings are anagrams.

//         Args:
//             s: The first string.
//             t: The second string.

//         Returns:
//             True if t is an anagram of s, False otherwise.
//         """

//         if len(s) != len(t):
//             return False

//         char_count = {}
//         for char in s:
//             char_count[char] = char_count.get(char, 0) + 1

//         for char in t:
//             if char not in char_count or char_count[char] == 0:
//                 return False
//             char_count[char] -= 1

//         return True

// # Example usage
// s = "anagram"
// t = "nagaram"
// solution = Solution()
// result = solution.isAnagram(s, t)
// print(result)  # Output: True
