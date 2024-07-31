# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
def length_of_longest_substring(s: str) -> int:
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length
def length_of_longest_substring(s):
    char_index = {}
    max_length = 0
    start = 0

    for i, char in enumerate(s):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        char_index[char] = i
        max_length = max(max_length, i - start + 1)
    
    return max_length

# Example usage
s = "abcabcbb"
print(length_of_longest_substring(s))  # Output: 3

s = "bbbbb"
print(length_of_longest_substring(s))  # Output: 1

s = "pwwkew"
print(length_of_longest_substring(s))  # Output: 3
def length_of_longest_substring(s):
    char_index = {}
    max_length = 0
    start = 0

    for i, char in enumerate(s):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        char_index[char] = i
        max_length = max(max_length, i - start + 1)
    
    return max_length

# Example usage
s = "abcabcbb"
print(length_of_longest_substring(s))  # Output: 3

s = "bbbbb"
print(length_of_longest_substring(s))  # Output: 1

s = "pwwkew"
print(length_of_longest_substring(s))  # Output: 3
