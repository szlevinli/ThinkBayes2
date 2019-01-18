######################################################################
#
# 火车头问题
#     有个火车车队拥有N辆火车头，每个火车头都有个编号，从1-N，他每分钟按从小到大
# 的顺序发车。加入某时某地你看到一个火车头是60号，那么请问发出了多少辆火车？
#
######################################################################
import sys

sys.path.insert(0, '../thinkbayes2')
sys.path.insert(0, '../thinkplot')

import thinkplot
from thinkbayes2 import Suite

class Locomotive(Suite):

    def Likelihood(self, data, hypo):
        if hypo < data:
            return 0
        else:
            return 1.0/hypo


locomotiveNumbers = range(1, 1001)
locomotive = Locomotive(locomotiveNumbers)
locomotive.Update(60)
locomotive.Update(160)
locomotive.Update(80)
locomotive.Update(570)
locomotive.Update(640)
print('Mean: {}'.format(locomotive.Mean()))

thinkplot.preplot(1)
thinkplot.Pmf(locomotive)
thinkplot.show(xlabel='Number of train',
               ylabel='Probability')
