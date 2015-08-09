
def rot_cw_x(x):
    return 0, x

def rot_cw_y(y):
    return -y, y

def rot_ccw_x(x):
    return x, -x

def rot_ccw_y(y):
    return -y, 0

def rot_cw_xy(x, y):
    x1, y1 = rot_cw_x(x)
    x2, y2 = rot_cw_y(y)
    return x1 + x2, y1 + y2

def rot_ccw_xy(x, y):
    x1, y1 = rot_cww_x(x)
    x2, y2 = rot_ccw_y(y)
    return x1 + x2, y1 + y2

def rot_cw_pos(pos):
    x, y = pos
    return rot_cw_xy(x, y)

def rot_ccw_pos(pos):
    x, y = pos
    return rot_ccw_xy(x, y)

rot_cache = {}

def mem_rot(pos, cw):
    k = (pos, cw)
    if k not in rot_cache:
        rot_cache[k] = rot_cw_pos(pos) if cw else rot_ccw_pos(pos)
    return rot_cache[k]

def translate(pos):
    x, y = pos
    sh = y / 2
    return x - sh, y

def untranslate(pos):
    x, y = pos
    sh = y / 2
    return x + sh, y

def add(pos1, pos2):
    return pos1[0] + pos2[0], pos1[1] + pos2[1]

def sub(pos1, pos2):
    return pos1[0] - pos2[0], pos1[1] - pos2[1]

def scale(pos, k):
    return pos[0] * k, pos[1] * k

ns_d = ((-1, 0), (0, -1), (1, -1), (1, 0), (0, 1), (-1, 1))
ns_d_hex = ((-1, 0), (1, 0), (0, 1), (-1, 1))

def ns(pos, hextris = True):
    p = translate(pos)
    r = []
    for d in ns_d:
        r.append(add(p, d))
    return map(untranslate, r)

def ns_hextris(pos, hextris = True):
    p = translate(pos)
    r = []
    for d in ns_d_hex:
        r.append(add(p, d))
    return map(untranslate, r)

