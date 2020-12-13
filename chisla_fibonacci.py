class Fibn:
    class _Fibn_iter:
        def __init__(self):
            self.i = 0
            self.fibs = chisla
            
        def __next__(self):
                if self.i < 0:
                    raise StopIteration()
                else:
 n=int(input())
                    j = self.i
                    self.i += 1
                    return fibonacci(n - 1) + fibonacci(n - 2)
        def __iter__(self):
             return Fibn._Fibn_iter()

fn = Fibn()

for f in fn:
    print(f)
    
print(list(fn))
