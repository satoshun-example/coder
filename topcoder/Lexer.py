class Lexer:
    def tokenize(self, tokens, s):
        v = []
        tokens = sorted(tokens, reverse=True)
        while s:
            for t in tokens:
                print(s)
                if s.startswith(t):
                    s = s[len(t):]
                    v += [t]
                    break
            else:
                s = s[1:]
        return tuple(v)


l = Lexer()
assert l.tokenize(("ab","aba","A"), "ababbbaAab") ==  ("aba", "A", "ab")
