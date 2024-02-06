# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally,
# pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def has_cycle(head):
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next  # Move slow pointer by one step
        fast = fast.next.next  # Move fast pointer by two steps

        if slow == fast:
            return True  # Cycle detected

    return False  # No cycle found


# head, pos = [3, 2, 0, -4], 1

node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)

# Connect the nodes to form the list 3 -> 2 -> 0 -> -4
node1.next = node2
node2.next = node3
node3.next = node4

# Create a cycle as indicated by pos = 1 (0-based index)
# Linking node4's next to node2 creates the cycle
node4.next = node2

# Check if the linked list has a cycle
print(has_cycle(node1))  # Output: True

# head , pos = [1,2],  0

node1 = ListNode(1)
node2 = ListNode(2)

# Connect the nodes to form the list 1 -> 2
node1.next = node2
node2.next = node1

print(has_cycle(node1))

# head , pos = [1], -1

node1 = ListNode(1)
node2 = None
node1.next = node2

print(has_cycle(node1))
