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


def fill_values(head, values):
    if head is None:
        return values
    values.append(head.value)
    return fill_values(head.next, values)


def linked_list_values(head):
    values = []
    fill_values(head, values)
    return values


print(linked_list_values(a))
