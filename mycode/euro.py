######################################################################
#
# Euro Problem
#   这个是著名的“欧元”问题，该问题描述如下：
#   当一枚欧元硬币以边缘旋转250次，得到正面为140次，反面110次。这个结果是否对
# “硬币是偏心的而非均匀”提供了证据呢？
#
#   这个问题实际上描述了，当我们观察到了一组数据，这些数据可以提供什么作证呢？
#
#   使用贝叶斯理论来分析这个问题，首先需要明确我们的问题，即这枚硬币是否是均匀的？
# 换个角度看，如果这枚硬币是均匀的，那么即得到正面H的概率应接近50%
#
# - 第一步：设定“假设”，我们可以设定101个假设，即硬币的偏心率从0%到100%
# - 第二步：我们假定上面的假设的概率分布为平均分布（uniform distribution)
# - 第三步：在假设的情况下，似然值的计算。比如在假设“偏心率”是1%时，得到正面H的
#         概率应为1%，而得到反面T的概率应为99%。将其数学化，在假设“偏心率”是
#         x%的时候，得到正面H的概率为x%，而得到反面T的概率是1-x%
#
######################################################################

from thinkbayes2 import Suite
import thinkplot


class Euro(Suite):

    def Likelihood(self, data, hypo):
        x = hypo
        if data == 'H':
            return x / 100
        else:
            return 1 - x / 100


def main():
    hypos = range(0, 101)
    dataset = 'H' * 140 + 'T' * 110
    euro = Euro(hypos)
    for data in dataset:
        euro.Update(data)
    thinkplot.Clf()
    thinkplot.Pmf(euro)
    thinkplot.show()


if __name__ == '__main__':
    main()
