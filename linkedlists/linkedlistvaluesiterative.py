class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")

a.next = b
b.next = c
c.next = d


# Time: O(n)
# Space: O(n)
def fill_values(head, values):
    while head is not None:
        values.append(head.value)
        head = head.next
    return values


def linked_list_values(head):
    values = []
    values = fill_values(head, values)
    return values


print(linked_list_values(a))
