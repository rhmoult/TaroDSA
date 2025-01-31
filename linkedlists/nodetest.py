def nodes_to_array(head):
    outputArray = []
    while head is not None:
        outputArray.append(head.value)
        head = head.next
    return outputArray
    ...


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

print(nodes_to_array(a))
