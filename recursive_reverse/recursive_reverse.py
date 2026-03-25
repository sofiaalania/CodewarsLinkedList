class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    def nested(cur, prev):
        if not cur:
            return prev
        
        new = cur.next
        cur.next = prev

        return nested(new, cur)
    return nested(head, None)
    
            
            