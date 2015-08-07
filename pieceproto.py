from utils import *

class PieceProto(object):
    def __init__(self, data):
        self.pivot = translate((data['pivot']['x'], data['pivot']['y']))
        self.mems = map(lambda x: sub(x, self.pivot), map(translate, map(lambda x: (x['x'], x['y']), data['members'])))
