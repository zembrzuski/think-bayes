
"""
bayes's theorem

p(A and B) = p(B and A)

p(A and B) = p(A) * p(B|A)
p(B and A) = p(B) * p(A|B)


p(A) * p(B|A) = p(B) * p(A|B)

p(B|A) = p(B) * p(A|B)
         -------------
            p(A)


mas gostamos de usar outras letras, entao

posteriori    priori     likelihood
p(H|D)      = p(H) * p(D|H)
            -------------
                p(D)   normalizacao


"""





"""
the cookie problem
bowl 1 --> 30 vanilla    10 chocolate
bowl 2 --> 20 vanilla    20 chocolate

pego um biscoito de vanilla. qual eh a probabilidade de que
tenha vindo do bowl1 ?

p(bowl1|vanilla) = ?

p(bowl1|vanilla) = p(bowl1) * p(vanilla|bowl1)
                   ---------------------
                      p(vanilla)


p(bowl1|vanilla) = .5 * 3/4
                   ------------
                      5/8
"""

print(.5*(3./4)/(5./8))



"""

tentando usar a tabelinha agora

hipotese A - veio do bowl1
hipotese B - veio do bowl2

    priori      likelihood                             posteriori
    p(H)        p(D|H)            p(H)*p(D|H)          p(H|D)
-------------------------------------------------------------------
A   .5          .75               .375                 .6
B   .5          .5                .25                  .4




the mm problem.
b94:        30% brown           20% yellow      20% red     10% green   10% orange      10% tan
b96:        24% blue            20% green       16% orange  14% yellow  13% red         13$ brown

yellow + green

qual eh a probabilidade que o yellow venha da bag b94?


HA - yellow veio do b94 e verde veio do b96
HB - yellow veio do b96 e verde veio do b94


   priori      likelihood        multiplication       posteriori
-----------------------------------------------------------------------------------------
A  .5          .2 * .2           .02                   .74
B  .5          .14 * .1          .007                  .26






the monty hall problem.

eu estou na porta A;

HA - o premio esta na porta A
HB - o premio esta na porta B
HC - o premio esta na porca C

likelihood - probabilidade que o monty abra a porta B

   priori     likelihood      multiplication       posteriori
--------------------------------------------------------------------------------------------
A   1./3       .5             1.6666               .33333
B   1./3        0             0                    0
C   1./3        1             .3333                .66666s

"""
