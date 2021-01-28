import itertools

fibs = [1, 0]

class Fibs:

    class _numbers_:
        def __init__(self):
            self.i = 0

        def __next__(self):
            cmp = fibs[0]
            fibs[0] = fibs[1]
            fibs[1] = cmp + fibs[1]
            return fibs[1]

    def __iter__(self):
        return Fibs._numbers_()
    
f = Fibs()
print(list(itertools.islice(f, 20)))
