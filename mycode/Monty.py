from sys import path

path.insert(0, '../thinkbayes2')

from thinkbayes2 import Pmf

class Monty(Pmf):

  def __init__(self, hypos):
    Pmf.__init__(self)
    for hypo in hypos:
      self.Set(hypo, 1)
    self.Normalize()