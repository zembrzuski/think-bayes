from chap02_file04_encapsulating_framework import Suite

class Monty(Suite):
    def Likelihood(self, data, hypo):
        if hypo == data:
            return 0
        elif hypo == 'A':
            return 0.5
        else:
            return 1

hypos = ['A', 'B', 'C']
pmf = Monty(hypos)
data = 'B'
pmf.Update(data)
pmf.Print()
