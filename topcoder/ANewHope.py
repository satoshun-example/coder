import math


class ANewHope:
    def count(self, firstWeek, lastWeek, D):
        if firstWeek == lastWeek:
            return 1

        m = 0
        for i, e in enumerate(firstWeek):
            for j, e2 in enumerate(lastWeek):
                if e == e2:
                    mm = i - j
                    if mm > m:
                        m = mm
                        break
        return math.ceil(m / (len(firstWeek) - D)) + 1


hope = ANewHope()
assert hope.count((1,2,3,4), (4,3,2,1),3) == 4
assert hope.count((8,5,4,1,7,6,3,2), (2,4,6,8,1,3,5,7),3) == 3
