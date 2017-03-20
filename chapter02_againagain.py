
"""

PMF - probability mass function

"""

from thinkbayes import Pmf
from thinkbayes import Suite


# introducing pmf.
pmf = Pmf()
for x in [1, 2, 3, 4, 5, 6]:
    pmf.Set(x, 1./6)





# re-introducing pmf.
word_list = ['atirei', 'o', 'pau', 'atirei', 'gato', 'gato']

pmf = Pmf()
for word in word_list:
    pmf.Incr(word, 1)
pmf.Normalize()

print(pmf.Prob('gato'))








# the cookie problemm
pmf = Pmf()
pmf.Set("bowl 1", .5)
pmf.Set("bowl 2", .5)

pmf.Set("bowl 1", .75)
pmf.Set("bowl 2", .5)

pmf.Normalize()
print(pmf.Prob('bowl 1'))






# the cookie prolem using a class -- more generic than the previous
class Cookie(Pmf):

    mixes = {
        'Bowl 1': dict(vanilla=0.75, chocolate=0.25),
        'Bowl 2': dict(vanilla=0.5, chocolate=0.5),
    }

    def __init__(self, hypos):
        Pmf.__init__(self)
        for hypo in hypos:
            self.Set(hypo, 1)
        self.Normalize()

    def Update(self, data):
        for hypo in self.Values():
            like = self.Likelihood(data, hypo)
            self.Mult(hypo, like)
        self.Normalize()

    def Likelihood(self, data, hypo):
        mix = self.mixes[hypo]
        like = mix[data]
        return like



hypos = ["Bowl 1", "Bowl 2"]
pmf = Cookie(hypos)
pmf.Update('vanilla')

for hypo, prob in pmf.Items():
    print hypo, prob












# the monty hallprobblem

class Monty(Pmf):

    def __init__(self, hypos):
        Pmf.__init__(self)
        for hypo in hypos:
            self.Set(hypo, 1)
        self.Normalize()

    def Update(self, data):
        for hypo in self.Values():
            like = self.Likelihood(data, hypo)
            self.Mult(hypo, like)
        self.Normalize()

    def Likelihood(self, data, hypo):
        if hypo == data:
            return 0
        elif hypo == 'A':
            return .5
        else:
            return 1


hypos = ['A', 'B', 'C']
pmf = Monty(hypos)

data = 'B'
pmf.Update(data)

for hypo, prob in pmf.Items():
    print hypo, prob





class MontyDois(Suite):
    def Likelihood(self, data, hypo):
        if hypo == data:
            return 0
        elif hypo == 'A':
            return .5
        else:
            return 1


print("monty problem using suite")
suite = MontyDois('ABC')
suite.Update('B')
suite.Print()









# the mm problem


class MandM(Suite):
    mix94 = dict(brown=30, yellow=20, red=20, green=10, orange=10, tan=10)
    mix96 = dict(blue=24, green=20, orange=16, yellow=14, red=13, brown=13)

    hypoA = dict(bag1=mix94, bag2=mix96)
    hypoB = dict(bag1=mix96, bag2=mix94)

    hypotheses = dict(A=hypoA, B=hypoB)

    def Likelihood(self, data, hypo):
        bag, color = data

        mix = self.hypotheses[hypo][bag]
        like = mix[color]
        return like

print('mm probblem')
suite = MandM('AB')
suite.Update(('bag1', 'yellow'))
suite.Update(('bag2', 'green'))
suite.Print()



