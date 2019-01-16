# 使用 Suite 类来实现 cookie 问题

import sys

sys.path.insert(0, '../thinkbayes2')

from thinkbayes2 import Suite

class Cookie(Suite):

  mixes = {
    'Bowl 1': dict(vanilla=30, cocalate=10),
    'Bowl 2': dict(vanilla=20, cocalate=20)
  }