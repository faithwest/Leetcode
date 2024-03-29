# def solution():
#     #empty dict to store the frequency of letters
#     freq={}
#     #instance
#     P = 'abc'
#     Q = 'bcd'
#     P==Q#not necessary

#     #combine and chage to lower case
#     both = (P + Q).lower()
#     print(both)

#     #iterate over the letters
#     for char in both: #loop to iterate over the string both
#         if char not in freq:#if not a character in the freq
#             freq[char] == freq[char]
#             return freq[char]
#         else:
#             freq[char]+=1#if exist,record the

#     min_frequency = min(freq.values())

#     print(min_frequency)        

# # Call the function
# solution()
# def solution(P, Q):
#     N = len(P)
#     distinct_letters = set()
#     must_have_letters = set()

#     for i in range(N):
#         if P[i] != Q[i]:
#             distinct_letters.add(P[i])
#             distinct_letters.add(Q[i])
#         else:
#             must_have_letters.add(P[i])

#     return max(len(must_have_letters), 1)  # Ensure at least one distinct letter

# p=["axxz"]
# q=[ "yzwy"]
# print(solution(p, q)) #

# # array=[1,3,7,2,1,5]
# def solution(B):
#     n = len(B)
#     cat = set()
#     for i in range(n):
#         if B[i] > 0:
#             cat.add(B[i])
#             print(cat)
#             return list(cat)

# print(solution([1,3,7,2,1,5]))
# We are given two strings P and Q, each consisting of N lowercase English letters. For each position in the strings, we have to choose one letter from either P or Q, in order to construct a new string S, such that the number of distinct letters in S is minimal. Our task is to find the number of distinct letters in the resulting string S.

# For example, if P = "ca" and Q = "ab", S can be equal to: "ca", "cb", "aa" or "ab". String "aa" has only one distinct letter ('a'), so the answer is 1 (which is minimal among those strings).

# Write a function:

# def solution(P, Q)

# that, given two strings P and Q, both of length N, returns the minimum number of distinct letters of a string S, that can be constructed from P and Q as described above.

# Examples:

# 1. Given P = "abc", Q = "bcd", your function should return 2. All possible strings S that can be constructed are: "abc", "abd", "acc", "acd", "bbc", "bbd", "bcc", "bcd". The minimum number of distinct letters is 2, which be obtained by constructing the following strings: "acc", "bbc", "bbd", "bcc".

# 2. Given P = "axxz", Q = "yzwy", your function should return 2. String S must consist of at least two distinct letters in this case. We can construct S = "yxxy", where the number of distinct letters is equal to 2, and this is the only optimal solution.

# 3. Given P = "bacad", Q = "abada", your function should return 1. We can choose the letter 'a' in each position, so S can be equal to "aaaaa".

# 4. Given P = "amz", Q = "amz", your function should return 3. The input strings are identical, so the only possible S that can be constructed is "amz", and its number of distinct letters is 3.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..200,000];
# strings P and Q are both of length N;
# strings P and Q are made only of lowercase letters (a−z);
# strings P and Q contain a total of at most 20 distinct letters.

def generate_and_count_distinct(P, Q):
    def generate_strings(current_string, index):
        # Base case: if index reaches the length of P and Q, add the current string to the result
        if index == len(P):
            result.append(current_string)
            return

        # Add the current characters from P and Q at the index to the current string
        generate_strings(current_string + P[index], index + 1)
        generate_strings(current_string + Q[index], index + 1)

    distinct_letters = set(P + Q)
    distinct_count = len(distinct_letters)

    result = []
    generate_strings("", 0)
    variations = result

    return distinct_count, variations

# Example usage:
P1 = "bacad"
Q1 = "abada"
distinct_count1, variations1 = generate_and_count_distinct(P1, Q1)
print("Distinct count:", distinct_count1)
print("Variations:", variations1)

P2 = "abc"
Q2 = "bcd"
distinct_count2, variations2 = generate_and_count_distinct(P2, Q2)
print("Distinct count:", distinct_count2)
print("Variations:", variations2)

P3 = "amz"
Q3 = "amz"
distinct_count3, variations3 = generate_and_count_distinct(P3, Q3)
print("Distinct count:", distinct_count3)
print("Variations:", variations3)
# def solution(string):
#     distinct = set(string)
#     return len(distinct)

# def generate_variations(P, Q):
#     def generate_strings(current_string, index):
#         # Base case: if index reaches the length of P and Q, add the current string to the result
#         if index == len(P):
#             result.append(current_string)
#             return

#         # Add the current characters from P and Q at the index to the current string
#         generate_strings(current_string + P[index], index + 1)
#         generate_strings(current_string + Q[index], index + 1)

#     result = []
#     generate_strings("", 0)
#     return result

# # Example usage:
# P1 = "bacad"
# Q1 = "abada"
# variations1 = generate_variations(P1, Q1)
# distinct_counts1 = [solution(variation) for variation in variations1]
# print("Distinct counts for each variation:", min(distinct_counts1))

# P2 = "abc"
# Q2 = "bcd"
# variations2 = generate_variations(P2, Q2)
# distinct_counts2 = [solution(variation) for variation in variations2]
# print("Distinct counts for each variation:", min(distinct_counts2))

# P3 = "amz"
# Q3 = "amz"
# variations3 = generate_variations(P3, Q3)
# distinct_counts3 = [solution(variation) for variation in variations3]
# print("Distinct counts for each variation:", min(distinct_counts3))
