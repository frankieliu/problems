import os

class curler:
    def __init__(self, msg=None, outfile=None):
        self.msg = msg
        self.outfile = outfile
        pass

    def send(self):
        os.system(self.msg + ">> {}".format(self.outfile))
