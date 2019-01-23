######################################################################
#
#
#
######################################################################
from thinkbayes2 import Suite


class M_and_M(Suite):

    def __init__(self, hypos):
        Suite.__init__(self, hypos)
        self.mix94 = dict(
            brown=30,
            yellow=20,
            red=20,
            green=10,
            orange=10,
            tan=10
        )
        self.mix96 = dict(
            blue=24,
            green=20,
            orange=16,
            yellow=14,
            red=13,
            brown=13
        )
        self.hypoA = dict(bag1=self.mix94, bag2=self.mix96)
        self.hypoB = dict(bag1=self.mix96, bag2=self.mix94)
        self.hypotheses = dict(A=self.hypoA, B=self.hypoB)

    def Likelihood(self, data, hypo):
        bag, color = data
        mix = self.hypotheses[hypo][bag]
        like = mix[color]
        return like


def main():
    m_and_m = M_and_M('AB')
    m_and_m.Update(('bag1', 'yellow'))
    m_and_m.Update(('bag2', 'green'))

    m_and_m.Print()


if __name__ == '__main__':
    main()
