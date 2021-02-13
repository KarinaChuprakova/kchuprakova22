a = 2717
b = 2337
def gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        c, x1, y1 = gcd(b, a % b)
        return c, y1, x1- (a // b) * y1
    
print(gcd(a, b))
