class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next  # Store next node
        current.next = prev  # Reverse current node's pointer
        prev = current  # Move prev and current one step forward
        current = next_node
    return prev

# Helper function to print the linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

# Helper function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Example usage
values = [1, 2, 3, 4, 5]
head = create_linked_list(values)
print("Original Linked List:")
print_linked_list(head)

reversed_head = reverse_linked_list(head)
print("Reversed Linked List:")
print_linked_list(reversed_head)
