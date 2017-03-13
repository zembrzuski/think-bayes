from chap02_file04_encapsulating_framework import Suite


class Train(Suite):

    def Likelihood(self, data, hypo):
        if hypo < data:
            return 0
        return 1./hypo


hypos = xrange(1, 6)
print(hypos)
suite = Train(hypos)
suite.Update(3)
suite.Print()