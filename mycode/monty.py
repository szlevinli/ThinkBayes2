######################################################################
#
#
#
######################################################################
from thinkbayes2 import Pmf


class Monty(Pmf):

    def __init__(self, hypos):
        Pmf.__init__(self)
        for hypo in hypos:
            self.Set(hypo, 1)
        self.Normalize()

    def Update(self, data):
        for hypo in self.Values():
            like = self.Likelihood(data, hypo)
            self.Mult(hypo, like)
        self.Normalize()

    def Likelihood(self, data, hypo):
        if hypo == data:
            return 0
        elif hypo == 'A':
            return 0.5
        else:
            return 1


def main():
    hypos = 'ABC'
    monty = Monty(hypos)
    data = 'B'
    monty.Update(data)

    for hypo, prob, in monty.Items():
        print('{}: {}'.format(hypo, prob))


if __name__ == '__main__':
    main()
