###############################################################################
#
#
#
###############################################################################
import sys

sys.path.insert(0, '../thinkbayes2')

from thinkbayes2 import Suite

class Dice(Suite):

  def Likelihood(self, data, hypo):
    if hypo < data:
      return 0
    else:
      return 1 / hypo

dice = Dice([4, 6, 8, 12, 20])
dice.Update(6)
dice.Print()
for roll in [6, 8, 7, 7, 5, 4]:
  dice.Update(roll)
dice.Print()
