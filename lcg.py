
class Lcg(object):
    def __init__(self, seed):
        self.seed = seed
        self.st = seed

    def cur(self):
        return (self.st & 0b1111111111111110000000000000000) >> 16

    def adv(self):
        self.st = (1103515245 * self.st + 12345) % (0b100000000000000000000000000000000)

    def gen(self):
        x = self.cur()
        self.adv()
        return x

