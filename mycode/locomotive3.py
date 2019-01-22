######################################################################
#
# 火车头问题：
#   通过调整先验概率(prior)的分布方式（将火车头的平均分布概率(uniform)调整为
# 幂律概率(power law)分布），来提升后验概率的准确度
#
######################################################################

from thinkbayes2 import Pmf
from .dice import Dice


class Locomotive(Dice):
    def __init__(self, hypos, alpha=1.0):
        Pmf.__init__(self)
        for hypo in hypos:
            self.Update(hypo, hypo**(-alpha))
        self.Normalize()
