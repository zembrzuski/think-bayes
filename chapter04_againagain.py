from thinkbayes import Pmf
from thinkbayes import Suite
from thinkbayes import Percentile
from thinkbayes import CredibleInterval
import thinkplot

"""
agora que fiz uma enorme recapitulacao, vou recomecar com o chapter 4.
o conteudo ja esta fresquinho na minha memoria agora.


the euro problem:
    girei a moeda 250 vezes
        - 140 heads
        - 110 tails

    vou criar, entao, 101 hipoteses, em que cada hipotese eh a probabilidade de que de heads.



    se jogo a moeda uma vez, somente e tiro heads.

        priori      likelihood                  posteriori
        P(H)        P(D|H)                      P(H|D)
H0      1./101      0/100
H1      1./101      1/100
H2      1./101      2/200
H3      1./101      3/100
...
H100    1./101      100/100

                    depois, faco o fluxo normal e chego nas probabilidades a posteriori.
                    entretanto, nao vou fazer o passo completo aqui. vou desenovlver mais



se jogo duas moedas e tiro HEADS HEADSA.

        priori      likelihood                  posteriori
        P(H)        P(D|H)                      P(H|D)
H0      1./101      0/100
H1      1./101      1/100
H2      1./101      2/200
H3      1./101      3/100
...
H100    1./101      100/100



"""



def PlotSuites(suites, root):
    """Plots two suites.

    suite1, suite2: Suite objects
    root: string filename to write
    """
    thinkplot.Clf()
    thinkplot.PrePlot(len(suites))
    thinkplot.Pmfs(suites)

    thinkplot.Save(root=root,
                   xlabel='x',
                   ylabel='Probability',
                   formats=['pdf', 'eps'])


class Euro(Suite):

    def Likelihood(self, data, hypo):
        if data == 'H':
            return hypo/100.
        if data == 'T':
            return 1 - hypo/100.


suite = Euro(xrange(0, 101))
dataset = 'H' * 140 + 'T' * 110

for data in dataset:
    suite.Update(data)

#suite.Print()
print("maximum likelihood" + str(suite.MaximumLikelihood()))
print("mean " + str(suite.Mean()))
print("median " + str(Percentile(suite, 50)))
print("credible interval " + str(CredibleInterval(suite, 90)))
print(suite.Prob(50))
#PlotSuites([suite], 'euro1')

print("finished.")



def TrianglePrior():
    suite = Euro()
    for x in range(0, 51):
        suite.Set(x, x)
    for x in range(51, 101):
        suite.Set(x, 100-x)
    suite.Normalize()

