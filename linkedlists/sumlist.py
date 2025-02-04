from node import Node

a = Node(2)
b = Node(8)
c = Node(3)
d = Node(7)

a.next = b
b.next = c
c.next = d


# Time Complexity: O(n)
# Space Complexity: O(1)
def get_sum_list(head):
    sum = 0
    while head is not None:
        sum += head.value
        head = head.next
    return sum


# Time Complexity: O(n)
# Space Complexity: O(n)
def get_sum_list_recursive(head):
    if head is None:
        return 0

    return head.value + get_sum_list_recursive(head.next)


print(get_sum_list(a))
print(get_sum_list_recursive(a))
