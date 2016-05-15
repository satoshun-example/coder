class AccessChanger:
    def convert(self, lines):
        np = []
        for line in lines:
            a  = line.split('//', 2)
            if len(a) == 1:
                a[0] = a[0].replace('->', '.')
                np += [a[0]]
            else:
                a[0] = a[0].replace('->', '.')
                np += [a[0] + '//' + a[1]]
        return tuple(np)

changer = AccessChanger()
assert changer.convert(("Test* t = new Test();", "t->a = 1;", "t->b = 2;", "t->go(); // a=1, b=2 --> a=2, b=3")) == ("Test* t = new Test();", "t.a = 1;", "t.b = 2;", "t.go(); // a=1, b=2 --> a=2, b=3")
