from thinkbayes import Pmf
from thinkbayes import Suite
from thinkbayes import Percentile
import thinkplot

"""

VOU REVER PELA DECIMA VEZ ESSE CARA.


The dice problem
    Tenho dados de 4, 6, 8, 12 e 20 faces
    Seleciono um dado por acaso. Rolo ele. Tiro 6.
    Qual eh a probabilidade de que
        o dado seja o dado de 4 faces?
        o dado seja de 6 faces?
        o dado seja de 8 faces?
        assim por diante.

    Vou, primeira coisa, fazer isso com o teorema de bayes, na mao, para ver
    se eu me lembro. Depois, vou fazer usando o codigo do cara do livro.


      hip priori     likelihood     multip
      P(H)           P(H|D)         P(H)*P(H|D)                                 P(D|H)
H4    1./5           0              0                                           0
H6    1./5           1./6           1./5  * 1./6                                0.36
H8    1./5           1./8           1./5  * 1./8                                0.27
H12   1./5           1./12          1./5  * 1./12                               0.18
H20   1./5           1./20          1./5  * 1./12                               0.18
                                    somatorio = 0.09166666666666666


antes de seguir para a parte seguinte, de codar o exemplo do cara, vou rever todo o livro para
entendere essa tabelinha aqui de cima again.

P(A|B) = P(A) * P(B|A)
         -------------
             P(B)

vanilla
b1:     30 vanilla 10 chocolates
b2:     20 vanilla 20 chocolates


P(bowl1|vanilla) = P(bowl1) * P(vanilla|bowl1)
                   ---------------------------
                          P(vanilla)

p(bowl1|vanilla) = .5 * (3./4) / (50./80.)
                 = .6

        priori   likelihood
        P(H)     P(D|H)       MULT
bowl1   .5       3./4         .375
bowl2   .5       2./4         .25
                            soma: .625
                            notar que .625 === 50/80

                            entao eu faco a divisao para normalizar.

                            fimm.
                            estah deduzida novamente a relacao entre
                            o teorema de bayes e a tabelinha magica.

agora, estou pronto novamente para codar o codigo do cara do livro.


primeiro, vou recapitular o problema do dado para poder implementa-lo.



The dice problem
    Tenho dados de 4, 6, 8, 12 e 20 faces
    Seleciono um dado por acaso. Rolo ele. Tiro 6.
    Qual eh a probabilidade de que
        o dado seja o dado de 4 faces?
        o dado seja de 6 faces?
        o dado seja de 8 faces?
        assim por diante.

    Vou, primeira coisa, fazer isso com o teorema de bayes, na mao, para ver
    se eu me lembro. Depois, vou fazer usando o codigo do cara do livro.


      hip priori     likelihood     multip
      P(H)           P(H|D)         P(H)*P(H|D)                                 P(D|H)
H4    1./5           0              0                                           0
H6    1./5           1./6           1./5  * 1./6                                0.36
H8    1./5           1./8           1./5  * 1./8                                0.27
H12   1./5           1./12          1./5  * 1./12                               0.18
H20   1./5           1./20          1./5  * 1./12                               0.18
                                    somatorio = 0.09166666666666666
            >> notar que resolvi de forma errada, porque na ultima hipotese, considerei que
            o dado tinha 12 faces em vez de 20. mas tudo bem. capturei a essencia.


"""


class Dice(Suite):

    def Likelihood(self, data, hypo):
        if hypo < data:
            return 0
        else:
            return 1./hypo


suite = Dice([4, 6, 8, 12, 20])
suite.Update(6)
suite.Update(6)
suite.Update(12)
suite.Print()