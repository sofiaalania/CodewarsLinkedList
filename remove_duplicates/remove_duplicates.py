class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):

    cur = head
    while cur and cur.next:
        if cur.data == cur.next.data:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return head
        