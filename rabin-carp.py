def hash(a):
    n = len(a)
    sum = 0
    for i in range(0, n):
        sum += ord(a[i]) * 2**(i+1)
    return sum

def Rabin_Karp(a, sub):
    ind = []
    n = len(a)
    m = len(sub)
    hs = hash(a[:m])
    hsub = hash(sub)
    for i in range(0, n - m):
        if hs == hsub:
            ind += [i]
        hs = (hs - 2*ord(a[i])) // 2 + ord(a[m+i]) * 2**m
    if hs == hsub:
        ind += [i+1]    
    return ind

print(Rabin_Karp('abcefadbcghabcdabcd', 'abcd'))
