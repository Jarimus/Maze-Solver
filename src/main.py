from window import Window
from line import Line
from point import Point

def main():
    #open window
    win = Window(800, 600)

    #draw a few lines
    p0 = Point(0, 0)
    p1 = Point(100, 100)
    p2 = Point(200, 100)
    p3 = Point(100, 200)
    line1 = Line(p0, p1)
    line2 = Line(p0, p2)
    line3 = Line(p0, p3)
    lines = [line1, line2, line3]
    for line in lines:
        win.draw_line(line, "red")

    #wait for close
    win.wait_for_close()



if __name__ == '__main__':
    main()