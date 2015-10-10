from random import randrange as r
# Setup size of the drawing table 
radius = float(500)
side_a =   2 * radius
side_b =   2 * radius
#Number of sections
n = 10
#Number of annuluses 
m = 10

def setup():
    size(side_a, side_b)

def draw():
    background(235)
    noStroke()
    draw_square(1, 10)
    delay(1000)

def draw_square(number_slices,number_annuluses):
    my_color = [r(255), r(255), r(255)]
    [draw_pie(number_slices, (1 - (float(k) / number_annuluses)) * radius, my_color) for k in range(number_annuluses + 1)]

def draw_pie(number_slices, radial_size, my_color):
    angular_size = 2 * PI / number_slices 
    [draw_arc(k * angular_size, (k + 1) *angular_size, radial_size, my_color) for k in range(number_slices)]
    
def draw_arc(angle_start, angle_stop, radial_size, my_color):
    print "draw arc with radial size " + str(radial_size)
    if r(2):
        #fill(*my_color)
        fill(0,0,0)
    else:
        fill(255,255,255)
        
    arc(radius,  radius, 2 * radial_size, 2 * radial_size, angle_start, angle_stop); 
