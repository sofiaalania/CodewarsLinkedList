from preloaded import Node

def swap_pairs(head):
    if not head or not head.next:
        return head
    second = new_head = head.next 
    first = head
    prev = None

    while second and first:
        new_first = second.next
        first.next = new_first
        if new_first:
            new_second = second.next.next
        else:
            new_second = None
        second.next = first
        if prev:
            prev.next = second
        prev = first
        first = new_first
        second = new_second
    return new_head
    