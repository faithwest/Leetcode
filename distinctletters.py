def solution(P, Q):
    distinct_letters = set()
    for p, q in zip(P, Q):#zip is used to iterate simultanously over p and q
        #<used to check if p is than q
        #if a character in p comes before a character in q records
        distinct_letters.add(p if p < q else q)
    return len(distinct_letters)

print(solution("abc", "bcd"))    # Output: 2
print(solution("axxz", "yzwy"))  # Output: 2
print(solution("bacad", "abada"))# Output: 1
print(solution("amz", "amz"))    # Output: 3