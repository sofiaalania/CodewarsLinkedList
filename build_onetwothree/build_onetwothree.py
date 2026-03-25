from preloaded import Node

'''
Node is defined in preloaded like this:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
    
def push(head, data):
    node = Node(data)
    node.next = head
    return  node

def build_one_two_three():
    head = None
    for i in range(3,0,-1):
        head = push(head, i)
    return head