class ANDEquation:
    def restoreY(self, A):
        A = list(A)
        b = A[0]
        for a in A:
            b = b & a
        if A.count(b) >= 2:
            return b
        if b in A:
            A.remove(b)
            c = A[0]
            for a in A:
                c = c & a

            if c == b:
                return c

        return -1


e = ANDEquation()
assert e.restoreY([1, 3, 5]) == 1
assert e.restoreY([31, 7, 7]) == 7
assert e.restoreY([191411,256951,191411,191411,191411,256951,195507,191411,192435,191411, 191411,195511,191419,191411,256947,191415,191475,195579,191415,191411, 191483,191411,191419,191475,256947,191411,191411,191411,191419,256947, 191411,191411,191411]) == 191411
