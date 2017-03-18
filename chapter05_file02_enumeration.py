import random
import collections
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt



# primeira coisa: eu vou criar um dado de 3 faces

class MeuDado:

    def __init__(self, qtd_faces):
        prob_cada_face = 1./qtd_faces
        self.pmf = dict()
        for i in xrange(1, qtd_faces+1):
            self.pmf[i] = prob_cada_face

    def print_pmf(self):
        for k, v in self.pmf.items():
            print(str(k) + " - " + str(v))

    def retrieve_dado(self):
        return self.pmf



dado1 = MeuDado(6)
dado2 = MeuDado(6)



class MegaMap:

    def __init__(self):
        self.pmf = dict()

    def incrementa_probabilidade(self, key, value):
        if key in self.pmf:
            self.pmf[key] += value
        else:
            self.pmf[key] = value

    def get_data(self):
        ordered = collections.OrderedDict(sorted(self.pmf.items()))
        return ordered


megamap = MegaMap()

for v1, p1 in dado1.retrieve_dado().items():
    for v2, p2 in dado2.retrieve_dado().items():
        for v3, p3 in dado2.retrieve_dado().items():
            soma_valores = v1+v2+v3
            soma_probs = p1*p2*p3

            megamap.incrementa_probabilidade(soma_valores, soma_probs)


keys = megamap.get_data().keys()
values = map(lambda x: x[1], megamap.get_data().items())
y_pos = np.arange(len(keys))

plt.bar(y_pos, values, align='center', alpha=0.5)
plt.xticks(y_pos, keys)
plt.show()

