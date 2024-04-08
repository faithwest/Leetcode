// Problem: Container With Most Water

// Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

function maxArea(height) {
    let maxArea = 0;
    let left = 0;
    let right = height.length - 1;

    while (left < right) {
        // Calculate area between left and right pointer
        const area = Math.min(height[left], height[right]) * (right - left);
        maxArea = Math.max(maxArea, area);

        // Move the pointer with smaller height towards the other pointer
        if (height[left] < height[right]) {
            left++;
        } else {
            right--;
        }
    }

    return maxArea;
}

// Example usage:
const height = [1, 8, 6, 2, 5, 4, 8, 3, 7];
console.log(maxArea(height)); // Output: 49


// def maxArea(height):
//     max_area = 0
//     left = 0
//     right = len(height) - 1
    
//     while left < right:
//         # Calculate area between left and right pointer
//         area = min(height[left], height[right]) * (right - left)
//         max_area = max(max_area, area)
        
//         # Move the pointer with smaller height towards the other pointer
//         if height[left] < height[right]:
//             left += 1
//         else:
//             right -= 1
            
//     return max_area

// # Example usage:
// height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
// print(maxArea(height)) # Output: 49
