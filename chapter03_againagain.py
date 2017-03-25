from thinkbayes import Pmf
from thinkbayes import Suite
from thinkbayes import Percentile
import thinkplot

"""
the dice problem:

4, 6, 8, 12, 20 faces.
tirei um 6.
qual eh a probabilidade de que rolei o dado 4?
qual eh a probabilidade de que rolei o dado 6?
assim por  diante.


"""


class Dice(Suite):

    def Likelihood(self, data, hypo):
        if hypo < data:
            return 0
        return 1./hypo

suite = Dice([4, 6, 8, 12, 20])

suite.Update(6)

for roll in [6, 8, 7, 7, 5, 4]:
    suite.Update(roll)

suite.Print()








"""
The locomotive problem.

Existe uma ferrovia, em que os vagoes sao numerados de 1..N
Vi um cara com numero 60.
Estima o numero de locomotivas que existem.
"""

hypos = xrange(1, 1001)

class Train(Suite):

    def Likelihood(self, data, hypo):
        if hypo < data:
            return 0
        else:
            return 1./hypo

suite = Train(hypos)
suite.Update(60)

"""
thinkplot.PrePlot(1)
thinkplot.Pmf(suite)
thinkplot.Save(root='train1',
               xlabel='Number of trains',
               ylabel='Probability',
               formats=['pdf', 'eps'])
"""

def Mean(suite):
    total = 0
    for hypo, prob in suite.Items():
        total += hypo * prob
    return total

print(Mean(suite))





class Train(Dice):
    def __init__(self, hypos, alpha=1.0):
        Pmf.__init__(self)
        for hypo in hypos:
            self.Set(hypo, hypo**(-alpha))
        self.Normalize()


print("agoravai")
hypos = range(1, 2000)
suite = Train(hypos)
suite.Update(30)
suite.Update(60)
suite.Update(90)
print(suite.Mean())

print(Percentile(suite, 5))
print(Percentile(suite, 95))
