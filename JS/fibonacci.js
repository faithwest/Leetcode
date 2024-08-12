// function fibonacci(n) {
//     const seq = [0, 1];
//     for (let i = 2; i < n; i++) {
//         seq.push(seq[i - 1] + seq[i - 2]);
//     }
//     return seq;
// }
// console.log(fibonacci(10)); // Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

// function flattenArray(arr) {
//     return arr.reduce((acc, val) => Array.isArray(val) ? acc.concat(flattenArray(val)) : acc.concat(val), []);
// }
// console.log(flattenArray([1, [2, [3, [4, 5]]]])); // Output: [1, 2, 3, 4, 5]
def product_except_self(nums):
    length = len(nums)
    answer = [0] * length

    answer[0] = 1
    for i in range(1, length):
        answer[i] = nums[i - 1] * answer[i - 1]

    right = 1
    for i in reversed(range(length)):
        answer[i] = answer[i] * right
        right *= nums[i]

    return answer

# Example usage
nums = [1,2,3,4]
print(product_except_self(nums))  # Output: [24,12,8,6]

nums = [-1,1,0,-3,3]
print(product_except_self(nums))  # Output: [0,0,9,0,0]
