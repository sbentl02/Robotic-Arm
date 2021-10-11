from svgpathtools import svg2paths2
import time

def setup_SVG(filename):
    paths, attributes, svg_attributes = svg2paths2(filename)
    dimensions = svg_attributes['viewBox']
    dims = dimensions.split()

    return paths


def get_xy(xy_coords, timestep):
    xy = xy_coords[timestep]
    return xy[0], xy[1], xy[2]

def read_SVG(filename, sampling_rate):
    paths, attributes, svg_attributes = svg2paths2(filename)
    dimensions = svg_attributes['viewBox']
    dims = dimensions.split()
    #TODO: something to scale dimensions to appropriate

    xy_coords = []

    for path in paths:
        print("New path")
        for seg in path:
            print("New seg")
            for i in range(0, sampling_rate):
                if (i+1 >= sampling_rate): #End of segment, pen up
                    xy = tuple((seg.point(i/sampling_rate).real, seg.point(i/sampling_rate).imag, 0))
                elif (i == 0): #Beginning of segment, pen down
                    xy = tuple((seg.point(i/sampling_rate).real, seg.point(i/sampling_rate).imag, 1))   
                else: 
                    xy = tuple((seg.point(i/sampling_rate).real, seg.point(i/sampling_rate).imag, 1))
                #print(seg.point(i/sampling_rate).real, seg.point(i/sampling_rate).imag)
                xy_coords.append(xy)

    return xy_coords
                
xy_coords = read_SVG('SCB.svg', 10)

x,y,down = get_xy(xy_coords, len(xy_coords) - 12)
print(x, y, down)

