class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    if not head or not head.next:
        raise ValueError
    cur = head
    head2 = head.next
    while cur.next and cur.next.next:
        new_cur = cur.next
        cur.next = cur.next.next
        new_cur.next = cur.next.next
        cur = cur.next

    if cur.next:
        cur.next = None
    return Context(head, head2)
        