import random
import collections
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


class MegaMap():

    def __init__(self):
        self.counts = dict()

    def incr(self, key):
        if key in self.counts:
            self.counts[key] = self.counts[key] + 1
        else:
            self.counts[key] = 1

    def imprime(self):
        ordered = collections.OrderedDict(sorted(self.counts.items()))
        for k, v in ordered.iteritems(): print k, v

    def get_data(self):
        ordered = collections.OrderedDict(sorted(self.counts.items()))
        return ordered


megamap = MegaMap()
sampleSize = 10000

for i in xrange(1, sampleSize):
    dice_sum = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
    megamap.incr(dice_sum)

keys = megamap.get_data().keys()
values = map(lambda x: x[1], megamap.get_data().items())
y_pos = np.arange(len(keys))

plt.bar(y_pos, values, align='center', alpha=0.5)
plt.xticks(y_pos, keys)
plt.show()

# a parte da simulacao, que eh trivial, eu ja fiz. agora vou fazer a da enumeracao,
# que eh bem mais dificil. mas, de qualquer maneira, acho que eh bem facil.

