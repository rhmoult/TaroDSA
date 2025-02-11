from node import Node


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
    if head is None:
        return values
    values.append(head.value)
    return fill_values(head.next, values)


def linked_list_values(head):
    values = []
    return fill_values(head, values)


print(linked_list_values(a))
