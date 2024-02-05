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

