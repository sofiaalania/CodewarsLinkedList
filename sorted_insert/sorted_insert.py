""" For your information:
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
"""

def sorted_insert(head, data):
    new_node = Node(data)
    if not head or head.data > data:
        new_node.next = head
        return new_node

    cur = head
    while cur:
        if cur.data > data:
            prev.next = new_node
            new_node.next = cur
            return head
        prev = cur
        cur = cur.next
    prev.next = new_node
    return head