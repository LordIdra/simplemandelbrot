from tkinter import *
from math import sqrt


def convert_from_rgb(rgb):
    return "#%02x%02x%02x" % rgb


def calculate(x, y):
    
    val = complex(x, y)
    it = 0

    while abs(val) <= 4 and it <= 50:
    
        val *= val
        val += complex(x, y)
        
        it += 1

    return it*5


w = Tk()
c = Canvas(width = 800, height = 800, bg = 'black')
c.pack()


for ix in range(-400, 400):
    for iy in range(-400, 400):
        
        color = calculate(ix/200, iy/200)
        c.create_rectangle(ix+400, iy+400, ix+405, iy+405, fill = convert_from_rgb((0, 0, int(color))), outline = convert_from_rgb((0, 0, int(color))))
        w.update()
