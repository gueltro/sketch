from random import randrange as r
# Setup size of the drawing table 
side_a = float(1000)
side_b = float(1000)

n = 7

def setup():
    size(side_a, side_b)

def draw():
    save("pic.jpeg")
    background(255)
    
    noStroke()
    fill(r(255), r(255), r(255))
    #[draw_square(i,j,r(2)) for i in range(n + 1) for j in range(n + 1)] 
    [draw_sim_square(i,j,r(2)) for i in range((n + 1)/2) for j in range((n + 1)/2)] 
    delay(1000)
    
def draw_square(x,y,is_colored):
    d_a = side_a / (n + 1) 
    d_b = side_b / (n + 1)
    if is_colored:
        rect(x * d_a, y * d_b, d_a + 1, d_b + 1, (d_a + d_b) / 16)

def draw_sim_square(x,y,is_colored):
    draw_square(x , y, is_colored)
    draw_square(n - x, y, is_colored)
    draw_square(x, n - y, is_colored)
    draw_square(n - x, n - y, is_colored)
