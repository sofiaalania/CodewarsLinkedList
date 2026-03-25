from preloaded import Node

def linked_list_from_string(list_repr: str) -> Node | None:
    null = ["null", "NULL", "nil", "nullptr", "null()", "None"]

    list_repr = list_repr.split(" -> ")
    if list_repr[0] in null:
        return None
    prev = Node(int(list_repr[0]))
    head = prev
    for i in list_repr[1:]:
        if i in null:
            break
        prev.next = Node(int(i))
        prev = prev.next
    return head