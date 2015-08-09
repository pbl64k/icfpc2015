
class StSt(object):
    def __init__(self, l = None, r = None):
        if l is None:
            self.l = None
            self.r = None
        else:
            self.l = l
            self.r = r

    def seq(self, buf):
        if self.l is not None:
            self.l.seq(buf)
            buf.write(self.r)

