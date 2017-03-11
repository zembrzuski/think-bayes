from chap02_file04_encapsulating_framework import Suite

class Dice(Suite):
    def Likelihood(self, data, hypo):
        if hypo < data:
            return 0
        else:
            return 1.0 / hypo


suite = Dice([4, 6, 8, 12, 20])
#suite .Update(6)

#for roll in [6, 8, 7, 7, 5, 4]:
#    suite.Update(roll)

for roll in [6, 8]:
    suite.Update(roll)

suite.Print()

