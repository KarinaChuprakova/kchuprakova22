def repeat(n):
    def my_decorator(true_function):
        def fake_function(result):
            for i in range(n):
                result = true_function(result)
            return result
        return fake_function
    return my_decorator

@repeat(2)
def plus_1(x):
    return x + 1

@repeat(0)
def mul_2(x):
    return x * 2

print(plus_1(3))
print(mul_2(4))
