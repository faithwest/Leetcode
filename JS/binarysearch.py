def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7
print(binary_search(arr, target))  # Output: 6

##################################################
##linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def find_middle(head):
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow

# Example usage:
# Creating a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

middle_node = find_middle(head)
print(middle_node.val)  # Output: 3
def sum_even_numbers(nums):
    """
    Calculates the sum of all even numbers in a list.

    Args:
    nums (list of int): List of integers.

    Returns:
    int: Sum of all even numbers in the list.
    """
    sum_even = 0
    for num in nums:
        if num % 2 == 0:
            sum_even += num
    return sum_even

# Example usage:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = sum_even_numbers(numbers)
print(f"The sum of even numbers in the list is: {result}")
