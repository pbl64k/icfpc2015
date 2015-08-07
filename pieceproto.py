from utils import *

class PieceProto(object):
    def __init__(self, data):
        self.pivot = translate((data['pivot']['x'], data['pivot']['y']))
        mems = map(lambda x: sub(x, self.pivot), map(translate, map(lambda x: (x['x'], x['y']), data['members'])))
        self.mems = []
        seen = set()
        for ix in range(6):
            tmems = tuple(sorted(mems))
            if tmems in seen:
                break
            self.mems.append(mems)
            seen.add(tmems)
            mems = map(lambda x: mem_rot(x, True), mems)
        orig_pos = map(untranslate, self.mems[0])
        orig_x = map(lambda x: x[0], orig_pos)
        orig_y = map(lambda x: x[1], orig_pos)
        self.min_x = min(orig_x)
        self.max_x = max(orig_x)
        self.min_y = min(orig_y)
        self.max_y = max(orig_y)

