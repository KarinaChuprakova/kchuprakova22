import turtle as tl

def draw_fractal(scale):
    if scale <= 8:
        tl.fd(scale)
        return
    draw_fractal(scale / 2.0)
    tl.left(15)
    draw_fractal(scale / 2.0)
    tl.right(45)
    draw_fractal(scale / 2.0)
    tl.left(15)
    draw_fractal(scale / 2.0)


tl.speed(0)
scale = 450
tl.penup()
tl.backward(scale / 2.0)
tl.pendown()
tl.color("blue")

draw_fractal(scale)
tl.done()
