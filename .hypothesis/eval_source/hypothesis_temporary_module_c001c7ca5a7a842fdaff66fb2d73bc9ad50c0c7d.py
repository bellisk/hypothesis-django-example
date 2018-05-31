from hypothesis.utils.conventions import not_set

def accept(f):
    def test_median(self, portfolio=not_set, subs=not_set):
        return f(self=self, portfolio=portfolio, subs=subs)
    return test_median
