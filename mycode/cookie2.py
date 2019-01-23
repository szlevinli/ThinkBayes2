######################################################################
#
# 使用 Suite 类来实现 cookie 问题
#
######################################################################

from thinkbayes2 import Suite


class Cookie(Suite):

    mixes = {
        'Bowl 1': dict(vanilla=30, cocalate=10),
        'Bowl 2': dict(vanilla=20, cocalate=20)
    }

    def Likelihood(self, data, hypo):
        totalCookies = 0
        for v in self.mixes[hypo].values():
            totalCookies += v
        cookie = self.mixes[hypo][data]
        return (cookie / totalCookies)


def main():
    cookie = Cookie(('Bowl 1', 'Bowl 2'))
    cookie.Update('vanilla')
    cookie.Print()


if __name__ == '__main__':
    main()
