from thinkbayes import Pmf


## cookie problem.

cookie = Pmf()
cookie.Set('b1', .5)
cookie.Set('b2', .5)

cookie.Mult('b1', .75)
cookie.Mult('b2', .5)

cookie.Normalize()

print(cookie.Prob('b1'))
print(cookie.Prob('b2'))



## monty hall problem

pmf = Pmf()
x = 1./3
pmf.Set('A', x)
pmf.Set('B', x)
pmf.Set('C', x)

pmf.Mult('A', .5)
pmf.Mult('B', 0)
pmf.Mult('C', 1)

pmf.Normalize()

print(pmf.Prob('A'))
print(pmf.Prob('B'))
print(pmf.Prob('C'))





## mm's problem

pmf = Pmf()
x = 1./2
pmf.Set('A', x)
pmf.Set('B', x)

