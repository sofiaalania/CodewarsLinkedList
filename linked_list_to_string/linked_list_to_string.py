def stringify(node):
    cur = node
    res = ''
    if not cur:
        return "None"
    while cur:
        res+=f'{cur.data} -> '
        cur = cur.next
    res+= f'None'
    return res