a = 401

def prime_number(a):
    b = 2
    while a % b != 0:
        b += 1
    return a == b

print(prime_number(a))
