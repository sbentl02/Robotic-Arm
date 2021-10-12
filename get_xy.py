from svgpathtools import svg2paths2

def get_xy(xy_coords, timestep):
    #check timestep within bounds
    if (timestep >= len(xy_coords)):
        print("Timestep out of bounds")
        return
    xy = xy_coords[timestep]
    return xy[0], xy[1], xy[2]

def read_SVG(filename, sampling_rate):
    paths, attributes, svg_attributes = svg2paths2(filename)
    dimensions = svg_attributes['viewBox']
    dims = dimensions.split()
    #TODO: something to scale dimensions to appropriate?

    xy_coords = []

    for path in paths:
        for seg in path:
            for i in range(0, sampling_rate + 1):
                if (i+1 >= sampling_rate): #End of segment, pen up with 0
                    xy = tuple((seg.point(i/sampling_rate).real, seg.point(i/sampling_rate).imag, 0))
                elif (i == 0): #Beginning of segment, pen down when 1
                    xy = tuple((seg.point(i/sampling_rate).real, seg.point(i/sampling_rate).imag, 1))   
                else: 
                    xy = tuple((seg.point(i/sampling_rate).real, seg.point(i/sampling_rate).imag, 1))
                xy_coords.append(xy)
    return xy_coords


#Sample code    
#xy_coords = read_SVG('Examples\SCB.svg', 10)
#x,y,down = get_xy(xy_coords, len(xy_coords) - 12)
#print(x, y, down)

