
def display(w, h, view):
    f = False
    l = ''
    for x in range(w):
        l += ' / \\'
    l += '\n'
    for y in range(h):
        if f: l += '  '
        f = not f
        l += '| '
        for x in range(w):
            l += view[x][y]
            l += ' | '
        l += '\n'
        for x in range(w):
            if f:
                l += ' \ /'
            else:
                l += ' / \\'
        if f:
            l += ' \\'
        else:
            l += ' /'
        l += '\n'
    print l

