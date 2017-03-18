import random
import collections
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import random
import collections
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt



class Megamap:

    def __init__(self):
        self.pmf = dict()

    def increment(self, key):
        if key in self.pmf:
            self.pmf[key] += 1
        else:
            self.pmf[key] = 1

    def imprime(self):
        ordered = collections.OrderedDict(sorted(self.pmf.items()))
        for k, v in ordered.iteritems(): print k, v

    def get_data(self):
        ordered = collections.OrderedDict(sorted(self.pmf.items()))
        return ordered


megamap = Megamap()

for i in xrange(1, 50):
    soma = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
    megamap.increment(soma)


keys = megamap.get_data().keys()
values = map(lambda x: x[1], megamap.get_data().items())
y_pos = np.arange(len(keys))

plt.bar(y_pos, values, align='center', alpha=0.5)
plt.xticks(y_pos, keys)
plt.show()

