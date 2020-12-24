import numpy as np
from numpy.linalg import norm
from numpy.linalg import solve as solve_out_of_the_box
from numpy import array

ab = array([
    [1.5, 2.0, 1.5, 2.0, 5.0],
    [3.0, 2.0, 4.0, 1.0, 6.0],
    [1.0, 6.0, 0.0, 4  , 7.0],
    [2.0, 1.0, 4.0, 3  , 8.0]
], dtype=float)

def gauss(a, b):
   
    def forward():
        n = len(ab)
        for k in range(n - 1):
            for i in range(k + 1, n):
                div = ab[i][k] / ab[k][k]
                ab[i][-1] -= div * ab[k][-1]
                for j in range(k, n):
                    ab[i][j] -= div * ab[k][j]

    def backward():
        n = len(ab)
        x = np.zeros(len(b), dtype=float)
        for k in range(n - 1, -1, -1):
            x[k] = (ab[k][-1] - sum([ab[k][j] * x[j] for j in range(k + 1, n)])) / ab[k][k]
        return x

    forward()
    x = backward()
    return x

a = array([
    [1.5, 2.0, 1.5, 2.0],
    [3.0, 2.0, 4.0, 1.0],
    [1.0, 6.0, 0.0, 4  ],
    [2.0, 1.0, 4.0, 3  ]
], dtype=float)

b = array([5, 6, 7, 8], dtype=float)

oob_solution = solve_out_of_the_box(a, b)
solution = gauss(a, b)

print(solution)
print("Макс отклонение компоненты решения:", norm(solution-oob_solution, ord=1))
