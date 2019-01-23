######################################################################
#
# 火车头问题：
#   通过调整先验概率(prior)的分布方式（将火车头的平均分布概率(uniform)调整为
# 幂律概率(power law)分布），来提升后验概率的准确度
#
######################################################################

from thinkbayes2 import Pmf
from dice import Dice


class Locomotive(Dice):
    def __init__(self, hypos, alpha=1.0):
        Pmf.__init__(self)
        '''
        父类对prior的概率分布采用的是平均分布(uniform distribution)
        此处改写prior的概率分布为幂律(power law distribution)
        '''
        for hypo in hypos:
            self.Set(hypo, hypo**(-alpha))
        self.Normalize()


def execute(observations=[], num=[]):
    """
    docstring here
        :param observations=[]: 
        :param num=[]: 
    """
    locomotive = Locomotive(num)
    for i in observations:
        locomotive.Update(i)
    return '拥有{}个火车头的情况下，观察到的火车头编号为{}，则预测结果平均值为{}'.format(len(num), observations, locomotive.Mean())


def main():
    observations = [60]
    fleets = [range(1, 501), range(1, 1001), range(1, 2001)]
    for fleet in fleets:
        print(execute(observations, fleet))

    print('*'*80)

    observations = [60, 30]
    fleets = [range(1, 501), range(1, 1001), range(1, 2001)]
    for fleet in fleets:
        print(execute(observations, fleet))

    print('*'*80)

    observations = [60, 30, 90]
    fleets = [range(1, 501), range(1, 1001), range(1, 2001)]
    for fleet in fleets:
        print(execute(observations, fleet))


if __name__ == '__main__':
    main()
