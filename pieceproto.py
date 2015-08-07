from utils import *

class PieceProto(object):
    def __init__(self, data):
        self.pivot = translate((data['pivot']['x'], data['pivot']['y']))
        mems = map(lambda x: sub(x, self.pivot), map(translate, map(lambda x: (x['x'], x['y']), data['members'])))
        self.mems = []
        for ix in range(6):
            self.mems.append(mems)
            mems = map(lambda x: mem_rot(x, True), mems)

