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

