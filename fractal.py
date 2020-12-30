import turtle as tl
scale = 200
n = 4
def draw_fractal(scale, n):
    if n == 0:
        tl.forward(scale)
    else:
        draw_fractal(scale / 3.0, n - 1)
        tl.left(45)
        draw_fractal(scale / 3.0, n - 1)
        tl.right(90)
        draw_fractal(scale / 3.0, n - 1)
        tl.left(45)
        draw_fractal(scale / 3.0, n - 1)

def draw_fractal_1(scale, n):
    for i in range(3):
        draw_fractal(scale, n)
        tl.right(120)


draw_fractal_1(scale, n)
tl.done()
