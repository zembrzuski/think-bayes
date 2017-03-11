from thinkbayes import Pmf
from chap02_file04_encapsulating_framework import Suite

### the cookie problem

# bowl 1 --> 30 vanilla         10 chocolate
# bowl 2 --> 20 vanilla         20 chocolate
# peguei 1 cookie de vanilla. qual probabilidade que seja do bowl1?






# prior distribution
pmf = Pmf()
pmf.Set('Bowl 1', .5)
pmf.Set('Bowl 2', .5)

# we will update the distribution based on the vanilla dataa.
pmf.Mult('Bowl 1', 0.75) # isso acontece pois temos 30 vanilla / 40 total
pmf.Mult('Bowl 2', 0.5)  # isso acontece pois temos 20 vanilla / 40 total

pmf.Normalize()

print(pmf.Prob('Bowl 1'))
print(pmf.Prob('Bowl 2'))



### refactoring now.
### I can't understand why is he doing it now.

class Cookie(Suite):

    mixes = {
        'Bowl 1': dict(vanilla=0.75, chocolate=0.25),
        'Bowl 2': dict(vanilla=0.5, chocolate=0.5),
    }

    def Likelihood(self, data, hypo):
        mix = self.mixes[hypo]
        like = mix[data]
        return like

# prior probabilities
hypos = ['Bowl 1', 'Bowl 2']
pmf = Cookie(hypos)
pmf.Update('vanilla')
pmf.Print()