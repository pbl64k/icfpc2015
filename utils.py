
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


