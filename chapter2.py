from thinkbayes import Pmf

# pmf -> probability mass function. eh a distribuicao, no fim das contas.
pmf = Pmf()
for x in [1, 2, 3, 4, 5, 6]:
    pmf.Set(x, 1/6.)


phrase = "gremio gremio inter"
word_list = phrase.split(" ")

pmf = Pmf()
for word in word_list:
    pmf.Incr(word, 1)

pmf.Normalize()

print(pmf.Prob('gremio'))
print(pmf.Prob('inter'))



### the cookie problem

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
