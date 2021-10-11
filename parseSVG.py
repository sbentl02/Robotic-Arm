from svgpathtools import svg2paths2
import turtle, time

# t.goto(10,10)
# t.pendown()
# t.goto(100,100)
# t.penup()

# turtle.done()

def read_SVG(filename, sampling_rate):
    paths, attributes, svg_attributes = svg2paths2(filename)
    s = turtle.Screen()
    t = turtle.Turtle()
    s.reset()
    dimensions = svg_attributes['viewBox']
    dims = dimensions.split()
    #s.setworldcoordinates(int(dims[0]), int(dims[1]), int(dims[2]), int(dims[3]))
    s.setworldcoordinates(-50, -50, 50,50)

    print(len(paths))
    for path in paths:
        print(len(path))
    for path in paths:
        time.sleep(1)
        print("New path")
        for seg in path:
            # seg = path[0]
            print("New seg")
            t.penup()
            t.goto(seg.point(0).real, seg.point(0).imag)
            t.pendown()
            for i in range(0, sampling_rate):
                t.goto(seg.point(i/sampling_rate).real, seg.point(i/sampling_rate).imag)
                print(seg.point(i/sampling_rate).real, seg.point(i/sampling_rate).imag)
            t.penup()
                    
read_SVG('SCB.svg', 10)

