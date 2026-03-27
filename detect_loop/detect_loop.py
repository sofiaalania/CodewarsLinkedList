def loop_size(node):
    slow = node
    fast = node
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            slow = fast

            while fast!=slow:
                fast = fast.next
                slow = slow.next
            begin = slow
            len = 0
            while True:
                slow = slow.next
                len += 1
                if slow == begin:
                    return len
            
            
                
            