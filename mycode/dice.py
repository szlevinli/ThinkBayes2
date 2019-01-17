###############################################################################
#
# 骰子问题：
#     有一袋子骰子，分别是4面、6面、8面、12面和20面。
#     假设随机从袋子里拿出一个骰子，投骰子结果为6，问投出6的这个骰子是袋中每个骰子的概率分别是多少
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
