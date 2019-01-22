######################################################################
#
# 使用火车头问题去理解 prior
#
######################################################################
from locomotive import Locomotive


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
