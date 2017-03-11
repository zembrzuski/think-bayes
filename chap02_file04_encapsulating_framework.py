from thinkbayes import Pmf

class Suite(Pmf):

    def __init__(self, hypo):
        Pmf.__init__(self)
        for hypo in hypo:
            self.Set(hypo, 1)
        self.Normalize()

    def Update(self, data):
        for hypo in self.Values():
            like = self.Likelihood(data, hypo)
            self.Mult(hypo, like)
        self.Normalize()

    def Print(self):
        for hypo, prob in self.Items():
            print(hypo, prob)

    def Likelihood(self, data, hypo):
        pass
